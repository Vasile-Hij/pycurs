Agenda telefonica stoacata pe disc.
--
>Romanian language

**Fields:**
- nume
- prenume
- numar_de_telefon
- adresa_de_email

Meniu (functie):
- adaugam inregistrar
- modificam inregistrar
- stergem inregistrar- cautam inregistrari

- input de la utilizator (A - adauga, M - modifica, S - stergere, C - cautare)
    - valideaza input
    - apeleaza niste functii in functie de input


**Operatiuni agenda**

ADAUGARE
- cere input de la utilizator
- valideaza input-ul (OPTIONAL)
- scrie input-ul in fisier

MODIFICARE
- incarca inregistrarile din fisier (lista?)
- cere input de la utilizator
    - valideaza input-ul (OPTIONAL)
    - ce inregistrare trebuie modificata?
    - ce campuri trebuiesc modificate sau suprascriem toate campurile?
- salveaza schimbarile in fisier
Fisier: A,B,C -> Python A,B,C -> Python modific B->B' -> Fisier A,B',C

STERGERE
- incarca inregistrarile din fisier
- cere input de la utilizator
    - ce inregistrare / inregistrari trebuiesc sterse?
- salveaza schimbarile in fisier

CAUTARE
- incarca inregistrarile din fisier
- cere input de la utilizator
- itereaza prin elementele din lista
    - compara input-ul de la utilizator cu elementele din fiecare field
    - returneaza si afiseaza elementele care corespund
