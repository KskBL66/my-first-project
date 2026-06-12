{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "053b1ec1-1ce1-4ab6-b75b-cba080b608d0",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-06-12T09:35:03.604778Z",
     "iopub.status.busy": "2026-06-12T09:35:03.604532Z",
     "iopub.status.idle": "2026-06-12T09:35:05.923760Z",
     "shell.execute_reply": "2026-06-12T09:35:05.923025Z",
     "shell.execute_reply.started": "2026-06-12T09:35:03.604750Z"
    },
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Looking in indexes: http://mirrors.baidubce.com/pypi/simple/\r\n",
      "Requirement already satisfied: opencv-python in ./external-libraries/lib/python3.10/site-packages (4.13.0.92)\r\n",
      "Requirement already satisfied: mediapipe==0.10.9 in ./external-libraries/lib/python3.10/site-packages (0.10.9)\r\n",
      "Requirement already satisfied: pyautogui in ./external-libraries/lib/python3.10/site-packages (0.9.54)\r\n",
      "Requirement already satisfied: absl-py in ./external-libraries/lib/python3.10/site-packages (from mediapipe==0.10.9) (2.4.0)\r\n",
      "Requirement already satisfied: attrs>=19.1.0 in /opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages (from mediapipe==0.10.9) (25.4.0)\r\n",
      "Requirement already satisfied: flatbuffers>=2.0 in ./external-libraries/lib/python3.10/site-packages (from mediapipe==0.10.9) (25.12.19)\r\n",
      "Requirement already satisfied: matplotlib in /opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages (from mediapipe==0.10.9) (3.10.8)\r\n",
      "Requirement already satisfied: numpy in ./external-libraries/lib/python3.10/site-packages (from mediapipe==0.10.9) (2.2.6)\r\n",
      "Requirement already satisfied: opencv-contrib-python in ./external-libraries/lib/python3.10/site-packages (from mediapipe==0.10.9) (4.13.0.92)\r\n",
      "Requirement already satisfied: protobuf<4,>=3.11 in /opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages (from mediapipe==0.10.9) (3.20.3)\r\n",
      "Requirement already satisfied: sounddevice>=0.4.4 in ./external-libraries/lib/python3.10/site-packages (from mediapipe==0.10.9) (0.5.5)\r\n",
      "Requirement already satisfied: python3-Xlib in ./external-libraries/lib/python3.10/site-packages (from pyautogui) (0.15)\r\n",
      "Requirement already satisfied: pymsgbox in ./external-libraries/lib/python3.10/site-packages (from pyautogui) (2.0.1)\r\n",
      "Requirement already satisfied: pytweening>=1.0.4 in ./external-libraries/lib/python3.10/site-packages (from pyautogui) (1.2.0)\r\n",
      "Requirement already satisfied: pyscreeze>=0.1.21 in ./external-libraries/lib/python3.10/site-packages (from pyautogui) (1.0.1)\r\n",
      "Requirement already satisfied: pygetwindow>=0.0.5 in ./external-libraries/lib/python3.10/site-packages (from pyautogui) (0.0.9)\r\n",
      "Requirement already satisfied: mouseinfo in ./external-libraries/lib/python3.10/site-packages (from pyautogui) (0.1.3)\r\n",
      "Requirement already satisfied: pyrect in ./external-libraries/lib/python3.10/site-packages (from pygetwindow>=0.0.5->pyautogui) (0.2.0)\r\n",
      "Requirement already satisfied: Pillow>=9.2.0 in /opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages (from pyscreeze>=0.1.21->pyautogui) (10.4.0)\r\n",
      "Requirement already satisfied: cffi in /opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages (from sounddevice>=0.4.4->mediapipe==0.10.9) (2.0.0)\r\n",
      "Requirement already satisfied: pycparser in /opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages (from cffi->sounddevice>=0.4.4->mediapipe==0.10.9) (2.23)\r\n",
      "Requirement already satisfied: contourpy>=1.0.1 in /opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages (from matplotlib->mediapipe==0.10.9) (1.3.2)\r\n",
      "Requirement already satisfied: cycler>=0.10 in /opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages (from matplotlib->mediapipe==0.10.9) (0.12.1)\r\n",
      "Requirement already satisfied: fonttools>=4.22.0 in /opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages (from matplotlib->mediapipe==0.10.9) (4.61.1)\r\n",
      "Requirement already satisfied: kiwisolver>=1.3.1 in /opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages (from matplotlib->mediapipe==0.10.9) (1.4.9)\r\n",
      "Requirement already satisfied: packaging>=20.0 in /opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages (from matplotlib->mediapipe==0.10.9) (25.0)\r\n",
      "Requirement already satisfied: pyparsing>=3 in /opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages (from matplotlib->mediapipe==0.10.9) (3.3.1)\r\n",
      "Requirement already satisfied: python-dateutil>=2.7 in /opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages (from matplotlib->mediapipe==0.10.9) (2.9.0.post0)\r\n",
      "Requirement already satisfied: six>=1.5 in /opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages (from python-dateutil>=2.7->matplotlib->mediapipe==0.10.9) (1.17.0)\r\n",
      "Requirement already satisfied: pyperclip in /opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages (from mouseinfo->pyautogui) (1.11.0)\r\n",
      "Note: you may need to restart the kernel to use updated packages.\r\n"
     ]
    }
   ],
   "source": [
    "pip install opencv-python mediapipe==0.10.9 pyautogui"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1e93f5ac-8a73-4c53-9622-1389b13ee82d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-06-12T09:35:08.592224Z",
     "iopub.status.busy": "2026-06-12T09:35:08.591970Z",
     "iopub.status.idle": "2026-06-12T09:35:10.404901Z",
     "shell.execute_reply": "2026-06-12T09:35:10.404120Z",
     "shell.execute_reply.started": "2026-06-12T09:35:08.592194Z"
    },
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'DISPLAY'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[2], line 4\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mmediapipe\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mmp\u001b[39;00m\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mmath\u001b[39;00m\n\u001b[0;32m----> 4\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mpyautogui\u001b[39;00m\n\u001b[1;32m      6\u001b[0m \u001b[38;5;66;03m# 关闭pyautogui安全边界限制\u001b[39;00m\n\u001b[1;32m      7\u001b[0m pyautogui\u001b[38;5;241m.\u001b[39mFAILSAFE \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mFalse\u001b[39;00m\n",
      "File \u001b[0;32m~/external-libraries/lib/python3.10/site-packages/pyautogui/__init__.py:246\u001b[0m\n\u001b[1;32m    242\u001b[0m     screenshot \u001b[38;5;241m=\u001b[39m _couldNotImportPyScreeze\n\u001b[1;32m    245\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 246\u001b[0m     \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mmouseinfo\u001b[39;00m\n\u001b[1;32m    248\u001b[0m     \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mmouseInfo\u001b[39m():\n\u001b[1;32m    249\u001b[0m \u001b[38;5;250m        \u001b[39m\u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m    250\u001b[0m \u001b[38;5;124;03m        Launches the MouseInfo app. This application provides mouse coordinate information which can be useful when\u001b[39;00m\n\u001b[1;32m    251\u001b[0m \u001b[38;5;124;03m        planning GUI automation tasks. This function blocks until the application is closed.\u001b[39;00m\n\u001b[1;32m    252\u001b[0m \u001b[38;5;124;03m        \"\"\"\u001b[39;00m\n",
      "File \u001b[0;32m~/external-libraries/lib/python3.10/site-packages/mouseinfo/__init__.py:223\u001b[0m\n\u001b[1;32m    220\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m    221\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m\n\u001b[0;32m--> 223\u001b[0m _display \u001b[38;5;241m=\u001b[39m Display(\u001b[43mos\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43menviron\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mDISPLAY\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m]\u001b[49m)\n\u001b[1;32m    225\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21m_linuxPosition\u001b[39m():\n\u001b[1;32m    226\u001b[0m     coord \u001b[38;5;241m=\u001b[39m _display\u001b[38;5;241m.\u001b[39mscreen()\u001b[38;5;241m.\u001b[39mroot\u001b[38;5;241m.\u001b[39mquery_pointer()\u001b[38;5;241m.\u001b[39m_data\n",
      "File \u001b[0;32m/opt/conda/envs/python35-paddle120-env/lib/python3.10/os.py:680\u001b[0m, in \u001b[0;36m_Environ.__getitem__\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m    677\u001b[0m     value \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_data[\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mencodekey(key)]\n\u001b[1;32m    678\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m:\n\u001b[1;32m    679\u001b[0m     \u001b[38;5;66;03m# raise KeyError with the original key value\u001b[39;00m\n\u001b[0;32m--> 680\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m(key) \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m    681\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mdecodevalue(value)\n",
      "\u001b[0;31mKeyError\u001b[0m: 'DISPLAY'"
     ]
    }
   ],
   "source": [
    "import cv2\r\n",
    "import mediapipe as mp\r\n",
    "import math\r\n",
    "import pyautogui\r\n",
    "\r\n",
    "# 关闭pyautogui安全边界限制\r\n",
    "pyautogui.FAILSAFE = False\r\n",
    "\r\n",
    "# 初始化MediaPipe手部检测\r\n",
    "mp_hands = mp.solutions.hands\r\n",
    "mp_draw = mp.solutions.drawing_utils\r\n",
    "\r\n",
    "# 手部检测参数\r\n",
    "hands = mp_hands.Hands(\r\n",
    "    static_image_mode=False,\r\n",
    "    max_num_hands=1,\r\n",
    "    min_detection_confidence=0.5,\r\n",
    "    min_tracking_confidence=0.5\r\n",
    ")\r\n",
    "\r\n",
    "# 获取屏幕分辨率\r\n",
    "screen_w, screen_h = pyautogui.size()\r\n",
    "\r\n",
    "# 计算两点欧氏距离\r\n",
    "def get_distance(p1, p2):\r\n",
    "    return math.hypot(p1.x - p2.x, p1.y - p2.y)\r\n",
    "\r\n",
    "# 打开摄像头\r\n",
    "cap = cv2.VideoCapture(0)\r\n",
    "print(\"程序启动，做出手势控制鼠标，按 Q 退出\")\r\n",
    "\r\n",
    "while cap.isOpened():\r\n",
    "    ret, frame = cap.read()\r\n",
    "    if not ret:\r\n",
    "        break\r\n",
    "\r\n",
    "    # 画面镜像翻转，符合视觉习惯\r\n",
    "    frame = cv2.flip(frame, 1)\r\n",
    "    h, w, _ = frame.shape\r\n",
    "    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)\r\n",
    "    results = hands.process(img_rgb)\r\n",
    "\r\n",
    "    if results.multi_hand_landmarks:\r\n",
    "        for hand_landmarks in results.multi_hand_landmarks:\r\n",
    "            # 绘制手部关键点和连线\r\n",
    "            mp_draw.draw_landmarks(\r\n",
    "                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,\r\n",
    "                mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=3),\r\n",
    "                mp_draw.DrawingSpec(color=(255, 0, 0), thickness=2)\r\n",
    "            )\r\n",
    "\r\n",
    "            lms = hand_landmarks.landmark\r\n",
    "            # 食指指尖坐标映射到屏幕，移动鼠标\r\n",
    "            mouse_x = lms[8].x * screen_w\r\n",
    "            mouse_y = lms[8].y * screen_h\r\n",
    "            pyautogui.moveTo(mouse_x, mouse_y)\r\n",
    "\r\n",
    "            # 拇指 & 食指距离\r\n",
    "            thumb_index_dist = get_distance(lms[4], lms[8])\r\n",
    "            # 其余四指指尖到掌根距离（判断握拳）\r\n",
    "            fist_dist = all(get_distance(lms[i], lms[0]) < 0.17 for i in [8, 12, 16, 20])\r\n",
    "\r\n",
    "            # 拇食相触 = 左键单击\r\n",
    "            if thumb_index_dist < 0.07:\r\n",
    "                pyautogui.click()\r\n",
    "            # 握拳 = 右键单击\r\n",
    "            if fist_dist:\r\n",
    "                pyautogui.rightClick()\r\n",
    "\r\n",
    "    cv2.imshow(\"手势控制鼠标\", frame)\r\n",
    "    # 按下Q键退出\r\n",
    "    if cv2.waitKey(1) & 0xFF == ord('q'):\r\n",
    "        break\r\n",
    "\r\n",
    "# 释放资源\r\n",
    "cap.release()\r\n",
    "cv2.destroyAllWindows()\r\n",
    "print(\"程序已退出\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "569d36d1-894e-4251-9a27-828844851c31",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "py35-paddle1.2.0"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
