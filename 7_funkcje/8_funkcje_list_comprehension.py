lista_liczb = [1, 2, 3, 4, 5]

lista_kwadratow = []
for liczba in lista_liczb:
    lista_kwadratow.append(liczba ** 2)

print("lista_kwadratow:", lista_kwadratow)

# list comprehension
lista_kwadratow_2 = [liczba ** 2 for liczba in lista_liczb]
print("lista_kwadratow_2:", lista_kwadratow_2)

# list comprehension z warunkiem
# if liczba % 2 == 0 sprawdza czy liczba jest parzysta
lista_kwadratow_3 = [liczba ** 2 for liczba in lista_liczb if liczba % 2 == 0]
print("lista_kwadratow_3:", lista_kwadratow_3)

