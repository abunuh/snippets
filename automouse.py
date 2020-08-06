#!/home/ebrahim/anaconda3/bin/python3


import pyautogui
import time
#import keyboard

while True:
    try:
        time.sleep(25)
        pyautogui.moveRel(100, 100, duration=1)
        time.sleep(60)
        pyautogui.moveRel(-100, -100, duration=1)
        time.sleep(60)
    except KeyboardInterrupt:
        print("Exiting")
        break



