# Ćwiczenia - Algorytm faktoryzacji Fermata

## Faktoryzacja brute force

Faktoryzacja *brute force* liczby naturalnej $n$ polega po prostu na sprawdzaniu czy kolejne liczby dzielą $n$.

**Krok 0.** Początkowa wartość $p=2$.

**Krok 1.** Sprawdzamy, czy $p$ dzieli $n$. Jeżeli tak, to $q=n/p$ i koniec algorytmu. Jeżeli nie, to przechodzimy do następnego kroku.

**Krok 2.** Zwiększamy wartość $p=p+1$. Jeżeli $p\leq\sqrt{n}$ to wracamy do kroku 1. Jeżeli jest większe niż $\sqrt{n}$, to kończymy alogrytm.

### Ćwiczenie 1.

Zaimplementuj faktoryzację brute force jako funkcję `brute_force`.

>Implementacja w pliku [brute_force.py](./brute_force.py)


## Faktoryzacja Fermata

Algorytm faktoryzacji Fermata liczby nieparzystej $n$ opiera się na znalezieniu pary liczb $a,b$ takich, że $n=a^2-b^2$. Wtedy od razu otrzymujemy faktoryzację $$n=(a+b)(a-b).$$

Dla dowolnej złożonej liczby nieparzystej (tzn. liczby nieparzystej nie będącej liczbą pierwszą) znajdziemy takie liczby $a,b$. W szczególności, w przypadku $n=pq$ mamy $$a=\frac{p+q}{2},\qquad b=\frac{p-q}{2}.$$

#### Krok 0.
Sprawdzamy, czy $\sqrt{n}$ jest liczbą naturalną. Jeżeli tak - znaleźliśmy faktoryzację i koniec algorytmu.
#### Krok 1.
Definiujemy zmienne pomocnicze
$$a = \left\lceil\sqrt{n}\right\rceil,\qquad
b^2 = a^2 - n.$$
#### Krok 2.
Jeżeli $\sqrt{b^2}$ jest liczbą całkowitą, to kończymy algorytm i zwracamy $a$ oraz $b=\sqrt{b^2}$. Jeżeli nie, to aktualizujemy zmienne:
$$a=a + 1,\qquad b^2=a^2 - n.$$

### Ćwiczenie 2.
Zaimplementuj algorytm faktoryzacji Fermata jako funkcję `fermat`.

>Implementacja w pliku [fermat.py](./fermat.py)

### Ćwiczenie 3.

Przetestuj działanie swoich implementacji na poniższych liczbach. Sprawdź średni czas wykonania faktoryzacji za pomocą `%%timeit`.

n1 = 2101644002566781
n2 = 3593875791313441
n3 = 800090608581732401
n4 = 22601441855002489679

