import numpy as np
import cv2 as cv
im = cv.imread('../res/contour5.png')

if (type(im) is np.ndarray) == False : print('file read error');exit()

imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cnt1 = contours[0]
cv.drawContours(im,[cnt1],0,(0,0,255),thickness=3)

_hr1 = hierarchy[0,0]

print("next ",_hr1[0])
print("prev ",_hr1[1])
print("first child ",_hr1[2])
print("parent ",_hr1[3])

print(len(contours))



# cv.imshow('temp',im)
# cv.waitKey(0)
# cv.destroyAllWindows()