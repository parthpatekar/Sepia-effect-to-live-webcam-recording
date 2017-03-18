"""
# -*- coding: utf-8 -*-

Created on Sun Mar 12 00:15:29 2017

@author: Parth Patekar

"""
import numpy as np
import cv2

#Start capturing from webcam        
cap = cv2.VideoCapture(0)
#Set width of the captured video
cap.set(3,320)
#Set height of the captured video
cap.set(4,240)

#Start a window named 'Frame'
cv2.namedWindow("Frame")

#For each frame
while(True):
    # Capture frame-by-frame
    (ret,frame) = cap.read()
    
#<--------------------------------Our operations on each frame come here---------------------------->
    
    #Get the shape of the frame
    (l,j,k) = frame.shape    
    
    #Flatten the frame matrix to get 1-D array [r0,b0,g0,r1,b1,g1,...,r(l*j*k),b(l*j*k),g(l*j*k)]
    frame=frame.reshape(-1)
    
    #For each set of the colours r(i),g(i),b(i),
    for i in xrange(0,len(frame),3):
        #Temporary assignment
        r=frame.item(i)
        g=frame.item(i+1)
        b=frame.item(i+2)
        
        #This is the formula for getting a sepia. Each new colour depends upon all three previous colours
        R = r * 0.393 + g * 0.769 + b * 0.189   
        G = r * 0.349 + g * 0.686 + b * 0.168
        B = r * 0.272 + g * 0.534 + b * 0.131
  
        #If the new value of the colour is greater than 255, then set the maximum possible value, i.e. 255
        frame.itemset(i+2,255) if R > 255 else frame.itemset(i+2,R)
        frame.itemset(i+1,255) if G > 255 else frame.itemset(i+1,G)
        frame.itemset(i,255) if B > 255 else frame.itemset(i,B)            
        
    #Reshape the matrix to its original form    
    frame=frame.reshape((l,j,k))
    
    #The output window will be as set - 320p x 240p, so we resize it to get a bigger window 
    frame_display = cv2.resize(frame, (j*2, l*2), interpolation=cv2.INTER_CUBIC)
    
    #Display the resulting frame
    cv2.imshow('sepia',frame_display)
    
    #Quit on Esc key
    if cv2.waitKey(1) == 27:
        break
    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()