imie = input("Podaj swoje imię: ")

# Wita się 10 razy po imieniu
# print(f"Cześć {imie} 1!")
# print(f"Cześć {imie} 2!")
# print(f"Cześć {imie} 3!")
# print(f"Cześć {imie} 4!")
# print(f"Cześć {imie} 5!")
# print(f"Cześć {imie} 6!")
# print(f"Cześć {imie} 7!")
# print(f"Cześć {imie} 8!")
# print(f"Cześć {imie} 9!")
# print(f"Cześć {imie} 10!")

# Wita się 10 razy po imieniu z użyciem pętli for
for i in range(50):
    print(f"Cześć {imie} {i + 1}!")

print("koniec programu")

for tymczasowa_zmienna in {"a", "b", "c", "d"}:
    print(f"Cześć {imie} {tymczasowa_zmienna}!")
