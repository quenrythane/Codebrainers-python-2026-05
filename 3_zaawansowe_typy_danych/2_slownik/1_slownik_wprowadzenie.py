# lista_imion = ["Adam", "Bartek", "Cezary", "Dawid", "Eryk"]

# # slownik = {"klucz" : "wartosc", "klucz" : "wartosc"}
# # slownik = {"Adam": 25, "Bartek": 12, "Cezary": 21, "Dawid": 34, "Eryk": 19}

# liczebnosc_klasy = {
#     "Klasa 1a": 15,
#     "Klasa 1b": 18,
#     "Klasa 2a": 25,
#     "Klasa 2b": 22,
#     "Klasa 3a": 32,
#     # "Klasa 3b": 36,
#     "Klasa 3b": 100,
# }


# print(liczebnosc_klasy["Klasa 3b"])
# print(liczebnosc_klasy.keys())
# print(liczebnosc_klasy.values())
# print(liczebnosc_klasy.items())


# json
posiadane_pokemony = {
   "Adam": ["Pikachu", "Squirtle"],
   "Bartek": ["Charmander", "Bulbasaur"],
   "Cezary": ["Bulbasaur", "Squirtle"],
   "Dawid": ["Squirtle", "Pikachu"],
   "Eryk": ["Gengar", "Charmander", "Mewtwo", "Mew"],
}

# print("Charmander" in posiadane_pokemony["Bartek"])
# print("Pikachu" in posiadane_pokemony["Bartek"])

# lista kluczy
klucze = list(posiadane_pokemony.keys())
print(klucze)
print(type(klucze))
print()

# lista wartości
wartosci = list(posiadane_pokemony.values())
print(wartosci)
print(type(wartosci))
print()

# lista par klucz-wartość
pairs = list(posiadane_pokemony.items())
print(pairs)  # ('Adam', ['Pikachu', 'Squirtle'])
print(type(pairs))
print()

print("pokemony Adama: ", posiadane_pokemony["Adam"])
print("pokemony Adama, pierwszy pokemon: ", posiadane_pokemony["Adam"][0])

# zmiana wartości przypisanej do klucza
posiadane_pokemony["Adam"] = ["ABC", "DEF", "GHI"]
print("pokemony Adama po wymianie: ", posiadane_pokemony["Adam"])

# dodawanie nowego rekordu (klucz i wartość)
posiadane_pokemony["Filip"] = ["Bulbasaur", "Squirtle", "Charmander"]
print("pokemony Filipa: ", posiadane_pokemony["Filip"])
print(list(posiadane_pokemony.keys()))

# usuwanie rekordu (klucz i wartość)
del posiadane_pokemony["Cezary"]
print(list(posiadane_pokemony.keys()))