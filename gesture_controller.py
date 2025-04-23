import pyautogui
from utils import focus_youtube_tab

def perform_action(gesture):
    if gesture == "playpause":
        if focus_youtube_tab():
            pyautogui.press('space')
    elif gesture == "volumeup":
        pyautogui.press('volumeup')
    elif gesture == "volumedown":
        pyautogui.press('volumedown')
    elif gesture == "next":
        if focus_youtube_tab():
            pyautogui.press('right')
    elif gesture == "previous":
        if focus_youtube_tab():
            pyautogui.press('left')