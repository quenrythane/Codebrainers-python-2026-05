
# int - integer - liczba całkowita, np 5, -12, 0
# float - float - liczba zmiennoprzecinkowa, np 5.0, -12.5, 0.1
# str - string - ciąg znaków, np
    # "Artur",
    # "a",
    # ".",
    # "5",
    # "Ala ma kota"
# bool - boolean - wartość logiczna, np True, False
# none - typ pusty, nic nie zawiera, wartość None, np ""

moj_int = 5
moj_float = 5.4
moj_string = "5"
moj_bool = False
moj_none = None


print("moj_int: ", type(moj_int))
print("moj_float: ", type(moj_float))
print("moj_string: ", type(moj_string))
print("moj_bool: ", type(moj_bool))
print("moj_none: ", type(moj_none))

wynik1 = "2" + "5"
print("wynik1:", wynik1)

wynik2 = "Ala" + " " + "MAKOTA"
print("wynik2:", wynik2)

wynik3 = int("2") + int("5")
print("wynik3:", wynik3)

#wynik4 = int("Artur") + int("Kowalski")
#print("wynik4:", wynik4)

wynik5 = "-" * 100
print("wynik5:", wynik5, type(wynik5))


