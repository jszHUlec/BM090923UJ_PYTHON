import socket

mysocket = socket.socket()
mysocket.bind(("0.0.0.0",4322))
mysocket.listen(1)
print("waiting for connection...")
con, adr = mysocket.accept()
print(f"client connected - > {adr}")

while True:
    toSent=input("wiadomosc dla clienta:")
    con.send(toSent.encode())

    if toSent.strip().upper() == "EXIT":
        print("polaczenie bedzie zamkniete")
        con.close()
        break

    fromClient = con.recv(2048).decode()
    print(fromClient)
    if fromClient.strip().upper() == "EXIT":
        print("client zakonczyl polaczenie")
        con.close()
        break

mysocket.close()