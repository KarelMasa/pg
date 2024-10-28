def urcityp(parametr1):
    #if type(parametr1) == int: print(f"Zadané číslo: {parametr1} je typu INT")
    print(f"Zadané číslo: {parametr1} je typu {type(parametr1)}")
    cislo_typ = type(parametr1)
    if cislo_typ == str:
        text = parametr1
        if ',' in text:
            cislo1 = tuple(text)
            print(f"Zadané číslo: {parametr1} je typu {type(cislo1)}")
        else:
            if '.' in text:
                cislo1 = float(text)
                print(f"Zadané číslo: {parametr1} je typu {type(cislo1)}")
            else: 
                cislo1 = int(text)
                print(f"Zadané číslo: {parametr1} je typu {type(cislo1)}")
    
    

if __name__ == "__main__":
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
    urcityp(a)
    urcityp(b)
    urcityp(c)
    urcityp(d)
    urcityp(e)
    urcityp(f)
    urcityp(g)
    urcityp(h)
    urcityp(i)
    urcityp(j)
    urcityp(k)

