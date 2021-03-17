#!/usr/bin/env python3

usr_input = int(input('Verifica un numar daca este prim: '))

def is_prime(dividend):
    prim = True
    for divisor in (2, dividend):
        while prim:
            if dividend % divisor == 0:
                prim = False
            else:
                prim = True
                break

    if prim:
        print('Numarul %d este prim' % dividend)
    else:
        print('Numarul %d nu este prim'% dividend)


is_prime(usr_input)