# -*- coding: utf-8 -*-
"""
Created on Thursday Jun 14 20:32:45 2018

@author: Amitrajit Bose
"""

import numpy as np
import cv2
x=input("Enter Filename With Extension: ")
filenames=[x]
for filename in filenames:
    im=cv2.imread(filename)
    imgray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(imgray,127,255,0) #green color
    im2,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #thresholded image
    cv2.drawContours(im,contours,-1,(0,255,0),5)
    #cv2.imshow("Border Image",im)
    #cv2.waitKey(0)
    cv2.imwrite('NEW'+filename,imgray)

