# a simple test program to test functionality between
# modified ipwebcam library and openCV
import cv2
import os
import sys
import keyboard
from ipwebcam import IPWEBCAM

os.system('cls' if os.name == 'nt' else 'clear')
print("loading...")
cameraIPAddress = '192.168.0.180:8080'

ipcam = IPWEBCAM(cameraIPAddress)

capturePort = cv2.VideoCapture(f'http://{cameraIPAddress}/video')


print(f"connected to: {cameraIPAddress}")

targetZoom = int(input('zoom: '))


faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
ipcam.zoom(0)

while(True):
	ret, frame = capturePort.read()

	# sample test cases
	if keyboard.is_pressed('q'):
    		ipcam.swap_camera("on")

	if keyboard.is_pressed('w'):
    		ipcam.swap_camera("off")
	if keyboard.is_pressed('z'):
    		ipcam.zoom(0)

	# face detection
	try:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = faceCascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(20,20))
	except cv2.error as e:
			input("connection lost! press enter to exit")
			sys.exit()

	for (x, y, w, h) in faces:
		
		cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]


		if w*h < targetZoom:
    		
			diff = targetZoom - w*h
			zoomIn = diff//330
			if targetZoom - w*h <= 1500:
				continue
			else:
				ipcam.zoom(zoomIn + 9)
				print(f'{zoomIn * 330} {(zoomIn * 330) + (w*h)}')


	cv2.imshow('video', frame)

	if cv2.waitKey(1)  == 27:
    		break

capturePort.release()
cv2.destroyAllWindows()
