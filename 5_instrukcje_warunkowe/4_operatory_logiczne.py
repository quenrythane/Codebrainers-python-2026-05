# not  - zaprzeczenie / odwrotność
# and - i (oba warunki muszą być spełnione) (iloczny logiczyn)
# or - lub (wystarczy, że jeden warunek będzie spełniony) (suma logiczna)

stan_1 = True
stan_2 = False

# print("stan_1:", stan_1)
# print("not stan_1:", not stan_1)
# print("not stan_2:", not stan_2)  # True

"Artur NIE jest dziewczyną"  # True


# --- Operatory OR ---
"Mati zawsze chodzi w butach puma LUB butach nike"  # True
wiek = 10
imie = "Karolina"


""" Klub dla pełnoletnich kobiet"""
if wiek >= 18 or imie[-1] == "a":
    # warunek1 wiek >= 18 == True
    # warunek2 imie[-1] == "a" == False
    # warunek1 or warunek2  =>  True and False == False
    # to co jest zagnieżdżone wewnątrz IF wykona się TYLKO jeśli warunek przy IF będzie == True
    print("Możesz wejść do klubu")
else:
    # to co jest zagnieżdżone wewnątrz ELSE wykona się TYLKO jeśli IF się NIE wykona
    print("TO JEST ELSE. Nie możesz wejść do klubu")



# --- Operatory AND ---
# To jest zdanie złożone. Wnioskujemy na podstawie logiki.


# print("stan_1 and stan_2", stan_1 and stan_2)
# print("stan_1 or stan_2", stan_1 or stan_2)




