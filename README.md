# 🖱️ Virtual Mouse with Hand Tracking

A Python-based virtual mouse system that lets you control your mouse cursor and click actions using only hand gestures captured through a webcam. This project utilizes **OpenCV**, **Mediapipe**, and **Autopy** to detect hand landmarks and translate gestures into cursor movement and mouse clicks.

---

## 🚀 Features

- Move cursor using index finger  
- Left-click by pinching index and middle fingers  
- Right-click with an open palm  
- Smooth cursor movement with coordinate interpolation  
- Real-time hand tracking with bounding box and visual feedback  

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/gautham0914/virtual_mouse.git
cd virtual-mouse
```

### 2. Create a Virtual Environment (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Make sure you have Python 3.7+ installed.

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not provided, install manually:

```bash
pip install opencv-python mediapipe numpy cvzone autopy pynput
```

> **Note**: `autopy` may require additional build tools depending on your system.

---

## 🧠 How It Works

### 📁 Files Overview

- `HandTrackingModule.py`: Custom module for detecting hands and fingers using MediaPipe.  
- `virtual_mouse.py`: Main script that connects webcam input to mouse control based on hand gestures.  
- `README.md`: Project instructions and documentation.

### ✋ Gesture Controls

| Gesture                        | Action             |
|-------------------------------|--------------------|
| Index finger up               | Move cursor        |
| Index + middle fingers up     | Left-click (pinch) |
| All fingers up                | Right-click        |

---

## 📷 Demo

> You can record or upload a demo here if you plan to publish on GitHub.

---

## ❗ Troubleshooting

- If `autopy` fails to install, try:
  - `pip install pyautogui` as an alternative for mouse control (with code changes).
- Ensure your webcam has permission and is not used by another application.
- Run the script from your terminal to see errors/logs in real-time.

---

## 🧑‍💻 Credits

Built with 💻 by Gautham using OpenCV, MediaPipe, and Autopy.

---

## 📜 License

This project is licensed under the MIT License. Feel free to use, share, and modify with credit.
