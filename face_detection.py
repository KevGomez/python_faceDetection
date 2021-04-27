# This project contains of Face detection python algorithm with openCV for image and webcam detection

import cv2
from random import randrange

#using the trained data
trainedFaceData = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#reading the image
# img = cv2.imread('Data/7.jpeg')

# for video
# if is it 0 then it is your webcam, then you can give the directory as well
# VideoCapture('video.mp4')
webCam = cv2.VideoCapture(0)

while True:
    print('Starting the loop')
    # reading the current frame
    success_frame, frame = webCam.read()

    #convertion to grayscale
    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #coordinates of the face in image
    face_coordinates = trainedFaceData.detectMultiScale(grayscale_img)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2)

    #showing the webcam
    cv2.imshow('Face detection', frame)
    key = cv2.waitKey(1)

    # ascii key for Q is 81 and q is 113
    if key==81 or key==113:
        break

webCam.release()

""" For image
#convertion to grayscale
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#coordinates of the face in image
face_coordinates = trainedFaceData.detectMultiScale(grayscale_img)

#drawing the rectangle, with for loop you can detect multiple faces
#(x, y, w, h) = face_coordinates[0]
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2) 
# img
# coordinates
# rectangle color
# thickness of the rectangle

#show the image
cv2.imshow('Face detector', img)
cv2.waitKey()
"""

