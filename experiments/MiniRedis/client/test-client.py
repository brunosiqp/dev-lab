import socket

HOST = "127.0.0.1"
PORT = 6379

while True:

    cmd = input("mini-redis> ")

    s = socket.socket()
    s.connect((HOST, PORT))

    s.send(cmd.encode())

    data = s.recv(1024)

    print(data.decode())

    s.close()