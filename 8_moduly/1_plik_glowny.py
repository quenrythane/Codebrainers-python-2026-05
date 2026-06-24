from folder_z_folderami.folder_z_funkcjami.modul_parzenia_herbaty import przygotuj_herbate


osoba = input("Jak masz na imię: ")
wybrana_herbata = input("Jaki rodzaj herbaty preferujesz: ")
wybrany_kubek = input("W jakim kubku preferujesz herbatę: ")


herbata_dla_osoby = przygotuj_herbate(wybrana_herbata, wybrany_kubek)
print(f"{osoba} oto twoja {herbata_dla_osoby}")


