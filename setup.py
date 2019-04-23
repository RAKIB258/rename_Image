import os
import cv2

import numpy as np

direc= 'test'
count=1

for img in os.listdir(direc):
	f1=cv2.imread('test/'+img)
	cv2.imwrite("target/"+"%d.jpg" % count, f1)
	count=count+1
