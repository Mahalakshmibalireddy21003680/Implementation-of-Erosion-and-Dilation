import cv2
import numpy as np
img1 = np.zeros((100,1000),dtype='uint8')
font=cv2.FONT_HERSHEY_COMPLEX_SMALL
cv2.putText(img1,'MahaLakshmi',(5,50),font,2,(255),3,cv2.LINE_AA)
cv2.imshow('My Image',img1)
kernel1=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
erodeimg=cv2.erode(img1,kernel1)
cv2.imshow("Eroded Image",erodeimg)
dilateimg=cv2.dilate(img1,kernel1)
cv2.imshow("Dilated Image",dilateimg)
cv2.waitKey(0)
cv2.destroyAllWindows()