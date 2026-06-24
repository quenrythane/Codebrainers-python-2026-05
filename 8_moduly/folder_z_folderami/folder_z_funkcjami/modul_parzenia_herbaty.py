def przygotuj_herbate(rodzaj_herbaty, nazwa_kubka, ilość_wody_w_mililitrach=200):
    print("Sprawdź czy w czajniku jest woda")
    print("Jeśli potrzeba dolej wodę do czajnika")
    print("Włącz czajnik")
    print("Czekaj aż woda się zagotuje")
    print("Sprawdź czy czajnik się wyłączył")
    print(f" Przygotuj {nazwa_kubka.upper()}")
    print(f"Wlej wodę {ilość_wody_w_mililitrach} ml do {nazwa_kubka.upper()}")
    print(f"Wsyp herbatę {rodzaj_herbaty.upper()} do {nazwa_kubka.upper()}")
    print("Poczekaj aż się zaparzy")
    print(f"Twoja {rodzaj_herbaty.upper()} herbata jest gotowa\n\n")
    return f"Gotowa {rodzaj_herbaty.upper()} herbata w rozmiarze {ilość_wody_w_mililitrach} ml w {nazwa_kubka.upper()}"


def przygotuj_kawe(czy_z_mlekiem):
    print("Przygotuj kawę")
    if czy_z_mlekiem == True:
        print("Dodaj mleko")
    return f"Gotowa kawa {'z mlekiem' if czy_z_mlekiem else 'bez mleka'}"

