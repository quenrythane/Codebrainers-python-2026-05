def dodawanie(liczba_1, liczba_2):
    print(liczba_1 + liczba_2)
    return liczba_1 + liczba_2

wynik = dodawanie(2, 5)
print(wynik)

def kapitalizowanie_imion(imie):
    """  # docstring
    Ta funkcja bierze string i zamienia go na imię z wielkiej litery XD \n
    To jest linia 2 \n
    To jest linia 3
    """
    return imie.capitalize()

poprawne_imie = kapitalizowanie_imion("MaReK")
print(poprawne_imie)

