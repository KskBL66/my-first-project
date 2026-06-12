# 手势控制鼠标系统 - 人工智能导论期末项目

## 项目简介
本项目基于 MediaPipe 与 OpenCV 实现了一套实时手势识别与鼠标控制系统，通过识别手部关键点坐标，将不同手势映射为鼠标操作，实现非接触式人机交互。项目同时支持百度飞桨AI Studio云端静态图片演示与本地电脑实时摄像头运行。

## 运行环境
- 开发平台：百度飞桨 AI Studio、本地 VS Code
- 编程语言：Python 3.8+
- 核心依赖：
  - opencv-python
  - mediapipe==0.10.9
  - pyautogui（本地版）

### 依赖安装
```bash
# 安装所有依赖
pip install opencv-python mediapipe==0.10.9 pyautogui

核心功能
手部关键点检测：识别手部 21 个关键点并可视化绘制骨架连线。
手势识别：支持三种核心手势识别：
食指伸出 → 移动鼠标光标
拇食相触 → 鼠标左键单击
五指握拳 → 鼠标右键单击
跨平台适配：同时支持 AI Studio 云端静态图片演示与本地实时摄像头运行。

 运行方式
1. 云端演示（AI Studio）
将 main.ipynb 文件上传至 AI Studio 项目
运行依赖安装代码块，完成环境配置
上传一张手势图片并命名为 hand.jpg
运行静态图片识别代码块，查看识别结果
2. 本地运行（完整版）
安装依赖后运行 main.py
对着摄像头做出对应手势即可控制鼠标
按键盘 Q 键退出程序
项目文件说明
main.ipynb：AI Studio 云端运行的 Notebook 文件
main.py：本地电脑运行的完整版本 Python 脚本
README.md：项目说明文件
report.md：Markdown 格式项目技术报告
📝 注意事项
云端环境无法直接调用摄像头，需使用静态图片模式进行演示
本地运行时请确保光线充足，手部距离摄像头 30-100cm 以获得最佳识别效果

---

## 三、AI Studio完整可运行代码（直接复制到Notebook）
```python
# 1. 安装依赖（仅需运行一次）
!pip install opencv-python mediapipe==0.10.9 -q

# 2. 导入库
import cv2
import mediapipe as mp
import math
import matplotlib.pyplot as plt

# 3. 初始化MediaPipe手部检测
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# 4. 计算两点距离
def get_distance(p1, p2):
    return math.hypot(p1.x - p2.x, p1.y - p2.y)

# 5. 手势判断函数
def judge_gesture(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]
    wrist = landmarks[0]
    
    index_len = get_distance(index_tip, wrist)
    thumb_index_len = get_distance(thumb_tip, index_tip)

    if index_len > 0.2 and thumb_index_len > 0.15:
        return "食指伸出 - 移动光标"
    elif thumb_index_len < 0.08:
        return "拇食相触 - 左键单击"
    elif all(get_distance(tip, wrist) < 0.18 for tip in [index_tip, middle_tip, ring_tip, pinky_tip]):
        return "握拳 - 右键单击"
    else:
        return "未识别有效手势"

# 6. 静态图片演示
img_path = "hand.jpg"  # 请先上传一张手势图片并命名为hand.jpg
img = cv2.imread(img_path)
if img is None:
    print("错误：请先上传名为hand.jpg的图片到项目目录")
else:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    gesture_text = "无手部检测"
    if result.multi_hand_landmarks:
        for hand_lms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                img, hand_lms, mp_hands.HAND_CONNECTIONS,
                mp_draw.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=3),
                mp_draw.DrawingSpec(color=(255,0,0), thickness=2)
            )
            gesture_text = judge_gesture(hand_lms.landmark)

    cv2.putText(img, gesture_text, (20, 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    plt.figure(figsize=(8, 6))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.title(f"识别结果: {gesture_text}")
    plt.show()

    print("程序运行完成，手势识别结果已显示")