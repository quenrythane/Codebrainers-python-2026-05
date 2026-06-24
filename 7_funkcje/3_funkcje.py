
def przygotuj_herbate(rodzaj_herbaty, nazwa_kubka, ilość_wody_w_mililitrach=200):
    print("Sprawdź czy w czajniku jest woda")
    print("Jeśli potrzeba dolej wodę do czajnika")
    print("Włącz czajnik")
    print("Czekaj aż woda się zagotuje")
    print("Sprawdź czy czajnik się wyłączył")
    print(f" Przygotuj {nazwa_kubka}")
    print(f"Wlej wodę {ilość_wody_w_mililitrach} ml do {nazwa_kubka}")
    print(f"Wsyp herbatę {rodzaj_herbaty} do {nazwa_kubka}")
    print("Poczekaj aż się zaparzy")
    print(f"Twoja {rodzaj_herbaty} herbata jest gotowa\n\n")
    

# parametr vs argument


# osoba1 = input("Podaj imię: ")
# herbata1 = input("Podaj rodzaj herbaty: ")

przygotuj_herbate("ZIELONA", "Kubek w samolociki".upper(), 350)
przygotuj_herbate("CZARNA", "Kubek kota".upper())
# przygotuj_herbate("CZARNA")
# przygotuj_herbate("CZERWONA")


