import socket

new_socket = socket.socket()
new_socket.connect(("127.0.0.1",4322))
print("connection established....")

while True:
    fromServer = new_socket.recv(2048).decode()
    print(fromServer)

    if fromServer.strip().upper() == "EXIT":
        print("server przerwal polaczenie")
        new_socket.close()
        break

    toServer = input("widomosc do Serwera:")
    new_socket.send(toServer.encode())
    if toServer.strip().upper() == "EXIT":
        new_socket.close()
        print("koncze program")
        break

new_socket.close()