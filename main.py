import pyautogui
import time


message = 5
while message > 0:
    time.sleep(4)
    pyautogui.typewrite("who are you?")
    time.sleep(4)
    pyautogui.press("enter")
    message = message - 1
