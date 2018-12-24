import numpy as np
import cv2 as cv

drag = False
mode = "circle"
ix,iy = -1,-1

def draw_function (event,x,y,flags,param) :
    global ix,iy,drag,mode
 
    if event == cv.EVENT_LBUTTONDOWN :
        drag = True
        ix,iy=x,y
    
    elif event == cv.EVENT_MOUSEMOVE:
        if drag == True:
            if mode == "circle" :
                cv.circle(img,(x,y),5,(0,0,,255),-1)
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0)-1)
            else:
                
