#!/usr/bin/env python3

# forma simpla de verificare a unui numar par

number = int(input('Scrie un numar mai mare sau egal ca 0: '))

if number % 2 == 0:
    print('numarul %d este par' % number)
else:
    print('numarul %d nu este par' % number)