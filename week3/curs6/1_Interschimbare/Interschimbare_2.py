#!/usr/bin/env python3

prima_valoare = 10
a_doua_valoare = 20

# metoda cu variabila temporara

variabila_temporara = prima_valoare
prima_valoare = a_doua_valoare
a_doua_valoare = variabila_temporara

print('Prima valoare este %d' % prima_valoare)
print('A doua valoare este %d' % a_doua_valoare)

