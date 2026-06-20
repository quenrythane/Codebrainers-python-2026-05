word = 'Ala ma  kota'
#       P   y  t  h  o  n
#
#       0   1  2  3  4  5
#       -6 -5 -4 -3 -2 -1

"""wycianie pojdeynczej znaku"""
print(word)
print(word[2])
print(word[3])
print(word[4])
print(word[-4])
print(word[8])

"""wycianie ciąg znaków"""
word = 'Python'
# word[start:stop]  # start od ŁĄCZNIE, stop ROZŁĄCZNIE
print(word[0:4])
print(word[0:2])  # Py
print(word[:2])  # Jeżeli chcemy od poczatku to możeme nie podawać indeksu start
print(word[2:])  # Jeżeli chcemy do konca to możeme nie podawać indeksu stop
print("yth:", word[1:4])
print(word[4:1])  # tu zrobiliśmy źle - bo indeks start musi być mniejszty niż indeks stop
print(word[-3:])

"""wycianie ciąg znaków z krokiem"""
word = 'Python'
# word[start:stop:step]
print(word[0:4:2])  # co drugi
print(word[::-1])  # odwrotna kolejnosc
print(word[::-2])  # odwrotna kolejnosc


# print(word[0:4:-1])  # odwrotna kolejnosc
# Pyth => htyP
sliced_word = word[0:4]  # Pyth
print(sliced_word[::-1])  # htyP
print(word[3::-1])






