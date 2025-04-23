# AirPointer: Real-Time YouTube Gesture Controller
AirPointer is a real-time YouTube Gesture Controller built using Python. It allows users to control YouTube video playback with simple hand gestures detected via webcam, without the need for a keyboard or mouse.

---
## 🎯 Features
- Real-time hand tracking using MediaPipe
- Simulated keypress control with PyAutoGUI
- Visual gesture feedback via OpenCV overlay
- Cooldown mechanism to avoid gesture repetition
- Modular, extendable Python codebase
---
## 🧰 Technology Stack
- **OpenCV** - Webcam input and visualization
- **MediaPipe** - Hand landmark detection
- **PyAutoGUI** - Simulate keyboard inputs
- **pygetwindow & win32gui** - Manage window focus and z-order
- **Python** - Core language
---
## ✋ Gesture Controls
| Gesture                        | Action           |
|--------------------------------|------------------|
| Open palm                      | Play / Pause     |
| Fist (no fingers up)           | Play / Pause     |
| Two fingers (index + middle)   | Volume Up        |
| Ring + pinky fingers           | Volume Down      |
| Pinky only                     | Fast Forward Video    |
| All fingers except pinky       | Fast Backward Video   |

---

## 📁 Project Structure
```
AirPointer_Modular/
├── main.py                 # Entry point, integrates all modules
├── hand_tracking.py        # MediaPipe hand tracker class
├── gesture_detector.py     # Logic to detect gestures from landmarks
├── gesture_controller.py   # Maps gestures to PyAutoGUI actions
├── utils.py                # Helper functions (e.g., window focus)
├── requirements.txt        # All required python packages
```
---

## 🚀 How to Run
### Prerequisites
- Python 3.7+
- Install dependencies from requirements.txt:
```bash
pip install opencv-python mediapipe pyautogui pygetwindow pywin32
```

### Run the App
```bash
python main.py
```

> 🧠 Ensure your browser is open with YouTube active before running for best results.

---

## 🔧 Customization

You can map gestures to different `pyautogui.press()` keys inside `gesture_controller.py`. For example:
```python
pyautogui.press('f')  # Fullscreen
pyautogui.press('ctrl')  # Control key
```

---
## 💡 Future Ideas
- Add voice + gesture fusion
- Gesture training for custom actions
- Cross-platform support for macOS/Linux
---

## 🧑‍💻 Author
Made with ❤️Chat-gpt by Sparty(kunal_nichit) — a part of the *AirPointer* initiative for intuitive and contactless interaction systems.

---

## 📜 License
This project is open-source and free to use under the MIT License.
