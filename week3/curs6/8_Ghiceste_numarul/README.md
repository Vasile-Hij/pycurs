Ghicește numărul
--
Scrieți un program Python care să îi ofere utilizatorului să ghicească un număr cuprins în intervalul 0 - 100 din maxim **7 încercări**.

Notă: Pentru moment numărul poate să fie predefinit în cadrul programului. De exemplu:

> secret = 67

La fiecare etapă de joc utilizatorul va trebui să propună un număr. Pentru fiecare număr primit programul va trebui să facă următoarele acțiuni:

* să verifice dacă valoarea primită este un număr în intervalul <span style="color:red"> 0 - 100</span>
    * în caz contrar va afișa pe ecran un mesaj de eroare
* să verifice etapa din joc
    * în cazul în care utilizatorul a epuizat cele **7** încercări, jocul se va termina și utilizatorul va primi un mesaj corespunzător.
* să compare numărul cu valoarea aleasă (cu <span style="color:red">secret</span>):
    * dacă valorile sunt egale, jucătorul a câștigat jocul
    * dacă valoarea aleasă este mai mică se va afișa pe ecran: <span style="color:red"> Numărul este mai mare.</span>
    * dacă valoarea aleasă este mai mare se va afișa pe ecran: <span style="color:red"> Numărul este mai mic.</span>