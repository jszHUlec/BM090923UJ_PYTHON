import os

adres_ip = input("Podaj adres IPv4: ").strip()
#Linux
if os.system(f"ping -c 2 {adres_ip} > ping.txt") == 0:
    print("maszyna wlaczona")
else:
    print("maszyna wylaczona")