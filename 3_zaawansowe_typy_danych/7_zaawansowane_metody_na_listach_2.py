lista_imion = ["Bartek", "Adam", "Dawid", "Cezary", "Eryk"]
plytka_lista_imion = lista_imion
gleboka_lista_imion = lista_imion.copy()

# print("lista_imion:", id(lista_imion))
# print("plytka_lista_imion:", id(plytka_lista_imion))
# print("gleboka_lista_imion:", id(gleboka_lista_imion))

# metoda vs funkcja
# funkcja sorted()
posortowane_1 = sorted(lista_imion)  # zawsze zwraca wynik "wytwarza wynik"
print("lista_imion:", lista_imion)
print("lista_imion:", id(lista_imion))
print("sorted():", posortowane_1)
print("sorted():", id(posortowane_1))

# metoda sort()
# metody NIE zwracją wyniku tylko modyfikują obiekt na którym są wywoływane
posortowane_2 = lista_imion.sort()  #
print("lista_imion:", lista_imion)
print("lista_imion:", id(lista_imion))
print("metoda sort():", posortowane_2)
print("metoda sort():", id(posortowane_2))


