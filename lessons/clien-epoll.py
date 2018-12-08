import socket

sock = socket.create_connection(("127.0.0.1"), 10001)
sock.sendall(b"client1")

