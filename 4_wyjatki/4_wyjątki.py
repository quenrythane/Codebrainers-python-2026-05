liczba = input("Podaj liczbę: ") # "dwa"

try:
    liczba = int(liczba)
    print("Udało się zamienić na liczbę int")
except ValueError:  # wykona się tylko wtedy gdy liniji try zwróciły by błąd
    print("Wprowadzona wartość nie jest liczbą")

waga_bagażu = 0
try:   # if program może wykonać się poprawnie bez błedu
    waga_bagażu < 50
    print("wyoknuje kod try")
except:  # else jeśli program zwróci błąd
    print("Błąd - niewłaściwa waga")

print("koniec progarmu")
