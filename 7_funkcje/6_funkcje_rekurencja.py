def suma_rekurencja(number):
    if number == 1:
        return 1
    return number * suma_rekurencja(number - 1)

wynik = suma_rekurencja(3)
print(wynik)
# print(suma_rekurencja(3))

