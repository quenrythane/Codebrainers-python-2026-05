zdanie = "To jest magiczne zdanie"


i = 0  # 4
while True:
    print(i, zdanie)
    i += 1  # 5
    if i == 11:
        print(f"spotkałem wartość i={i} więc wszedłem do IF, spotkałem break, więc wychodzę całkowicie z pętli")
        break


print("koniec pętli")
print("reszta programu")

