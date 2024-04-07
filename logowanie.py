severity = ["ERROR","FATAL",'WARNING']
with open("log.txt") as file:
    for linijka in file.readlines():
        x = linijka.split(" ")
        if x[2] in severity:
            print(linijka)
            print(x[0],x[1],x[3:6])