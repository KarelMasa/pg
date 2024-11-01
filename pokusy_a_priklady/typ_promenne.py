def urcityp_vrat_pouze_int(parametr1):
    #if type(parametr1) == int: print(f"Zadané číslo: {parametr1} je typu INT")
    print(f"Zadané číslo: {parametr1} je typu {type(parametr1)}")
    cislo_typ = type(parametr1)
    if cislo_typ == int:
        return int(parametr1)
    elif cislo_typ == str:
        text = parametr1
        if ',' in text:
            cislo1 = tuple(text)
            print(f"Zadané číslo: {parametr1} se převádí jako typ 'tuple'")
        else:
            if '.' in text:
                cislo1 = float(text)
                print(f"Zadané číslo: {parametr1} se převádí jako typ 'float'")
            else: 
                cislo1 = int(text)
                print(f"Zadané číslo: {parametr1} se převádí jako typ 'int'")
                return cislo1
    
    

if __name__ == "__main__":
    hodnota = None
    a=2.5
    b=28
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
    #urcityp(j)
    print("---------------------------------")
    hodnota = urcityp_vrat_pouze_int(b)
    print(hodnota)

"""    
    hodnota = urcityp_vrat_pouze_int(b)
    hodnota = urcityp_vrat_pouze_int(c)
    hodnota = urcityp_vrat_pouze_int(d)
    hodnota = urcityp_vrat_pouze_int(e)
    hodnota = urcityp_vrat_pouze_int(f)
    hodnota = urcityp_vrat_pouze_int(g)
    hodnota = urcityp_vrat_pouze_int(h)
    hodnota = urcityp_vrat_pouze_int(i)
    hodnota = urcityp_vrat_pouze_int(j)
    hodnota = urcityp_vrat_pouze_int(k)
"""

