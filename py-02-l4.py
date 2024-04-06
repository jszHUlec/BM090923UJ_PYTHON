"""
Napisz program, ktory przyjmuje od uzytkownika nazwe portu
np: FTP. Program wyswietli numer portu na ktorym powinien nasluchiwac
FTP -> 21
"""

# FTP, SSH, HTTP, HPPS
# stworz slownik {"ftp":21,...}
# pobeirz wartosc od uzytkownika (input)
# pobrana wartosc sprawdz w slowniku
#  slownik[odUzytkownika]

servicesAndPorts = {"FTP": 21, "SSH": 22, "HTTP": 80, "HTTPS": 443}

setService = input("Enter the service: ").upper().strip()
# port = setService
print(servicesAndPorts[setService])