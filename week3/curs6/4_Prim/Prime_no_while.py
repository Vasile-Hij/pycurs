#!/usr/bin/env python3

usr_input = int(input('Verifica un numar daca este prim: '))

dividend = usr_input
# definim o variabila
prim = False

if dividend > 1:
    for divisor in range(2, dividend):
        if (dividend % divisor == 0):
            prim = True
            break

if prim:
    print('Numarul %d nu este prim' % dividend)
    print(divisor, 'inmultit cu', dividend//divisor, 'este egal cu', dividend)
else:
    print('Numarul %d este prim' % dividend)