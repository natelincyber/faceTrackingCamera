from ipwebcam import IPWEBCAM
import cv2

ipcam = IPWEBCAM('192.168.0.180:8080')
capturePort = cv2.VideoCapture('http://192.168.0.180:8080/video')
zoom = 0
print("done")
while (True):
	ret, frame = capturePort.read()
	cv2.imshow('video', frame)
	
