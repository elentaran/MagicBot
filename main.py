import pyautogui as pa
import time
import cv2
from PIL import ImageGrab as ig
import numpy as np

img_combat_file = "images/combat.png"
img_solo_file = "images/solo.png"
img_arrow_file = "images/arrow.png"
region_default = (0,0,1900,1000)
region_menu = (100,100,600,1000)
neutral_point = (800,400)
min_val_reco = 0.2

def take_screen(region=region_default):
    screen = ig.grab(bbox=region)
    screen_np = np.array(screen)
    screen_np_cvt = cv2.cvtColor(screen_np,cv2.COLOR_RGB2BGR)    
    return screen_np_cvt

def locate_ctr_img(img,screen, region=region_default):
    res = cv2.matchTemplate(screen,img, cv2.TM_SQDIFF_NORMED)
    minv, maxv, minl, maxl = cv2.minMaxLoc(res)
    print(minv)
    if minv > min_val_reco:
        return None
    topleft=minl
    h,w = img.shape[0:2]
    return (topleft[0] + (w//2)+region[0], topleft[1] + (h//2)+region[1])

def mo_click():
    pa.mouseDown()
    time.sleep(0.1)
    pa.mouseUp()

    
def select(img, region=region_default):
    screen = take_screen(region)
    pos = locate_ctr_img(img, screen, region)
    pa.moveTo(pos)
    mo_click()
    pa.moveTo(neutral_point)
    time.sleep(0.5)


#A = cv2.imread(img_combat)
testimg = cv2.imread("images/test.png")
img_combat = cv2.imread(img_combat_file)
img_solo = cv2.imread(img_solo_file)
img_arrow = cv2.imread(img_arrow_file)

select(img_combat, region_menu)
select(img_solo, region_menu)
select(img_arrow)

#center = locate_ctr_img(testimg, a_np)
#cv2.circle(a_np,center,5,(0,0,255),-1)
#print(center)
#cv2.namedWindow("test")
#cv2.imshow("test",a_np)
#cv2.waitKey(0)


quit()

pa.moveTo(neutral_point)
mo_click()

# select_menu(img_combat)
# select_menu(img_solo)
select(img_arrow)
