import pyautogui as pa
import time
import cv2

img_combat = "images/combat.png"
img_solo = "images/solo.png"
img_arrow = "images/arrow.png"
region_menu = (100,100,600,1000)
neutral_point = (800,400)

def mo_click():
    pa.mouseDown()
    time.sleep(0.1)
    pa.mouseUp()

    
def select_menu(img):
    pos = pa.locateCenterOnScreen(img, region=region_menu )
    print(pos)
    pa.moveTo(pos)
    mo_click()
    pa.moveTo(neutral_point)
    time.sleep(0.5)

def select(img):
    pos = pa.locateCenterOnScreen(img, grayscale=True)
    print(pos)
    pa.moveTo(pos)
    mo_click()



pa.moveTo(neutral_point)
mo_click()

# select_menu(img_combat)
# select_menu(img_solo)
select(img_arrow)
