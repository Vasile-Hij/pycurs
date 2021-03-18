#!/usr/bin/env python3

number = int(input("Scrie un numar integral: "))


if number % 2 == 0:
    # numere pare > x / 2
    for numbers_output in range(number // 2 + 1, number + 1): # 12 // 6 + 1 va afisa de la 7 la 12(x) (+1 pana la 12 inclusiv)
        print(f'Numere pare mai mari decat x / 2:', numbers_output)
    # numere impare < x / 2
elif number % 2 == 1 and not number % 5 == 0:
    for numbers_output in range(number // 2 + 1):
        print(f'Numere impare mai mici decat x/2, dar nedivizibile cu 5:', numbers_output)
else:
    for numbers_output in range(0, number // 5 + 1, 3): # ex : 45 va afisa: 0, 3, 6, 9
        print(f'Numerele mai mici divizibile cu 5 din 3 in 3:', numbers_output)