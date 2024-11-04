"""#   DULEZITA POZNAMKA - dle zadani v prikladu jsou souradnice pozic prehozene (y,x) vuci zazitemu standardu (x,y)   !!!!!!!!!!!!
#   Prvotne programovano na zaklade zazitich parametru (x,y)
# !!!!!!!!!!!!!!        Bud upravit veskere funkce a vypocty -- prehodit parametry na (y,x)
# !!!!!!!!!!!!!!        Nebo ve funkcich dopsat prohozeni parametru (x,y) za (y,x)
"""

sachovnice_x = (1,2,3,4,5,6,7,8) # sloupec
sachovnice_y = (1,2,3,4,5,6,7,8) # řádek
souradnice_prohozene = False
# x = označuje sloupec, y řadu

# pravidlo_tahu = (0- pozice, 1- vlevo, 2- vpravo, 3- nahoru, 4- dolu, 5- l_na, 6- p_na, 7- l_do, 8- p_do, 9- pouze_o_1_pole = True/False, 10 - je prvni tah specificky = True/False)
pravidlo_tahu = {0:None, 1: None, 2: None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9: None, 10: None }

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
    smer_tahu="Zustava"
    smer_tahu_cislo = None
    # vlevo, vpravo, nahoru, dolu, l_na, p_na, l_do, p_do   x, y
    if p_pozice[0] == c_pozice[0] and p_pozice[1] == c_pozice[1]: smer_tahu="Zustava"
    else:
        if p_pozice[0] == c_pozice[0]:  # osa X = řádek
            if p_pozice[1] > c_pozice[1]:
                smer_tahu="dolu"
                smer_tahu_cislo = 4
                #print(smer_tahu)
            elif p_pozice[1] < c_pozice[1]:
                smer_tahu="nahoru"
                smer_tahu_cislo = 3
                #print(smer_tahu)
        elif p_pozice[1] == c_pozice[1]:  # osa Y = sloupec
            if p_pozice[0] > c_pozice[0]:
                smer_tahu="vlevo"
                smer_tahu_cislo = 1
                #print(smer_tahu)
            elif p_pozice[0] < c_pozice[0]:
                smer_tahu="vpravo"
                smer_tahu_cislo = 2
                #print(smer_tahu)
        elif p_pozice[1] < c_pozice[1]:  # nahoru 
            if p_pozice[0] > c_pozice[0]:
                smer_tahu="l_na"        # vlevo
                smer_tahu_cislo = 5
            elif p_pozice[0] < c_pozice[0]:
                smer_tahu="p_na"        # vpravo
                smer_tahu_cislo = 6
        elif p_pozice[1] > c_pozice[1]:  # dolu
            if p_pozice[0] > c_pozice[0]:
                smer_tahu="l_na"        # vlevo
                smer_tahu_cislo = 7
            elif p_pozice[0] < c_pozice[0]:
                smer_tahu="p_na"        #vpravo
                smer_tahu_cislo = 8



    # vrací "text - směr tahu" a číselné označení směru (0- pozice, 1- vlevo, 2- vpravo, 3- nahoru, 4- dolu, 5- l_na, 6- p_na, 7- l_do, 8- p_do, 9- pouze_o_1_pole = True/False)
    return (smer_tahu, smer_tahu_cislo)

#   DOPSAT funkce

#                                                   Určí, zda je cílová souřadnice vůči počáteční v rámci pravidel tahu
def urci_spravnost_tahu_podle_pravidel(f_typ,f_pozice, c_pozice, smer, o1pole, tah1):
    if f_typ == 'pěšec':
        if f_pozice[0] == 2 and tah1 == True and (c_pozice[1]-f_pozice[1]<= 2): return True
        elif (f_pozice[0] + smer[0] == c_pozice[0]) and (f_pozice[1] + smer[1] == c_pozice[1]): return True
        else: return False
    elif f_typ == 'jezdec':
        print("jezdec - doplnit")
    elif o1pole == True:
        if (f_pozice[0] + smer[0] == c_pozice[0]) and (f_pozice[1] + smer[1] == c_pozice[1]): return True 
        else: return False
    else:
        if abs(f_pozice[0] - c_pozice[0]) == abs(f_pozice[1] - c_pozice[1]): return True
        else: return False


    #
    #
    #return True

#   DOPSAT - bude testovat, zda je nejaka figurka v ceste a brani pohybo na cilove souradnice
def figurka_v_ceste(figurka, pocatecni_pozice, cilova_pozice,obsazena_pozice, tah_vypocet, o1pole, prvni_tah_sp):
    if cilova_pozice in obsazena_pozice:
        return True
    else: return False

#   Prehodi souradnice (y,x) na (x,y) a vrati upravene hodnoty - pouze pro tento ukol
def uprav_souradnice(fig, cilpoz, obspoz):
    fig1 = fig
    #x=0
    #y=0
    x=fig["pozice"][1]
    y=fig["pozice"][0]
    fig1['pozice'] = (x,y)
    x= cilpoz[1]   
    y= cilpoz[0]
    cilpoz1 = (x,y)
    print(fig1)
    print(cilpoz1)
    obspoz1 = set({})
    for i in obspoz:
        x=i[1]
        y=i[0]
        obspoz1.add((x,y))
    print(obspoz)
    print(obspoz1)
    return fig1, cilpoz1, obspoz1




def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
#    Prevede zadane souradnice z (y,x) na (x,y) a ulozi do pomocnych promennych - pouze pro tento ukol
    figurka1, cilova_pozice1, obsazene_pozice1 = uprav_souradnice(figurka,cilova_pozice, obsazene_pozice)
    test_cil = tah_mimo_sachovnici(cilova_pozice1)
    test_obsazeni = obsazena_pozice(cilova_pozice1, obsazene_pozice1)
    if test_cil == False:
        print("Cil je mimo sachovnici")
        return False
    else:
        if test_obsazeni == True:
            print("Cilova pozice je obsazena")
            return False

        else:
            #print("cil je: ", test_cil)
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
            if figurka1['pozice'][0]>2: pravidlo_tahu[10] = False
        elif figurka1['typ'] == 'jezdec':
            pravidlo_tahu = (figurka1['pozice'], (0,0), (0,0), (0,0), (0,0), (-2,1), (2,1), (-2,-1), (2,-1), False, False)
        elif figurka1['typ'] == 'věž':
            pravidlo_tahu = (figurka1['pozice'], (-1,0), (1,0), (0,1), (0,-1), (0,0), (0,0), (0,0), (0,0), False, True)
        elif figurka1["typ"] == 'střelec':
            pravidlo_tahu = (figurka1['pozice'], (0,0), (0,0), (0,0), (0,0), (-1,1), (1,1), (-1,-1), (1,-1), False, False)
        elif figurka1['typ'] == 'dáma':
            pravidlo_tahu = (figurka1['pozice'], (-1,0), (1,0), (0,1), (0,-1), (-1,1), (1,1), (-1,-1), (1,-1), False, False)
        elif figurka1['typ'] == 'král':
            pravidlo_tahu = (figurka1['pozice'], (-1,0), (1,0), (0,1), (0,-1), (-1,1), (1,1), (-1,-1), (1,-1), True, True)

        smer_tahu_figurky = urci_smer_tahu(figurka1["pozice"],cilova_pozice1)
        print(f"{figurka1['typ']} je na pozici {figurka1['pozice']} a táhne na {cilova_pozice1}. Směr tahu figurky je: {smer_tahu_figurky[0]}. Pro počty se bude brát: {pravidlo_tahu[smer_tahu_figurky[1]]}, figurka se může pohybovat pouze o 1 pole: {pravidlo_tahu[9]}, specifikum prvního tahu: {pravidlo_tahu[10]} ") 

        # pokud je dle pravidel tahu figurky označení směru (0,0), figurka tímto směrem táhnout nemůže
        if pravidlo_tahu[smer_tahu_figurky[1]] == (0,0): 
            return False 
        elif urci_spravnost_tahu_podle_pravidel(figurka1["typ"], figurka1["pozice"], cilova_pozice1, pravidlo_tahu[smer_tahu_figurky[1]], pravidlo_tahu[9], pravidlo_tahu[10]) == False: return False 
        else:
            figurka_v_ceste(figurka1["typ"], figurka1["pozice"], cilova_pozice1, obsazene_pozice1, pravidlo_tahu[smer_tahu_figurky[1]], pravidlo_tahu[9], pravidlo_tahu[10] )
            return True
    
    #
    #


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}                          #   odzkoušeno - asi OK
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    

#    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
#    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
#    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
#    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat
#    print(je_tah_mozny(pesec, (3, 4), obsazene_pozice))  # False, protože pěšec nemůže couvat

    #print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    #print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    #print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    #print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

#    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    #print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
