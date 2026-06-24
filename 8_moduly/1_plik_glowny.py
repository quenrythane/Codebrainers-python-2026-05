from folder_z_folderami.folder_z_funkcjami.modul_parzenia_herbaty import przygotuj_herbate


osoba = input("Jak masz na imię: ")
wybrana_herbata = input("Jaki rodzaj herbaty preferujesz: ")
wybrany_kubek = input("W jakim kubku preferujesz herbatę: ")


herbata_dla_osoby = przygotuj_herbate(wybrana_herbata, wybrany_kubek)
print(f"{osoba} oto twoja {herbata_dla_osoby}")

# ins
# insert


# stwórz folder w którym stworzył plik (moduł)
# wewnątrz tego pliku stwórz 2 funckje: dodawnie() i odejmowanie()
# poza folderem stwórz plik main.py
# w pliku main.py zaimportuj obie funkcje z pliku (modułu)
# w pliku main.py wywołaj funkcje dodawani i odejmowani. Wyprintuj wyniki
# uruchom program
