moja_lista = [1, 3.14, "Ania", True, None, ["a", "b", "Cezary"]]

print(type(moja_lista))
print(type(moja_lista[1]))  # 3.14  # float

wewnetrzna_lista = moja_lista[-1]  # ["a", "b", "c"]
letter = moja_lista[-1][-1][-2] # ["a", "b", "c"][-1]
print(wewnetrzna_lista)
print(letter)

lista_elementow = [[1, 2, 3], ["a", "b", "c"], [True, False, None]]

lista_elementow = [
    [1, 2, 3],
    ["a", "b", "c"],
    [True, False, None]
]
