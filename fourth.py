"""
#   DULEZITA POZNAMKA - dle zadani v prikladu jsou souradnice pozic prehozene (y,x) vuci zazitemu standardu (x,y)   !!!!!!!!!!!!
# !!!!!!!!!!!!!!        Dopsána funkce na prohození souřadnic z (y,x) na (y,x)
"""

sachovnice_x = (1,2,3,4,5,6,7,8) # sloupec
sachovnice_y = (1,2,3,4,5,6,7,8) # řádek

# pravidlo_tahu = (0- pozice, 1- vlevo, 2- vpravo, 3- nahoru, 4- dolu, 5- l_na, 6- p_na, 7- l_do, 8- p_do, 9- pouze_o_1_pole = True/False, 10 - je prvni tah specificky = True/False)
# pravidlo_tahu = {0:None, 1: None, 2: None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9: None, 10: None }

#                                                           prohodi souradnice ze zadani (y,x) na pouzivane (x,y)   -- pouze specifikum pro tento ukol

def tah_mimo_sachovnici(cilova_pozice):
    if cilova_pozice[0] not in sachovnice_x or cilova_pozice[1] not in sachovnice_y:
        return False
    else: return True

def obsazena_pozice(cilova_pozice, obsazene_pozice):
    if cilova_pozice in obsazene_pozice:
        return True
    else: return False

#   Určí směr tahu fygurky pro další výpočty - vrací směr tahu
def urci_smer_tahu(p_pozice, c_pozice):
    # vlevo, vpravo, nahoru, dolu, l_na, p_na, l_do, p_do   x, y
    if p_pozice[0] == c_pozice[0] and p_pozice[1] == c_pozice[1]: smer_tahu_cislo = None # "Zustava na místě"
    else:
        if p_pozice[0] == c_pozice[0]:  # osa X = řádek
            if p_pozice[1] > c_pozice[1]: smer_tahu_cislo = 4     #dolu
            elif p_pozice[1] < c_pozice[1]: smer_tahu_cislo = 3     #nahoru
        elif p_pozice[1] == c_pozice[1]:  # osa Y = sloupec
            if p_pozice[0] > c_pozice[0]: smer_tahu_cislo = 1     #vlevo
            elif p_pozice[0] < c_pozice[0]: smer_tahu_cislo = 2     #vpravo
        elif p_pozice[1] < c_pozice[1]:  # nahoru 
            if p_pozice[0] > c_pozice[0]: smer_tahu_cislo = 5     # vlevo
            elif p_pozice[0] < c_pozice[0]: smer_tahu_cislo = 6     # vpravo
        elif p_pozice[1] > c_pozice[1]:  # dolu
            if p_pozice[0] > c_pozice[0]: smer_tahu_cislo = 7     # vlevo
            elif p_pozice[0] < c_pozice[0]: smer_tahu_cislo = 8     #vpravo
    # vrací číselné označení směru (0- pozice, 1- vlevo, 2- vpravo, 3- nahoru, 4- dolu, 5- l_na, 6- p_na, 7- l_do, 8- p_do, 9- pouze_o_1_pole = True/False)
    return (smer_tahu_cislo)

#                                                   Určí, zda je cílová souřadnice vůči počáteční v rámci pravidel tahu
def urci_spravnost_tahu_podle_pravidel(f_typ,f_pozice, c_pozice, smer, o1pole, tah1):
    if f_typ == 'pěšec':
        if f_pozice[0] == 2 and tah1 == True and (c_pozice[1]-f_pozice[1]<= 2): return True
        elif (f_pozice[0] + smer[0] == c_pozice[0]) and (f_pozice[1] + smer[1] == c_pozice[1]): return True
        else: return False
    elif f_typ == 'jezdec':
        if (f_pozice[0] + smer[0] == c_pozice[0]) and (f_pozice[1] + smer[1] == c_pozice[1]): return True
        else: return False
    # diagonalne
    if (f_pozice[0] != c_pozice[0]) and (f_pozice[1] != c_pozice[1]):
        if o1pole == True:
            if (f_pozice[0] + smer[0] == c_pozice[0]) and (f_pozice[1] + smer[1] == c_pozice[1]): return True 
            else: return False
        else:
            if abs(f_pozice[0] - c_pozice[0]) == abs(f_pozice[1] - c_pozice[1]): return True
            else: return False
    # horizontalne
    if (f_pozice[0] == c_pozice[0]) or (f_pozice[1] == c_pozice[1]):
        if o1pole == True:
#           Tah o 1 pole 
            if (f_pozice[0] + smer[0] == c_pozice[0]) and (f_pozice[1] + smer[1] == c_pozice[1]): return True 
            else: return False
        else:
#           Tah o více polí 
            px1 = abs(f_pozice[0]-c_pozice[0])
            py1 = abs(f_pozice[1]-c_pozice[1])
            if px1> py1: rozdil= px1 
            else: rozdil = py1
            if (f_pozice[0] + rozdil*smer[0] == c_pozice[0]) and (f_pozice[1] + rozdil*smer[1] == c_pozice[1]): return True
            else: return False

#    zda je nejaka figurka v ceste a brani pohybo na cilove souradnice
def figurka_v_ceste(f_typ, f_pozice, c_pozice,o_pozice, smer): 
    if f_typ == 'pěšec':
        if f_pozice[1] == 2:
            if (f_pozice[0]+smer[0],f_pozice[1]+smer[1]) in o_pozice : return True 
            else: return False
        else: return False

    elif f_typ == 'jezdec': return False

    # diagonalne
    if (f_pozice[0] != c_pozice[0]) and (f_pozice[1] != c_pozice[1]):
        if abs(f_pozice[0] - c_pozice[0]) == abs(f_pozice[1] - c_pozice[1]): 
            p = abs(f_pozice[0] - c_pozice[0])
            for i in range(1, p+1):
                if (f_pozice[0]+ i*smer[0],f_pozice[1]+ i*smer[1]) in o_pozice: return True
        else: return False
    # horizontalne
    if (f_pozice[0] == c_pozice[0]) or (f_pozice[1] == c_pozice[1]):
        px1 = abs(f_pozice[0]-c_pozice[0])
        py1 = abs(f_pozice[1]-c_pozice[1])
        if px1> py1: rozdil= px1 
        else: rozdil = py1
        for i in range(1,rozdil+1):
            px1 = i*smer[0]
            py1 = i*smer[1]
            pp=(px1, py1)
            if (f_pozice[0]+ px1,f_pozice[1]+ py1) in o_pozice: return True
        else: return False

#   Prehodi souradnice (y,x) na (x,y) a vrati upravene hodnoty - pouze pro tento ukol
def uprav_souradnice(fig, cilpoz, obspoz):
    fig1 = fig
    x=fig["pozice"][1]
    y=fig["pozice"][0]
    fig1['pozice'] = (x,y)
    x= cilpoz[1]   
    y= cilpoz[0]
    cilpoz1 = (x,y)
    obspoz1 = set({})
    for i in obspoz:
        x=i[1]
        y=i[0]
        obspoz1.add((x,y))
    return fig1, cilpoz1, obspoz1


def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
#    Prevede zadane souradnice z (y,x) na (x,y) a ulozi do pomocnych promennych - pouze pro tento ukol
    figurka1, cilova_pozice1, obsazene_pozice1 = uprav_souradnice(figurka,cilova_pozice, obsazene_pozice)
    if tah_mimo_sachovnici(cilova_pozice1) == False: return False
    else:
        if obsazena_pozice(cilova_pozice1, obsazene_pozice1) == True: return False
        """
        Ověří, zda se figurka může přesunout na danou pozici.

        :param figurka: Slovník s informacemi o figurce (typ, pozice).
        :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
        :param obsazene_pozice: Množina obsazených pozic na šachovnici.
        :return: True, pokud je tah možný, jinak False.
        """
    # Implementace pravidel pohybu pro různé figury zde.
    # pravidlo_tahu = (pozice, vlevo, vpravo, nahoru, dolu, l_na, p_na, l_do, p_do, pouze_o_1_pole = True/False, specificky_prvni_tah = True/False)
        if figurka1['typ'] == 'pěšec':
            pravidlo_tahu = (figurka1['pozice'], (0,0), (0,0), (0,1), (0,0), (0,0), (0,0), (0,0), (0,0), True, True)
    #        if figurka1['pozice'][0]>2: pravidlo_tahu[10] = False
        elif figurka1['typ'] == 'jezdec':
            pravidlo_tahu = (figurka1['pozice'], (0,0), (0,0), (0,0), (0,0), (-1,2), (1,2), (-1,-2), (1,-2), False, False)
        elif figurka1['typ'] == 'věž':
            pravidlo_tahu = (figurka1['pozice'], (-1,0), (1,0), (0,1), (0,-1), (0,0), (0,0), (0,0), (0,0), False, True)
        elif figurka1["typ"] == 'střelec':
            pravidlo_tahu = (figurka1['pozice'], (0,0), (0,0), (0,0), (0,0), (-1,1), (1,1), (-1,-1), (1,-1), False, False)
        elif figurka1['typ'] == 'dáma':
            pravidlo_tahu = (figurka1['pozice'], (-1,0), (1,0), (0,1), (0,-1), (-1,1), (1,1), (-1,-1), (1,-1), False, False)
        elif figurka1['typ'] == 'král':
            pravidlo_tahu = (figurka1['pozice'], (-1,0), (1,0), (0,1), (0,-1), (-1,1), (1,1), (-1,-1), (1,-1), True, True)
        pravidlo_tahu = list(pravidlo_tahu)
        smer_tahu_figurky = urci_smer_tahu(figurka1["pozice"],cilova_pozice1)
        # pokud je dle pravidel tahu figurky označení směru (0,0), figurka tímto směrem táhnout nemůže
        if pravidlo_tahu[smer_tahu_figurky] == (0,0) or smer_tahu_figurky == None: 
            return False 
        elif urci_spravnost_tahu_podle_pravidel(figurka1["typ"], figurka1["pozice"], cilova_pozice1, pravidlo_tahu[smer_tahu_figurky], pravidlo_tahu[9], pravidlo_tahu[10]) == False: return False 
        else:
            if figurka_v_ceste(figurka1["typ"], figurka1["pozice"], cilova_pozice1, obsazene_pozice1, pravidlo_tahu[smer_tahu_figurky] ) == True: return False 
            return True


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}                          
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat
    print(je_tah_mozny(pesec, (3, 4), obsazene_pozice))  # False, protože pěšec nemůže couvat
    print("*********************")
    print(je_tah_mozny({'typ': 'pěšec', 'pozice': (2, 4)}, (3, 4), {(2, 4), (8, 2), (3, 3), (5, 4), (8, 6), (8, 8), (6, 3), (1, 4)}))
    print("*********************")
    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici
    print(je_tah_mozny(jezdec, (1, 1), obsazene_pozice))  # False, tah je mimo pravidla pohybu jezdce

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
    print(je_tah_mozny(dama, (6, 5), obsazene_pozice))  # True
    print(je_tah_mozny(dama, (3, 7), obsazene_pozice))  # False, tah je mimo pravidla pohybu dámy

    print(je_tah_mozny(vez, (3, 8), obsazene_pozice))  # True
    print(je_tah_mozny(vez, (8, 1), obsazene_pozice))  # False, figurka v cestě
    print(je_tah_mozny(vez, (4, 7), obsazene_pozice))  # False, tah je mimo pravidla pohybu věže
    print(je_tah_mozny(vez, (1, 8), obsazene_pozice))  # True
    print(je_tah_mozny(vez, (9, 8), obsazene_pozice))  # False, tah mimo šachovnici

    print(je_tah_mozny(strelec, (3, 6), obsazene_pozice))  # False, figurka v cestě
    print(je_tah_mozny(strelec, (7, 1), obsazene_pozice))  # False, tah je mimo pravidla pohybu střelce
    print(je_tah_mozny(strelec, (8, 5), obsazene_pozice))  # True
    print(je_tah_mozny(strelec, (8, 1), obsazene_pozice))  # False, figurka v cestě
    print(je_tah_mozny(strelec, (9, 1), obsazene_pozice))  # False, tah mimo šachovnici

    print(je_tah_mozny(kral, (1, 2), obsazene_pozice))  # False, král může táhnout pouze o 1
    print(je_tah_mozny(kral, (3, 1), obsazene_pozice))  # True
    print(je_tah_mozny(kral, (2, 7), obsazene_pozice))  # False, tah mimo pravidla pohybu krále
    print(je_tah_mozny(kral, (5, 2), obsazene_pozice))  # True
    print(je_tah_mozny(kral, (6, 9), obsazene_pozice))  # False, tah mimo šachovnici
