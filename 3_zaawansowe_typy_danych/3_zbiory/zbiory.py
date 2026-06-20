zbior = {"Ala", "Bartek", "Cezary", "Dawid", "Eryk", "Ala", "Bartek"}
print(zbior)

print("Czy jest Adam:", "Adam" in zbior)
print("Czy nie ma Adama:", "Adam" not in zbior)
print("Czy jest Ala:", "Ala" in zbior)
print()

print("Ilość osób:", len(zbior))
zbior.add("Ala")  # ala już jest a zbiór nie przyjmuje duplikatów
print("Ilość osób:", len(zbior))
zbior.add("Adam")  # ala już jest a zbiór nie przyjmuje duplikatów
print("Ilość osób:", len(zbior))

zbior_osob_na_1_roku = {"Adam", "Bartek", "Cezary", "Dawid", "Eryk"}
zbior_osob_na_2_roku = {"Adam", "Bartek", "Filip"}
print(zbior_osob_na_1_roku.difference(zbior_osob_na_2_roku))
print(zbior_osob_na_2_roku.difference(zbior_osob_na_1_roku))

print(zbior_osob_na_1_roku - zbior_osob_na_2_roku)
print(zbior_osob_na_2_roku - zbior_osob_na_1_roku)
print(zbior_osob_na_1_roku | zbior_osob_na_2_roku)
print(zbior_osob_na_1_roku & zbior_osob_na_2_roku)
print(zbior_osob_na_1_roku ^ zbior_osob_na_2_roku)

lista_imion = ["Adam", "Adam", "Adam", "Bartek", "Cezary", "Bartek"]
lista_imion = list(set(lista_imion))
print(lista_imion)