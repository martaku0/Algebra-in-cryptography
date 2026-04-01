# RSA
## Algorytm RSA (Kryptografia asymetryczna)

Algorytm RSA opiera się na własnościach dużych liczb pierwszych i trudności problemu faktoryzacji (rozkładu dużej liczby na czynniki p i q). Działanie algorytmu składa się z etapu generowania pary kluczy, a następnie używania ich do szyfrowania i deszyfrowania wiadomości.

**Część I: Generowanie kluczy**

Krok 0. Wybieramy dwie duże, różne liczby pierwsze p oraz q.

Krok 1. Obliczamy wartość modułu n=p⋅q. Liczba n jest jawna i określa maksymalną wielkość pojedynczej szyfrowanej wiadomości.

Krok 2. Obliczamy wartość funkcji Eulera dla modułu n, korzystając ze wzoru: ϕ(n)=(p−1)(q−1). Wartość ta musi pozostać ściśle tajna.

Krok 3. Wybieramy wykładnik publiczny e, taki, aby 1<e<ϕ(n) oraz aby liczby e i ϕ(n) były względnie pierwsze (ich największy wspólny dzielnik to 1).

    Para (n,e) stanowi klucz publiczny, który udostępniamy wszystkim, aby mogli do nas szyfrować wiadomości.

Krok 4. Wyznaczamy wykładnik prywatny d, który jest odwrotnością modularną e. Oznacza to, że znajdujemy takie d, dla którego zachodzi równanie d⋅e≡1(modϕ(n)) (czyli reszta z dzielenia d⋅e przez ϕ(n) wynosi 1).

    Para (n,d) stanowi klucz prywatny, który zachowujemy w ścisłej tajemnicy do odczytywania wiadomości.

**Część II: Szyfrowanie i Deszyfrowanie**

Załóżmy, że nasza wiadomość to liczba m (taka, że m<n).

    Szyfrowanie (dla nadawcy): Do zaszyfrowania wiadomości m używamy klucza publicznego odbiorcy (n,e). Obliczamy szyfrogram c według wzoru:
    c=m^e(mod n)

    Deszyfrowanie (dla odbiorcy): Do odczytania szyfrogramu c używamy naszego tajnego klucza prywatnego (n,d). Odzyskujemy oryginalną wiadomość m według wzoru:
    m=c^d(mod n)

**Implementacja algorytmu**  
>Implementacja w pliku [rsa.py](./rsa.py)