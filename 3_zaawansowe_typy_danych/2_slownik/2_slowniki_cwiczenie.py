# utwórz słownik z 5 rekordami.
# Niech kluczami będzie nazwa owocu
# Niech wartością klucza będzie kolor owocu

# Wyświetl listę kluczy
# Wyświetl listę wartości
# Wyświetl listę par klucz-wartość

# Wybierz jeden owoc i usuń go ze słownika
# Wybierz jeden owoc i zmień jego kolor
# Wybierz jedną nazwę owocu i dodaj nowy kolor do tej nazwy

# zwróć kolor wybranego owocu (posiadane_pokemony["Adam"])


owoce = {
    "jabłko" : "zielone",
    "banan" : "żółte",
    "winogrono" : "fioletowe",
    "truskawka" : "czerwone",
    "malina" : "różowa",
}

print(list(owoce.keys()))
print(list(owoce.values()))
print(list(owoce.items()))
print()

del owoce["jabłko"]
print(list(owoce.keys()))
print()

owoce["banan"] = "czarny"
print(owoce["banan"])
print(owoce["winogrono"])
print()

owoce["kiwi"] = "brązowy"