"""
Ve svém repozitáři vytvořte soubor third.py, jako vzor použijte soubor přiložený k tomuto zadání. Upravte funkci je_prvocislo tak, aby pro jakékoli celé číslo vrátila True pokud je prvočíslo a False pokud není:
1 -> False
2 -> True
3 -> True
100 -> False
101 -> True
Upravte i druhou funkci vrat_prvocisla, které pro zadané maximum vrátí seznam prvočísel mezi 1 a zadaným maximem (včetně):
1 -> []
2 -> [2]
3 -> [2, 3]
10 -> [2, 3, 5, 7]
"""
from math import sqrt

def urcityp_vrat_pouze_int(parametr1):
    print(f"Zadané číslo: {parametr1} je typu {type(parametr1)}")
    cislo_typ = type(parametr1)
    if cislo_typ == int:
        return int(parametr1)
    elif cislo_typ == str:
        text = parametr1
        if ',' in text:
            #cislo1 = tuple(text)
            print(f"Zadané číslo: {parametr1} se převádí jako typ 'tuple'")
        else:
            if '.' in text:
                #cislo1 = float(text)
                print(f"Zadané číslo: {parametr1} se převádí jako typ 'float'")
            else: 
                cislo1 = int(text)
                print(f"Zadané číslo: {parametr1} se převádí jako typ 'int'")
                return cislo1

def je_prvocislo(cislo):
    cislo_prv = 0
    cislo_typ = type(cislo)
    if cislo_typ == int: cislo_prv = cislo
    if cislo_typ == str:
        text = cislo
        if ',' in cislo:   print(f"Zadané číslo: {cislo} je typu {cislo_typ}")


    cisloparam = int(cislo)
    if cisloparam > 0:
        odmocnina = sqrt(cisloparam)
    else:
        print(f"Zadané číslo: {cisloparam} < 1. Proto náš   ")


if __name__ == "__main__":
    cislo = input("Zadej celé číslo: ")
    type(cislo)
    if type(cislo) == str:
        #cislo = int(cislo)
        print(f"Zadané číslo: {cislo} ")
    elif cislo == float:
        print(f"Zadané číslo: {cislo} není celé číslo")
    else: print(f"Zadané číslo: {cislo} není celé číslo")
    
