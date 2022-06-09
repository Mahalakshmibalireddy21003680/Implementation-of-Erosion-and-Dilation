# Implementation-of-Erosion-and-Dilation
## Aim
To implement Erosion and Dilation using Python and OpenCV.
## Software Required
1. Anaconda - Python 3.7
2. OpenCV
## Algorithm:
### Step1:
Import the necessary packages to do Erosion and Dilution.

### Step2:
Create the text image of our name using putText from cv2 package.

### Step3:
Create the required structural element.

### Step4:
Apply Erode and Dilution for our NameImage.

### Step5:
Display the output images.

### Step6:
End the program.
 
## Program:

``` Python
Developed by: B. Mahalakshmi
Register Number: 212221240008
# Import the necessary packages
import cv2
import numpy as np

# Create the Text using cv2.putText
img1 = np.zeros((100,1000),dtype='uint8')
font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(img1,'Pavan',(5,50),font,2,(255),3,cv2.LINE_AA)
cv2.imshow('My Image',img1)

# Create the structuring element
kernel1=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))

# Erode the image
erodeimg=cv2.erode(img1,kernel1)
cv2.imshow("Eroded Image",erodeimg)

# Dilate the image
dilateimg=cv2.dilate(img1,kernel1)
cv2.imshow("Dilated Image",dilateimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

```
## Output:

### Display the input Image
![10 1](https://user-images.githubusercontent.com/93427286/172933505-929055ab-6304-4c06-a767-b953b408adcd.png)

### Display the Eroded Image
![10 2](https://user-images.githubusercontent.com/93427286/172933503-7569c857-9c55-4d80-b5f8-4625bd0a694b.png)

### Display the Dilated Image
![10 2](https://user-images.githubusercontent.com/93427286/172933503-7569c857-9c55-4d80-b5f8-4625bd0a694b.png)

## Result
Thus the generated text image is eroded and dilated using python and OpenCV.
