import socket

HOST = "127.0.0.1"
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Hello world!".encode("utf-8"))
socket.send("\nWhat else can I send?".encode("utf-8"))
print(socket.recv(1024).decode("utf-8"))
