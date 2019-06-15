# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 15:08:42 2019

@author: Tamer
"""

import cv2

# Use CascadeClassifier function to load xml file.
face_classifier = cv2.CascadeClassifier('files/haarcascade_frontalface_alt.xml')
eye_classifier = cv2.CascadeClassifier('files/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # scaleFactor: When image is enlarged to be more detectable the scale should also be increased.
    # this value minNeighbors: By increasing this number you can eliminate false positive but when increasing 
    # you should be careful because you may lose true positives too 
    face = face_classifier.detectMultiScale(frame, scaleFactor = 1.1, minNeighbors = 3)
    eye = eye_classifier.detectMultiScale(frame, scaleFactor = 1.1, minNeighbors = 5)
    
    for (x,y,w,h) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 3)
        for (x1,y1,w1,h1) in eye:
            cv2.rectangle(frame, (x1, y1), (x1+w1, y1+h1), (0,255,0), 3)
        
    cv2.imshow('Face Detector', frame)
    exit = cv2.waitKey(1)
    if exit == 27:
        break
    
cap.release()
cv2.destroyAllWindows()