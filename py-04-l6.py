import os, datetime



while True:
    print("Jestes w katalogu " + os.getcwd())
    directory = input("Podaj folder albo wpisz exit aby wyjsc z programu: ").strip()
    if directory.lower() == "exit":
        break
    else:

        if directory in os.listdir(os.getcwd()):
           pass
        else:
            os.mkdir(directory)
        os.chdir(directory)
        print("Teraz znajdujemy sie w katalogu " + os.getcwd())

    filename = input("Podaj nazwe pliku: ")
    with open(os.getcwd() + "/" + filename, 'w') as file:
        file.write(str(datetime.datetime.now()))
        print("Plik zapisano jako: " + filename)
        os.chdir("..")