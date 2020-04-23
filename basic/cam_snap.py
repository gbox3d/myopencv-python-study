import cv2 as cv 


cap = cv.VideoCapture(0)
ret,frame = cap.read()
print(ret)

cv.imwrite('test.png',frame)