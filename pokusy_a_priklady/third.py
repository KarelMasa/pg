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
    #print(f"Zadané číslo: {parametr1} je typu {type(parametr1)}")
    cislo_typ = type(parametr1)
    if cislo_typ == int:
        return int(parametr1)
    elif cislo_typ == str:
        text = parametr1
        if ',' in text:
            cislo1 = tuple(text)
            #print(f"Zadané číslo: {parametr1} se převádí jako typ 'tuple'")
        else:
            if '.' in text:
                cislo1 = float(text)
                #print(f"Zadané číslo: {parametr1} se převádí jako typ 'float'")
            else: 
                cislo1 = int(text)
                #print(f"Zadané číslo: {parametr1} se převádí jako typ 'int'")
                return cislo1

def je_prvocislo(cislo):
    cislo_int = urcityp_vrat_pouze_int(cislo)
    if cislo_int != None and cislo_int > 0: 
        celecislo = int(sqrt(cislo) // 1)
        if cislo_int == 1:
            prvocislo_test = False
        else:
            prvocislo_test = True    
        for x in range(2,celecislo+1):
            vypocet=cislo/x
            if vypocet % 1 == 0:
                prvocislo_test = False
        #if prvocislo_test == True: 
        return prvocislo_test
    else:
        print(f"Nebylo zadané celé kladné číslo! Nebudeme určovat, zda je {cislo} prvočíslo.")

def vrat_prvocisla(max):
    seznam_prvocisel = list()
    cislo_max = urcityp_vrat_pouze_int(max)
    if cislo_max != None and cislo_max > 1: 
        for y in range(1, max+1):
            if je_prvocislo(y) == True:
                seznam_prvocisel.append(y)
                #print(f" Cislo {y} je prvocislo = {je_prvocislo(y)}")
        return seznam_prvocisel
    else:
        print(f"Nebylo zadané celé kladné číslo! Nebudeme určovat, zda je {max} prvočíslo.")

    

if __name__ == "__main__":
    #cislo = input("Zadej celé číslo: ")
    a=2.5
    b=16
    c=45,8
    d=-27
    e=-45.8
    f=-48,8
    g='2.5'
    h='28'
    i='45,8'
    j='-27'
    k='-45.8'
    l='-48,8'
    for y in range(1, 102):
        print(f" Cislo {y} je prvocislo = {je_prvocislo(y)}")
    print("--------------------------")
    print(vrat_prvocisla(300))
    
