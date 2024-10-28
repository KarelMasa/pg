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


#                                                                           Funkce testuje, zda je zadany parametr vhodny pro zjisteni prvocisla. Musi byt cele cislo typu 'int'. 
def urcityp_vrat_pouze_int(parametr1):
    cislo_typ = type(parametr1)
    if cislo_typ == int:
        return int(parametr1)
    elif cislo_typ == str:
        text = parametr1
        pom1 = len(text)
        if pom1 > 0:
            jetocislo = True
            for c in range(0,pom1):
                if text[c] not in {'-','.','0','1','2','3','4','8','6','7','8','9'}: 
                    jetocislo = False
            if jetocislo == True:
                if ',' in text:
                    cislo1 = tuple(text)
                    print(f"Zadané číslo: '{parametr1}' se převádí jako typ 'tuple'")
                else:
                    if '.' in text:
                        cislo1 = float(text)
                
                        print(f"Zadané číslo: '{parametr1}' se převádí jako typ 'float'")
                    else: 
                        cislo1 = int(text)
                        print(f"Zadané číslo: '{parametr1}' se převádí jako typ 'int'")
                    return cislo1
            else:
                cislo1 = str(text)
                print(f"Zadané číslo: '{parametr1}' se převádí jako typ 'str'")


#                                                               Funkce zjistuje, zda je zadane cislo prvocislem. Funkce vraci 2 hodnoty: (cislo, false/true). Pokud vstupni paramet neodpovida pozadavkum, vraci (None, None)
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
        return (cislo_int, prvocislo_test)
    else:
        print(f"Nebylo zadané celé kladné číslo! Nebudeme určovat, zda je '{cislo}' prvočíslo.")
        return (None, None)

#                                                               Funkce vrací seznam prvocisel.Pokud vstupni paramet neodpovida pozadavkum, vraci None
def vrat_prvocisla(max):
    seznam_prvocisel = list()
    cislo_max = urcityp_vrat_pouze_int(max)
    if cislo_max != None and cislo_max > 1: 
        for y in range(1, max+1):
            vratcislo= je_prvocislo(y)
            if vratcislo[1] == True:
                seznam_prvocisel.append(vratcislo[0])
                #print(f" Cislo {y} je prvocislo = {je_prvocislo(y)}")
        return seznam_prvocisel
    else:
        print(f"Mebyla nalezena žádná prvočísla.")
        return None

    

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
    m='--2548.54  test'
    #for y in range(1, 102):
    vracenecislo = je_prvocislo(1)
    if vracenecislo[0] != None:
        print(f" Cislo {vracenecislo[0]} je prvocislo = {vracenecislo[1]}")
        
    print("--------------------------")
    print(f" Seznam prvočísel: {vrat_prvocisla(1)}")
    
