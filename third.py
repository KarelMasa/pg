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


# Funkce testuje, zda je zadany parametr vhodny pro zjisteni prvocisla. Musi byt cele cislo typu 'int'. pokud odpovida pozadavkum, vrati int, jinak vraci None
def urcityp_vrat_pouze_int(parametr1):
    cislo_typ = type(parametr1)
    if cislo_typ == int:
        return int(parametr1)
    elif cislo_typ == str:
        text = parametr1
        pom1 = len(text)
        if pom1 > 0:
            jetocislo = True
            countminus = 0
            counttecka = 0
            for c in range(0,pom1):
                if text[c] not in {'-','.','0','1','2','3','4','5','6','7','8','9'}: 
                    jetocislo = False
                else:
                    if text[c] == '-': countminus += 1
                    if text[c] == '.': counttecka += 1 
                    if countminus > 1 or counttecka > 1: jetocislo = False

            if jetocislo == True:
                if ',' in text:
                    cislo1 = tuple(text)
                    return None
                    #print(f"Zadané číslo: '{parametr1}' se převádí jako typ 'tuple'")
                elif '.' in text:
                        cislo1 = float(text)
                        #print(f"Zadané číslo: '{parametr1}' se převádí jako typ 'float'")
                        return None
                else:
                    cislo1 = int(text)
                    #print(f"Zadané číslo: '{parametr1}' se převádí jako typ 'int'")
                    return cislo1
            else:
                cislo1 = str(text)
                #print(f"Zadané číslo: '{parametr1}' se převádí jako typ 'str'")
                return None


# Funkce zjistuje, zda je zadane cislo prvocislem. Funkce vraci: (false/true). Pokud vstupni paramet neodpovida pozadavkum, vraci None
def je_prvocislo(cislo):
    cislo_int = urcityp_vrat_pouze_int(cislo)
    if cislo_int != None and cislo_int > 0: 
        celecislo = int(sqrt(cislo_int) // 1)
        if cislo_int == 1:
            prvocislo_test = False
        else:
            prvocislo_test = True    
        for x in range(2,celecislo+1):
            vypocet=cislo_int/x
            if vypocet % 1 == 0:
                prvocislo_test = False
        return prvocislo_test
    else:
        print(f"Nebylo zadané celé kladné číslo! Nebudeme určovat, zda je '{cislo}' prvočíslo.")
        return None

# Funkce vrací seznam prvocisel.Pokud vstupni paramet neodpovida pozadavkum, vraci None
def vrat_prvocisla(max):
    seznam_prvocisel = list()
    cislo_max = urcityp_vrat_pouze_int(max)
    if cislo_max != None and cislo_max > 1: 
        for y in range(1, cislo_max+1):
            vratcislo= je_prvocislo(y)
            if vratcislo == True:
                seznam_prvocisel.append(y)
        return seznam_prvocisel
    else:
        print(f"Mebyla nalezena žádná prvočísla.")
        return None

    

if __name__ == "__main__":
    zadej = input("Zadej číslo: ")
    vracenecislo = je_prvocislo(zadej)
    if vracenecislo != None:
        print(f" Cislo {zadej} je prvocislo = {vracenecislo}")
    print("--------------------------")
    print(f" Seznam prvočísel rozsahu 1 až {zadej}: {vrat_prvocisla(zadej)}")
    
