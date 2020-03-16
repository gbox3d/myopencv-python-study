import numpy as np
import cv2 as cv
im = cv.imread('../res/contour5.png')

if type(im) is np.ndarray == False : print('file read error');exit()

imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

print(len(contours))

# cv.imshow('temp',im)
# cv.waitKey(0)
# cv.destroyAllWindows()