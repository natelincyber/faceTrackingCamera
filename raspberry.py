import socket
from servoControl import servoController

HOST = '192.168.0.109'
PORT = 12345       

''' TODO: recieve data from PC and use servocontroller to move servos'''


def server(conn,addr):
    '''
    runner = servoController(17, 'someServo')
    runner.calibrate()'''
    with conn:
        print('Connected to', addr)
        while True:
            
            data = conn.recv(2048).decode()
            
            if not data: # prevents null values from being printed on screen
                continue
                
            if data == 'close':
                print('closing remote connection')
                conn.close()
                break
                
            if data == 'stop':
                print('closing remote connection')
                conn.close()
                return True

            print(data)
            #runner.move(int(data))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print("server started, waiting for connections")


while True:
    conn, addr = s.accept()
    stop = server(conn,addr)
    if stop:
        print('stopping server')
        break 


