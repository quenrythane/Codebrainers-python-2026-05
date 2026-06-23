
wiek = 15

if wiek >= 18:  # True
    print("Mogę ci sprzedać energetyka")
else:
    print("Nie mogę ci sprzedać energetyka")

# Artur "Siema mordo"
# Mati "Cześć gruby"
# łysy "Witaj Panie profesorze"
# ktokolwiek innt "Dzień dobry"


# Mati
imie = input("Podaj imię: ")

if imie == "Artur":
    print("Siema mordo")
elif imie == "Mati":
    print("Cześć gruby")
elif imie == "łysy":
    print("Witaj Panie profesorze")
else:
    print("Dzień dobry")


# zapytaj usera ile ma lat (pamiętaj że input zapisuej liczbęjako string)
# sprawdź czy jest pełnoletni (>= 18)
# jeśli tak to napisz że może kupić energetyka
# jeśli nie to napisz że nie może kupić energetyka

wiek = input("Podaj swój wiek: ")
wiek = int(wiek)

wiek = 20
print(wiek >= 18)

if wiek >= 18:
    print("Możesz kupić energetyka")
else:
    print("Nie możesz kupić energetyka")

