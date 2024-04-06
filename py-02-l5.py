""" zabawa ze strukturami danych
"""

lista = {}

lista.append("MAZOWIECKIE") # dodajmy slwonik {"Warszawa":["syrenka", "zamek","wisla"]}
lista.append("POMORSKIE") # dodajmy {"Gdansk":["neptun","westerplatte","muzeum"]}
lista.append({"Warszawa":"", "Gdansk":""})
lista[2]["Warszawa"] = ["syrenka", "zamek","wisla"]
lista[2]["Gdansk"] = ["neptun","westerplatte","muzeum"]
lista[2]["Krakow"] = ["wawel","smok"]
lista.append("MALOPOLSKA")
print("lista cala:", lista)
del lista[2]
print("lista bez slownika", lista)