import socket

my_sock = socket.socket()
my_sock.bind(("0.0.0.0",4444))
my_sock.listen(1)

con, adr = my_sock.accept()

my_sock.close()