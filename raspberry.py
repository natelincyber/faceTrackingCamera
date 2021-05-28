import socket

HOST = '127.0.0.1' 
PORT = 65432       

''' TODO: recieve data from PC and use servocontroller to move servos'''

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(2048).decode()
            if not data:
                break
            print(data)
            # for debugging?
            conn.send(str.encode(data))