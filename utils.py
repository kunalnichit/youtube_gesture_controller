import pygetwindow as gw
import win32gui
import win32con
import time

def set_opencv_window_always_on_top(window_title='AirPointer'):
    try:
        win = gw.getWindowsWithTitle(window_title)[0]
        hwnd = win._hWnd
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 100, 100, 640, 480, 0)
    except IndexError:
        print("⚠️ Could not find OpenCV window.")

def focus_youtube_tab():
    try:
        for title in ["YouTube", "Chrome", "Edge", "Firefox"]:
            windows = gw.getWindowsWithTitle(title)
            if windows:
                win = windows[0]
                win.activate()
                time.sleep(0.2)
                return True
    except Exception as e:
        print(f"Window focus failed: {e}")
    return False