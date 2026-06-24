# break - kończy całą petlę
# continue - skipuje pojedyczny obieg (iteracje)

for liczba in range(115):  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if liczba == 5:      # 4 == 5 -> False | 5 == 5 -> True
        print("pomiń continue")
        continue     # skipuje daną iteracje (obieg)
    if liczba == 7:
        print("spotkałem break, więc wychodzę całkowicie z pętli")
        break  # całkowicie zrywa (wychodzi) z pętli
    print(liczba)



print("koniec pętli")
print("reszta programu")

for x in range(10):
    pass
