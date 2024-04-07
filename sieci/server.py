import socket
my_sock = socket.socket()
my_sock.bind(("0.0.0.0",4444))
my_sock.listen(1)

con, adr = my_sock.accept()
data = con.recv(2048).decode("UTF-8")

con.send("Widomosc z Serwera".encode())

print(data)

my_sock.close()
input("wcisnij enter")