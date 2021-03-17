Exercises - Interacting with the Command Line
---

1. Creati o structura de fisiere / directoare, intr-un director la alegerea voastra, dupa urmatorul model:


    auto_tag /
        - cli.py
        - exception.py
        - detectors.py
        - database.py
        tests /
            data /
                - detectors_example.py
            database /
                - connection.py
            - conftest.py
            - detectors.yaml
            - cli.yml
            - cli.ini
            - env.conf
            - database.ini

2. Reorganizati structura astfel incat:

* database.ini sa ajunga in directorul auto_tag/tests/database
* cli.yml sa se numeasca cli.yaml

3. Creati un fisier care sa se numeasca -exception.yaml.

4. Adaugati continut in fisiere dupa cum urmeaza:

auto_tag / cli.py


    #!/usr/bin/env python
        def main():
            # TODO: add more functionality to this def
            print("Hello World!")
        if __name__ == "__main__":
        # TODO: is this really needed?
        main()

auto_tag / detectors.py

    #!/usr/bin/env python
    
    def detectors():
        #TODO: implement detectors
        pass
auto_tag / database.py

    #!/usr/bin/env python
    
    def database():
    ###TODO: implement database
    pass
auto_tag / tests / data / detecotrs_example.py

    #!/usr/bin/env python3
    ## TODO: implement unit tests for detectors
auto_tag / tests / database / connection.py

    #!/usr/bin/env python3
    # TODO: implement unit tests for database connections
auto_tag / database / database.ini

    [database]
    host = localhost:3306
    user = my_secret_user
    password = topSecret!


5. Cautari de fisiere:

* Gasiti toate fisierele care au extensia .yaml
* Gasiti toate fisierele care au extensia .yaml sau .ini
* Gasiti toate fisierele care nu au extensia .py
* Gasiti toate fisierele care nu au continut

6. Cautari in fisiere:

* Gasiti toate numele de fisiere care contin comentarii
* Gasiti toate TODO-urile din toate fisierele
* Afisati numele functiilor din toate fisierele cu extensia.py. Exemplu: In segmentul de cod "def detectors()", "detectors" este numele functiei
* Gasiti toate fisierele care vor interpretate folosind Python
* Gasiti si afisati interpretorii unici folositi in script-uri. Exemplu: In segmentul de cod "#!/usr/bin/env python", "python" este programul care va rula codul respectiv.

7. Permisiuni / Ownership:
* Schimbati permisiunile pentru fisierele cu extensia .py astfel incat:

    * owner-ul are drept de citire, scriere si executie
    * group si other nu au nici un fel de drepturi
* Schimbati permisiunile pentru orice fisier nu are extensia .py astfel incat:

    * owner-ul sa poata DOAR sa citeasca continutul
    * group si other nu au nici un fel de drepturi
* BONUS: fiecare actiune de mai sus indeplinita printr-un "one liner" (comenzi inlantuite)

* Afisati toate fisierele si directoarele impreuna cu permisiunile lor pentru a verifica permisiunile