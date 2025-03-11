# zad 1

def pietro():
    print("|------|")
    print("|  []  |")
    print("|------|")


pietro() 
pietro()  

# zad 2

def dach():
    szerokosc = 10
    wysokosc = szerokosc // 2  

    for i in range(wysokosc):
        spacje = " " * (wysokosc - i - 1)  # Spacje do wyśrodkowania
        gwiazdki = "/" + " " * (2 * i) + "\\"  # Tworzenie trójkąta
        print(spacje + gwiazdki)

def pietro():
    print("|--------|")
    print("|  []    |")
    print("|--------|")

def fundament():
    print("|________|")


dach()      
pietro()    
pietro()    
fundament() 

# zad 3

def dach(znak):
    szerokosc = 10
    wysokosc = szerokosc // 2  # Obliczamy wysokość dachu
    
    for i in range(wysokosc):
        spacje = " " * (wysokosc - i - 1)  # Spacje do wyśrodkowania
        krawedzie = znak + " " * (2 * i) + znak  # Tworzenie trójkąta z użyciem podanego znaku
        print(spacje + krawedzie)

def pietro(znak):
    print(f"{znak*10}")  # Górna krawędź piętra
    print(f"{znak}  []  [] {znak}")  # Ściany + okna
    print(f"{znak*10}")  # Dolna krawędź piętra

def fundament(znak):
    print(f"{znak*10}")

# Testowanie funkcji z różnymi znakami
print("Dom ze znakiem '!'")
dach("!")
pietro("!")
pietro("!")
fundament("!")

print("\nDom ze znakiem '#'")
dach("#")
pietro("#")
pietro("#")
fundament("#")


# zad 4
def dach(znak):
    szerokosc = 10
    wysokosc = szerokosc // 2  # Obliczamy wysokość dachu
    
    for i in range(wysokosc):
        spacje = " " * (wysokosc - i - 1)  # Spacje do wyśrodkowania
        krawedzie = znak + " " * (2 * i) + znak  # Tworzenie trójkąta z użyciem podanego znaku
        print(spacje + krawedzie)

def pietro(znak):
    print(f"{znak*10}")  # Górna krawędź piętra
    print(f"{znak}  []  [] {znak}")  # Ściany + okna
    print(f"{znak*10}")  # Dolna krawędź piętra

def fundament(znak):
    print(f"{znak*10}")

def rysuj_dom(liczba_pieter, znak_dachu, znak_pietra):
    dach(znak_dachu)  # Rysowanie dachu
    for _ in range(liczba_pieter):  # Rysowanie pięter
        pietro(znak_pietra)
    fundament(znak_pietra)  # Rysowanie fundamentu

# Testowanie funkcji z różnymi parametrami
print("Dom z 3 piętrami, dach ze znaku '^', piętra z '|':")
rysuj_dom(3, "^", "|")

print("\nDom z 2 piętrami, dach ze znaku '*', piętra z '#':")
rysuj_dom(2, "*", "#")


# zad 5

def szukajWLiscie(lista, a):
    return lista.count(a)

print("Liczba elementów w liście:", szukajWLiscie([1,2,3,4,4,4], 4))

# zad 6

def szukajWLiscie(lista, a):
    if isinstance(a,  (int, float)):
        szukana = a
    elif isinstance(a, str):
        try:
            szukana = float(a)
            if szukana.is_integer():
                szukana = int(a)
        except ValueError:
            szukana = sum(ord(znak) for znak in a)
    elif isinstance(a, bool):
        szukana = int(a)
    else:
        raise TypeError("Nieobsługiwany typ")
    
    return lista.count(szukana)

lista_testowa = [1, 42, 3.14, 97, "Python", 0, 42, "42", "ABC", True, False, "ABC"]

print(szukajWLiscie(lista_testowa, 42))    
print(szukajWLiscie(lista_testowa, "42"))   
print(szukajWLiscie(lista_testowa, 3.14))   
print(szukajWLiscie(lista_testowa, "3.14")) 
print(szukajWLiscie(lista_testowa, "ABC"))  
print(szukajWLiscie(lista_testowa, True))   
print(szukajWLiscie(lista_testowa, False)) 
#print(szukajWLiscie(lista_testowa, [1,2,3]))

# zad 7
import math

def odleglosc(P1, P2):
    return math.sqrt((P2[0] - P1[0])**2 + (P2[1] - P1[1])**2)

P1 = [1, 2]
P2 = [4, 6]

wynik = odleglosc(P1, P2)
print(f"Odległość między {P1} a {P2} wynosi: {wynik:.2f}")  

# zad 8

def obwodTrojkata(P1, P2, P3):
    bok_a = odleglosc(P1, P2)
    bok_b = odleglosc(P1, P3)
    bok_c = odleglosc(P2, P3)

    return bok_a + bok_b + bok_c

P1 = [1, 2]
P2 = [4, 6]
P3 = [3, 4]

print(obwodTrojkata(P1, P2, P3))

# zad 9 - 10

import math

def odleglosc(P1, P2):
    return math.sqrt((P2[0] - P1[0])**2 + (P2[1] - P1[1])**2)

def czy_wspolliniowe(P1, P2, P3):
    pole = abs(P1[0] * (P2[1] - P3[1]) + P2[0] * (P3[1] - P1[1]) + P3[0] * (P1[1] - P2[1])) / 2
    return pole == 0  # Jeśli pole = 0, to punkty są współliniowe

def obwod_trojkata(P1, P2, P3):
    
    if czy_wspolliniowe(P1, P2, P3):
        print("Podane punkty są współliniowe i nie tworzą trójkąta.")
        return 0  

    a = odleglosc(P1, P2)
    b = odleglosc(P2, P3)
    c = odleglosc(P3, P1)
    
    return a + b + c


print("Przykład 1 (trójkąt istnieje):")
P1 = [0, 0]
P2 = [4, 0]
P3 = [0, 3]
print(obwod_trojkata(P1, P2, P3))

print("Przykład 2 (punkty współliniowe):")
P1 = [0, 0]
P2 = [1, 1]
P3 = [2, 2]
print(obwod_trojkata(P1, P2, P3))

# zad 11

import statistics

def statystyki_listy(lista):
    mediana = statistics.median(lista)
    srednia = statistics.mean(lista)
    minimum = min(lista)
    maksimum = max(lista)
    odchylenie_std = statistics.stdev(lista) if len(lista) > 1 else 0  # Odchylenie standardowe dla >1 elementu

    return {
        "Mediana": mediana,
        "Średnia": srednia,
        "Min": minimum,
        "Max": maksimum,
        "Odchylenie standardowe": odchylenie_std
    }

lista_liczb = [10, 20, 30, 40, 50, 60, 70]

wynik = statystyki_listy(lista_liczb)
print("Statystyki listy:")
for klucz, wartosc in wynik.items():
    print(f"{klucz}: {wartosc:.2f}")


# zad 12

def czy_anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False 

print(czy_anagram("cat", "act"))

# zad 13

def sortuj_liste(lista):
    kierunek = input("Wybierz kierunek sortowania (rosnąco/malejąco): ").strip().lower()
    
    if kierunek == "rosnąco":
        return sorted(lista)
    elif kierunek == "malejąco":
        return sorted(lista, reverse=True)
    else:
        print("Niepoprawny wybór. Sortowanie domyślnie rosnące.")
        return sorted(lista)


lista_liczb = [34, 12, 5, 78, 23, 56, 9]
posortowana_lista = sortuj_liste(lista_liczb)

print("Posortowana lista:", posortowana_lista)


# zad 14

def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 1:
            return False
    return True

print(is_prime(4))

# zad 15

def lcs(X, Y, m, n):
 
    if m == 0 or n == 0:
       return 0
    elif X[m-1] == Y[n-1]:
       return 1 + lcs(X, Y, m-1, n-1)
    else:
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))
 
 
X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", lcs(X, Y, len(X), len(Y)))

# zad 16

def fibonacci(n):
    if n <= 0:
        raise ValueError("n musi być liczbą dodatnią")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Testowanie
print(fibonacci(10))  # 34


# zad 17

def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n-1)
    
print(silnia(5))

# zad 18

def konwersja_temperatury(temperatura, skala_wejsciowa, skala_docelowa):
    if skala_wejsciowa == skala_docelowa:
        return temperatura  # Jeśli skale są takie same, zwracamy tę samą wartość

    # Konwersja do Celsjusza
    if skala_wejsciowa == "F":
        temperatura = (temperatura - 32) * 5/9
    elif skala_wejsciowa == "K":
        temperatura = temperatura - 273.15

    # Konwersja z Celsjusza do skali docelowej
    if skala_docelowa == "F":
        return temperatura * 9/5 + 32
    elif skala_docelowa == "K":
        return temperatura + 273.15
    elif skala_docelowa == "C":
        return temperatura

    raise ValueError("Niepoprawna skala. Wybierz 'C', 'F' lub 'K'.")

# Testowanie funkcji
print(konwersja_temperatury(0, "C", "F"))   # 32.0
print(konwersja_temperatury(100, "C", "K")) # 373.15
print(konwersja_temperatury(212, "F", "C")) # 100.0
print(konwersja_temperatury(273.15, "K", "C")) # 0.0

# zad 19

import math

def rysuj_i_oblicz_pole(ksztalt, **parametry):
    if ksztalt == "kolo":
        promien = parametry.get("promien", 0)
        if promien <= 0:
            raise ValueError("Promień musi być większy od zera.")

        # Rysowanie koła (przybliżone)
        for y in range(-promien, promien + 1):
            linia = ""
            for x in range(-promien, promien + 1):
                if x**2 + y**2 <= promien**2:
                    linia += "*"
                else:
                    linia += " "
            print(linia)

        # Pole koła
        return math.pi * promien**2

    elif ksztalt == "kwadrat":
        bok = parametry.get("bok", 0)
        if bok <= 0:
            raise ValueError("Bok musi być większy od zera.")

        # Rysowanie kwadratu
        for _ in range(bok):
            print("*" * bok)

        # Pole kwadratu
        return bok**2

    elif ksztalt == "prostokat":
        szerokosc = parametry.get("szerokosc", 0)
        wysokosc = parametry.get("wysokosc", 0)
        if szerokosc <= 0 or wysokosc <= 0:
            raise ValueError("Szerokość i wysokość muszą być większe od zera.")

        # Rysowanie prostokąta
        for _ in range(wysokosc):
            print("*" * szerokosc)

        # Pole prostokąta
        return szerokosc * wysokosc

    else:
        raise ValueError("Nieobsługiwany kształt. Wybierz 'kolo', 'kwadrat' lub 'prostokat'.")


print("\nKoło:")
pole_kola = rysuj_i_oblicz_pole("kolo", promien=5)
print(f"Pole koła: {pole_kola:.2f}\n")

print("Kwadrat:")
pole_kwadratu = rysuj_i_oblicz_pole("kwadrat", bok=5)
print(f"Pole kwadratu: {pole_kwadratu:.2f}\n")

print("Prostokąt:")
pole_prostokata = rysuj_i_oblicz_pole("prostokat", szerokosc=6, wysokosc=3)
print(f"Pole prostokąta: {pole_prostokata:.2f}")

# zad 20

def szyfr_cezara(tekst, klucz):
    zaszyfrowany_tekst = ""

    for znak in tekst:
        if znak.isalpha():  # Sprawdzamy, czy to litera
            przesuniecie = klucz % 26  # Obsługa dużych wartości klucza
            kod_poczatkowy = ord('A') if znak.isupper() else ord('a')  # Określamy bazowy kod ASCII
            nowy_znak = chr(kod_poczatkowy + (ord(znak) - kod_poczatkowy + przesuniecie) % 26)
            zaszyfrowany_tekst += nowy_znak
        else:
            zaszyfrowany_tekst += znak  # Pozostawiamy inne znaki bez zmian

    return zaszyfrowany_tekst

tekst = "Hello, World!"
klucz = 3
zaszyfrowany = szyfr_cezara(tekst, klucz)
print(f"Tekst zaszyfrowany: {zaszyfrowany}")

# zad 21

import random

def kamien_papier_nozyce():

    opcje = ["kamień", "papier", "nożyce"]
    
    print("\nWitaj w grze 'Kamień, Papier, Nożyce'!")
    print("Wybierz: kamień, papier lub nożyce")

    # Wybór gracza
    wybor_gracza = input("Twój wybór: ").strip().lower()
    
    if wybor_gracza not in opcje:
        print("Niepoprawny wybór! Spróbuj ponownie.")
        return kamien_papier_nozyce()  # Restart gry
    
    # Wybór komputera
    wybor_komputera = random.choice(opcje)
    
    print(f"Komputer wybrał: {wybor_komputera}")

    # Określanie zwycięzcy
    if wybor_gracza == wybor_komputera:
        print("Remis! Spróbuj ponownie.")
    elif (wybor_gracza == "kamień" and wybor_komputera == "nożyce") or \
         (wybor_gracza == "papier" and wybor_komputera == "kamień") or \
         (wybor_gracza == "nożyce" and wybor_komputera == "papier"):
        print("Wygrałeś!")
    else:
        print("Przegrałeś!")

kamien_papier_nozyce()


# zad 22

def reverse_string(s):
    return s[::-1]

print(reverse_string("abc"))

# zad 23

class Person:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f"Mam na imię {self.imie} i mam {self.wiek} lat.")


osoba = Person("Jan", 25)
osoba.przedstaw_sie()  

# zad 24

class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height
    
rect = Rectangle(2, 3)
print(f"Pole prostokąta jest równe: {rect.area()}")

# zad 25

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Wpłacono {amount}. Aktualny stan konta: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Wypłacono kwotę {amount}. Aktualny stan konta: {self.balance}")
        else:
            print("Niewystarczające środki na koncie")


konto = BankAccount(100)  
konto.deposit(50)  
konto.withdraw(30)  
konto.withdraw(150)

# zad 26

class Student:
    def __init__(self):
        self.students = {} #słownik na imię: [oceny]

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = []
            print(f"Osoba o imieniu {name} została dodana do listy")
        else:
            print(f"Osoba o imieniu {name} już jest na liście")

    def add_grade(self, grade, name):
        if name in self.students:
            self.students[name].append(grade)
            print(f"Ocena {grade} została dodana dla {name}.")
        else:
            print(f"Błąd: Osoba o imieniu {name} nie istnieje na liście!")

school = Student()
school.add_student("Jan")
school.add_grade("Jan", 5)
school.add_grade("Jan", 4)
school.add_student("Anna")
school.add_grade("Anna", 3)   

# zad 27

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        if 0 <= percent <= 100:
            discount_amount = self.price * (percent / 100)
            self.price -= discount_amount
            print(f"Zastosowano rabat {percent}% na {self.name}. Nowa cena: {self.price:.2f} zł")
        else:
            print("Błąd: procent rabatu musi być między 0 a 100.")

product1 = Product("Laptop", 3000)
product1.apply_discount(10) 

product2 = Product("Smartfon", 2000)
product2.apply_discount(25)  

# zad 28

class User:
    def __init__(self):
        self.users = {}  # Przechowywanie użytkowników w formacie {username: password}

    def register(self, username, password):
        if username in self.users:
            print("Błąd: Użytkownik już istnieje!")
        elif len(password) < 6:
            print("Błąd: Hasło musi mieć co najmniej 6 znaków!")
        else:
            self.users[username] = password
            print(f"Użytkownik {username} został zarejestrowany.")

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            print(f"Zalogowano pomyślnie jako {username}.")
        else:
            print("Błąd: Nieprawidłowa nazwa użytkownika lub hasło.")


system = User()
system.register("jan", "haslo123")  
system.register("jan", "haslo123")  
system.register("anna", "123")  
system.login("jan", "haslo123")  
system.login("jan", "zlehaslo")  

