import numpy as np
import cv2 as cv

img = np.zeros((512,512,3),np.uint8)

cv.line(img,(0,0),(500,500),(255,0,0),5)


cv.imwrite('test.png',img)

print("save ok..")
