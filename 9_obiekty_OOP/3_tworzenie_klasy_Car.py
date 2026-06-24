class CarXD:
    def __init__(self, marka_xd, rok_produkcji, rodzaj_paliwa):
        self.marka = marka_xd
        self.rok_produkcji = rok_produkcji
        self.rodzaj_paliwa = rodzaj_paliwa

    def jedz(self):
        print(f"{self.marka} jedzie... Vroom Vroom")


polonez = CarXD("Polonez", 1978, "benzyna")
print("polonez.marka", polonez.marka)
print("polonez.rok_produkcji", polonez.rok_produkcji)
polonez.jedz()
print(type(polonez))
print(type("Artur"))


# malucha = Car("Maluch", 1980, "benzyna")
# print("malucha.marka", malucha.marka)
# print("malucha.rok_produkcji", malucha.rok_produkcji)