import cv2
import numpy as np
from ipwebcam import IPWEBCAM


cameraIPAddress = '192.168.0.180:8080'


capturePort = cv2.VideoCapture(f'http://{cameraIPAddress}/video')

default = 'haarcascade_frontalface_default.xml'
faceProfile = 'haarcascade_profileface.xml'
faceCascade = cv2.CascadeClassifier(default)

while(True):
	ret, frame = capturePort.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(20,20))

	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]

	cv2.imshow('video', frame)

	if cv2.waitKey(1)  == 27:
    		break

capturePort.release()
cv2.destroyAllWindows()

