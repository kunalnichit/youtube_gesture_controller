from hand_tracking import HandTracker
from gesture_detector import detect_gesture
from gesture_controller import perform_action
from utils import set_opencv_window_always_on_top

import cv2
import time

cap = cv2.VideoCapture(0)
cv2.namedWindow("AirPointer", cv2.WINDOW_NORMAL)
cv2.resizeWindow("AirPointer", 640, 480)

tracker = HandTracker()
last_gesture_time = 0
cooldown_seconds = 1.5
first_frame = True

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    landmarks, results = tracker.process_frame(frame)

    gesture = ""
    now = time.time()

    if landmarks and now - last_gesture_time > cooldown_seconds:
        gesture = detect_gesture(landmarks)
        if gesture:
            perform_action(gesture)
            last_gesture_time = now

    if gesture:
        cv2.putText(frame, f"Gesture: {gesture}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("AirPointer", frame)

    if first_frame:
        set_opencv_window_always_on_top("AirPointer")
        first_frame = False

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()