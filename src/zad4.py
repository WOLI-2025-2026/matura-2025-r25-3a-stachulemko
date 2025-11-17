# Stanisław Kępka - Zadanie 2

def trojkowy_na_dziesietny(napis):
    """Konwertuje napis (o,+,*) na liczbę dziesiętną"""
    wynik = 0
    for i, symbol in enumerate(reversed(napis)):
        if symbol == 'o':
            wartosc = 0
        elif symbol == '+':
            wartosc = 1
        elif symbol == '*':
            wartosc = 2
        wynik += wartosc * (3 ** i)
    return wynik

def dziesietny_na_trojkowy(liczba):
    """Konwertuje liczbę dziesiętną na zapis trójkowy (o,+,*)"""
    if liczba == 0:
        return 'o'
    
    wynik = ''
    while liczba > 0:
        reszta = liczba % 3
        if reszta == 0:
            wynik = 'o' + wynik
        elif reszta == 1:
            wynik = '+' + wynik
        elif reszta == 2:
            wynik = '*' + wynik
        liczba //= 3
    return wynik

with open("/workspaces/matura-2025-r25-3a-stachulemko/src/symbole.txt", "r") as f:
    linie = f.readlines()

suma = 0
max_liczba = 0
max_napis = ""


for linia in linie:
    napis = linia.strip()
    if napis:  
        liczba = trojkowy_na_dziesietny(napis)
        suma += liczba
        
        if liczba > max_liczba:
            max_liczba = liczba
            max_napis = napis

suma_trojkowa = dziesietny_na_trojkowy(suma)


with open("/workspaces/matura-2025-r25-3a-stachulemko/src/wyniki/zad4output.txt", "w") as wynik:
    wynik.write(f"{suma} {suma_trojkowa}\n")

print(f"{suma} {suma_trojkowa}")