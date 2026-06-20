lista_imion = ["Adam", "Bartek", "Cezary", "Dawid", "Eryk"]

# nowa_lista_imion = lista_imion  # płytka kopia - tworzy nowy alias do istniejącej listy (nowa ksywka kolegi)
# print(nowa_lista_imion)

# nowa_lista_imion.append("Filip")
# print("lista_imion:", lista_imion)
# print("nowa_lista_imion:", nowa_lista_imion)

# kopia płytka vs kopia głęboka
poprawna_nowa_lista_imion = lista_imion.copy()  # kopia głęboka - tworzy nową listę

print("lista_imion:", lista_imion)
print("poprawna_nowa_lista_imion:", poprawna_nowa_lista_imion)
print()

poprawna_nowa_lista_imion.append("Grzesiek")
print("lista_imion:", lista_imion)
print("poprawna_nowa_lista_imion:", poprawna_nowa_lista_imion)


