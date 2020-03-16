import numpy as np
import cv2 as cv

img = cv.imread('../res/messi5.jpg')

px = img[100,100]
print(px)

#read pixel
print(px[0])
print(px[1])
print(px[2])


print("--------------------")

print(img[100,100,0])
print(img[100,100,1])
print(img[100,100,2])

print("--------------------")
# get image info
print(img.shape)
print(img.size)
print(img.dtype)

#write pixel

for x in range(100) :
    for y in range(50) :
        img[100 + y,100+x] = [0,0,255]

#save result
cv.imwrite('../output/test.png',img)



