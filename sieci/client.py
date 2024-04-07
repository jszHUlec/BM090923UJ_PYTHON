import socket

new_socket = socket.socket()
new_socket.connect(("127.0.0.1",4444))
new_socket.send("Hello world".encode("UTF-8"))
new_socket.send("Nadaje z programu python".encode("UTF-8"))

wiadomosc = new_socket.recv(2048).decode()
print(wiadomosc)

new_socket.close()