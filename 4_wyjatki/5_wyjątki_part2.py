liczba = input("Podaj liczbę: ")  # "xd"
try:
    print("początek TRY")
    if liczba == "xd":
        print("wszedłem do IFa xd")
        raise ZeroDivisionError
    liczba = int(liczba)  # ValueError
    # liczba = liczba + 2  # TypeError
    # liczba = 10 / 0  # ZeroDivisionError
    print("koniec TRY")

except ValueError:
    print("Wykonuje się wyjątek ValueError")

except TypeError as error:
    print("Wykonuje się wyjątek TypeError")
    print("Przechwyciłem komunikat błędu:", error)

except ZeroDivisionError as error:
    print("Wykonuje się wyjątek ZeroDivisionError")

except:
    print("Tego nie przewidziałem")

else:
    print("ELSE Wykonało się bez wyjątku")

finally:
    print("FINALLY Zawsze się wykonuje na koniec programu")


print("*" * 100)

try:
    print("początek TRY 2")
    liczba = liczba + 2  # TypeError
except TypeError:
    print("Wystąpił błąd TypeError 2")
finally:
    print("FINALLY 2 Zawsze się wykonuje na koniec programu")



print("koniec programu")
