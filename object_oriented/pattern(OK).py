import cv2
import numpy as np 
path = '/home/hassan/Desktop/photo1.jpg'
path1 = '/home/hassan/Desktop/temple1.jpg'
#path3 = '/home/hassan/Desktop/pelak3.jpg'
img = cv2.imread(path,0)
cv2.imshow('img',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('img_gray',img_gary)
img_temple = cv2.imread(path1,0)
#img_temple3 = cv2.imread(path3,0)
cv2.imshow('img_temple',img_temple)
w,h = img_temple.shape[::-1]
#w,h = img_temple3.shape[::-1]
res = cv2.matchTemplate(img,img_temple,cv2.TM_CCOEFF_NORMED)
#res = cv2.matchTemplate(img,img_temple3,cv2.TM_CCOEFF_NORMED)
cv2.imshow('res',res)
threshold = 0.99
location = np.where(res >= threshold)
for pt in zip(*location[::-1]):
    cv2.rectangle(img,pt,(pt[0] + w, pt[1] + h),(255,255,255),1.5)
cv2.imshow('pelak',img)

              
cv2.waitKey(0)
cv2.destroyAllWindows()
