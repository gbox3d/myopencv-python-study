import numpy as np
import cv2 as cv
im = cv.imread('../res/contour1.png')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# print( len(contours))

cnt = contours[0]
_mmt = cv.moments(cnt)
# print ("moment :" , _mmt)
cx = _mmt["m10"]/_mmt["m00"]
cy = _mmt["m01"]/_mmt["m00"]
print(f'cx : {cx},cy: {cy}')

print("area : " , cv.contourArea(cnt))
print("arcLength : " , cv.arcLength(cnt,True))

# cv.drawContours(im,[cnt],0,(0,255,255),3)

# for _contour in contours : print(cv.contourArea(_contour))

_contours = [_contour  for _contour in contours if cv.contourArea(_contour) > 1000 ]

print(len(_contours))

font = cv.FONT_HERSHEY_SIMPLEX
for _cnt in _contours : 
    cv.drawContours(im,[_cnt],0,(0,0,255),3)
    _mmt = cv.moments(_cnt)
    cx = int(_mmt["m10"]/_mmt["m00"])
    cy = int(_mmt["m01"]/_mmt["m00"])
    cv.circle(im,(cx,cy),8,(255,0,0),-1)
    cv.putText(im,f'{cx},{cy}',(cx,cy), font,0.5 ,(0,255,0),2,cv.LINE_AA)



if cv.imwrite('../output/contours2.png',im) == True : print('save ok')
