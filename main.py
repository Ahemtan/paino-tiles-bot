from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con

# https://www.agame.com/game/magic-piano-tiles for reference game 
pyautogui.displayMousePosition()


# this function is use to get mouse position
# and color value of pixel
# uncomment below line to get mouse position and note
# the x and y position while hovering over tiles of paino tile game

# custom click function for faster speed
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    # put x and y co-ordinates in place of 581, 400
    # for each if statement check the 

    if pyautogui.pixel(361, 400)[0] == 0:
        click(581, 400)
    if pyautogui.pixel(423, 400)[0] == 0:
        click(682, 400)
    if pyautogui.pixel(570, 400)[0] == 0:
        click(770, 400)
    if pyautogui.pixel(689, 400)[0] == 0:
        click(869, 400)