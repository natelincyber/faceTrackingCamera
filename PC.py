import socket, os, sys, cv2


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
global s

os.system('cls' if os.name == 'nt' else 'clear')

# connect to remote camera and get live video stream
cameraIPAddress = '192.168.0.180:8080'
print('connecting to remote camera...')


capturePort = cv2.VideoCapture(f'http://{cameraIPAddress}/video')
print(f"connected to: {cameraIPAddress}")


# load data for face detection model
faceCascade = cv2.CascadeClassifier('faceData/haarcascade_frontalface_default.xml')

# connect to raspberry pi for remote data transfer
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

while(True):
    ret, frame = capturePort.read()

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

    
    '''
    TODO: code out servo calculations
    and sending calculations over to RPi
    if inp == 'stop':
        break
    s.sendall(str.encode(inp))
    '''
    cv2.imshow('video', frame)

    if cv2.waitKey(1)  == 27:
        break

capturePort.release()
cv2.destroyAllWindows()
