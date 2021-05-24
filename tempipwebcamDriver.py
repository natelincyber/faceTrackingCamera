# a simple test program to test functionality between
# modified ipwebcam library and openCV videoport
import cv2
import sys
import os
import keyboard
from ipwebcam import IPWEBCAM

print("loading...")
cameraIPAddress = '192.168.0.180:8080'

ipcam = IPWEBCAM(cameraIPAddress)
capturePort = cv2.VideoCapture(f'http://{cameraIPAddress}/video')
os.system('cls' if os.name == 'nt' else 'clear')
print(f"connected to: {cameraIPAddress}")

while(True):
	ret, frame = capturePort.read()

	if keyboard.is_pressed('q'):
    		ipcam.swap_camera("on")

	if keyboard.is_pressed('w'):
    		ipcam.swap_camera("off")
	if keyboard.is_pressed('z'):
    		ipcam.zoom(20)

	cv2.imshow('video', frame)

	if cv2.waitKey(1)  == 27:
    		break

capturePort.release()
cv2.destroyAllWindows()
