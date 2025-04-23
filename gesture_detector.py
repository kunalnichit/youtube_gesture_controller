def fingers_up(landmarks):
    fingers = []
    fingers.append(landmarks[4].x < landmarks[3].x)
    fingers.extend([landmarks[i].y < landmarks[i - 2].y for i in [8, 12, 16, 20]])
    return fingers

def detect_gesture(landmarks):
    fingers = fingers_up(landmarks)

    if all(fingers):
        return "playpause"
    elif not any(fingers):
        return "playpause"
    elif fingers == [False, True, True, False, False]:
        return "volumeup"
    elif fingers == [False, False, False, True, True]:
        return "volumedown"
    elif fingers == [False, False, False, False, True]:
        return "next"
    elif fingers == [True, True, True, True, False]:
        return "previous"
    return None