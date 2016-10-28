import pyautogui as pa
import time
import cv2
from PIL import ImageGrab as ig
import numpy as np

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

#A = cv2.imread(img_combat)
A = ig.grab()
a_np = np.array(A)
a_np = cv2.cvtColor(a_np,cv2.COLOR_RGB2BGR)

testimg = cv2.imread("images/test.png")
res = cv2.matchTemplate(a_np,testimg, cv2.TM_SQDIFF_NORMED)
minv, maxv, minl, maxl = cv2.minMaxLoc(res)
topleft=minl
w,h = testimg.shape[0:2]
botright=(topleft[0]+w,topleft[1]+h)
cv2.rectangle(a_np,topleft,botright,(0,0,255),2)

print(minv)
cv2.namedWindow("test")
cv2.imshow("test",a_np)
cv2.waitKey(0)


quit()
pa.moveTo(neutral_point)
mo_click()

# select_menu(img_combat)
# select_menu(img_solo)
select(img_arrow)
