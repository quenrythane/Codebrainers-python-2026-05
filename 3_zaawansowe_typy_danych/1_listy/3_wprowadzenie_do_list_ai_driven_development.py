""" Ćwiczenie: """
# 1. stwórz listę z 5-cioma imionami
# 2. wypisz elementy listy (wydrukuj listę)
# 3. wydrukuj typ listy
# 4. wydrukuj element list o indeksie 1
# 5. wydrukuj typ elementu listy o indeksie 1
# 6*. używając f stringa powiedz że osoby z listy z indeksu -2 i -1 to koledzy
# 7*. na bazie listy stwórz nową liste (slice'owanie)
# skłądjąc się z co drugiego elementu pierwotnej listy

# 1. stwórz listę z 5-cioma imionami
names = ["Anna", "Jan", "Krzysztof", "Maria", "Piotr"]

# 2. wypisz elementy listy (wydrukuj listę)
print("Lista imion:", names)

# 3. wydrukuj typ listy
print("Typ listy:", type(names))

# 4. wydrukuj element list o indeksie 1
print("Element o indeksie 1:", names[1])

# 5. wydrukuj typ elementu listy o indeksie 1
print("Typ elementu o indeksie 1:", type(names[1]))

# 6*. używając f stringa powiedz że osoby z listy z indeksu -2 i -1 to koledzy
print(f"Osoby z listy o indeksach -2 i -1 ({names[-2]} i {names[-1]}) to koledzy.")

# 7*. na bazie listy stwórz nową liste (slice'owanie) składającą się z co drugiego elementu
print("Nowa lista (co drugi element):", names[::2])
