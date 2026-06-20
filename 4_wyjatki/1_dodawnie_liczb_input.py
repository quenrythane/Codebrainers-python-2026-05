liczba_1 = input("Podaj liczbę nr 1: ")  # domyślnie przyjmuje typ danych jako string
liczba_2 = input("Podaj liczbę nr 2: ")

try:
    liczba_1 = int(liczba_1)  # "2" -> 2 "dwa"
    print("udało zamienić się w liczbę int")
except ValueError:
    print("Podano niepoprawną wartość")
liczba_2 = int(liczba_2)  # "5" -> 5


print(liczba_1 + liczba_2)



# liczba_1 = "2"  # string
# liczba_2 = "5"  # string

# liczba_1 = int(liczba_1)
# liczba_2 = int(liczba_2)

# print(liczba_1 + liczba_2)

