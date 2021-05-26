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
ipcam.zoom(0)
capturePort = cv2.VideoCapture(f'http://{cameraIPAddress}/video')


print(f"connected to: {cameraIPAddress}")


faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


while(True):
	ret, frame = capturePort.read()

	# sample test cases
	if keyboard.is_pressed('q'):
    		ipcam.swap_camera("on")

	if keyboard.is_pressed('w'):
    		ipcam.swap_camera("off")
	if keyboard.is_pressed('z'):
    		ipcam.zoom(20)

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

		targetZoom = 9000

		if w*h < targetZoom:
			print(w*h)
    		
			diff = targetZoom - w*h
			zoom = diff//330
			if targetZoom - w*h <= 1500:
				print(w*h)
				continue
			else:
				ipcam.zoom(zoom)


	cv2.imshow('video', frame)

	if cv2.waitKey(1)  == 27:
    		break

capturePort.release()
cv2.destroyAllWindows()
