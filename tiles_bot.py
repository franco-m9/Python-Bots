from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# Black RGB Value = (0, 0, 0)
# Tile 1 Position : X = 1109 | Y = 848
# Tile 2 Position : X = 1218 | Y = 848
# Tile 3 Position : X = 1321 | Y = 848
# Tile 4 Position : X = 1426 | Y = 848


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(1109, 848)[0] == 0:
        click(1109, 848)
    if pyautogui.pixel(1218, 848)[0] == 0:
        click(1218, 848)
    if pyautogui.pixel(1321, 848)[0] == 0:
        click(1321, 848)
    if pyautogui.pixel(1426, 848)[0] == 0:
        click(1426, 848)
