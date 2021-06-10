import socket, os, sys, cv2, time, keyboard
from ipwebcam import IPWEBCAM
from _thread import *

# servo without sticker - 15-180 degrees of rotation

HOST = '192.168.0.109'  # The server's hostname or IP address
PORT = 12345            # The port used by the server


os.system('cls' if os.name == 'nt' else 'clear')

# connect to remote camera and get live video stream
cameraIPAddress = '192.168.0.180:8080'
print("connecting to remote camera")
capturePort = cv2.VideoCapture(f'http://{cameraIPAddress}/video')
print(f"connected to: {cameraIPAddress}")


# load data for face detection model
faceCascade = cv2.CascadeClassifier('faceData/haarcascade_frontalface_default.xml')

# connect to raspberry pi for remote data transfer
try:
    print('connecting to raspberry pi remote server...')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print('connected to remote server')
except socket.error:
    input('unable to connect to remote server. press enter to exit')
    sys.exit()

# set resolution for remote camera
ipcam = IPWEBCAM(cameraIPAddress)
resolution = input("set resolution (0-8): ")
ipcam.set_resolution(resolution)

if resolution == 0:
    s.sendall('res0')
elif resolution == 1:
    s.sendall('res1')
else:
    width = ipcam.resolutions[resolution][0:3]
    height = ipcam.resolutions[resolution][4:]

s.sendall(str.encode('res' + width + height))


def imageHandler(x, y): # handles remote data transfer
    s.sendall(str.encode(str(int(x)) + ' ' + str(int(y))))


while(True):
    ret, frame = capturePort.read()

    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(20,20))
    except cv2.error as e:
        s.sendall(str.encode('close'))
        input("connection to ipcam lost. press enter to exit")
        sys.exit()


    for x, y, w, h, in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        start_new_thread(imageHandler, (x, y))

    if keyboard.is_pressed('q'):
        print('stopping server and closing the program...')
        s.sendall(str.encode('stop'))
        break

    cv2.imshow('video', frame)

    if cv2.waitKey(1)  == 27:
        s.sendall(str.encode('close'))
        break
    
        

capturePort.release()
cv2.destroyAllWindows()
