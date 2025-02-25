# zad.13

def czy_rowne(a, b):
    if a == b:
        return "TAK"
    return "NIE"

print(czy_rowne("a", "a"))
print(czy_rowne("a", "ab"))

# zad. 14

def czy_parzysta(x):
    if x % 2 == 0:
        return "Parzysta"
    
print(czy_parzysta(2))

# zad. 15

def jaki_typ(a):
    if a.isdigit() or a[1:].isdigit():
        return "int"
    
    if a.lower() in ["true", "false"]:
        return "bool"
    
    try:
        float_var = float(a)
        return "float"
    except ValueError:
        pass
    
    return "str"

a = input("Podaj zmienną: ")
print(jaki_typ(a))

# zad. 16

a = input("liczba1:")
b = input("liczba2:")

print(max(a, b))

# zad. 17

a = input("liczba1:")
b = input("liczba2:")
c = input("liczba3:")

print(sorted([a,b,c])[-1])

# zad. 18

a = input("liczba1:")
b = input("liczba2:")
c = input("liczba3:")

print(sorted([a,b,c]))

# zad. 19

a = float(input("Podaj wartość a: "))
b = float(input("Podaj wartość b: "))

if a == 0:
    if b == 0:
        print("Równanie ma nieskończenie wiele rozwiązań (tożsamość).")
    else:
        print("Równanie nie ma miejsc zerowych (sprzeczne).")
else:
    x0 = -b / a
    print(f"Miejsce zerowe funkcji: x = {x0}")


# zad. 20

import math

a = float(input("Podaj wartość a: "))
b = float(input("Podaj wartość b: "))
c = float(input("Podaj wartość c: "))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print(f"Równanie ma dwa miejsca zerowe: x1 = {x1}, x2 = {x2}")
elif delta == 0:
    x0 = -b / (2 * a)
    print(f"Równanie ma jedno miejsce zerowe: x0 = {x0}")
else:
    print("Równanie nie ma miejsc zerowych (brak rozwiązań w zbiorze liczb rzeczywistych).")

# zad. 21

number = int(input("Podaj liczbę: "))

jedności = number % 10
dziesiątki = (number // 10) % 10
setki = (number // 100) % 10

print(f"Cyfra jedności: {jedności}")
print(f"Cyfra dziesiątek: {dziesiątki}")
print(f"Cyfra setek: {setki}")
