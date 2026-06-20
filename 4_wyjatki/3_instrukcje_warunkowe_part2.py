# print("Chłopiec" == "Dziewczynka")  # == porównanie (czy jest równe?)
# print("Chłopiec" != "Dziewczynka")  # != porównanie (czy jest różne?)
# print(20 > 19)   # > porównanie (czy jest większe?)
# print(20 < 19)   # < porównanie (czy jest mniejsze?)
# print(20 >= 19)  # >= porównanie (czy jest większe lub równe?)
# print(20 <= 19)  # <= porównanie (czy jest mniejsze lub równe?)
# print(20 >= 20)  # >= porównanie (czy jest większe lub równe?)
# print(20 <= 20)  # <= porównanie
# print(20 == 20)  # == porównanie
# print(20 != 20)  # != porównanie

# punkty = 88

# if punkty < 50:  # False
#     print("nie zdałeś")
# elif punkty < 60:  # False
#     print("zdałeś na 3")
# elif punkty < 70:  # False
#     print("zdałeś na 4")
# elif punkty < 80:  # False
#     print("zdałeś na 5")
# elif punkty < 90:  # True
#     print("zdałeś na 6")  # ta linijka się wykonała
# elif punkty < 100:  # nie patrzę bo wyżej było True
#     print("zdałeś na 7")
# else:   # nie patrzę bo wyżej było True
#     print("punkty poza skalą")



# # klub tylko dla kobiet
# imie = "Sama"
# if imie[-1] == "a":
#     print("Zapraszam do klubu")
# else:
#     print("Nie ma mowy, nie możesz wejść")


# waga_bagażu = "0"
# if waga_bagażu < 50:
#     print("Waga bagażu jest dopuszczalna")
# elif waga_bagażu == 50:
#     print("Waga bagażu jest idealna")
# elif waga_bagażu > 50:
#     print("Musisz dopłacić za nadmiarowe kilogramy")
# else:
#     print("Błąd - niewłaściwa waga")


waga_bagażu = 0
try:   # if program zwróci błąd
    waga_bagażu < 50
    print("wyoknuje kod try")
except:
    print("Błąd - niewłaściwa waga")

print("koniec progarmu")