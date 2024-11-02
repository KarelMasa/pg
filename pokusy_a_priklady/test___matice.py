# pro osobni vyzkouseni a procviceni prace s maticemi

def zadej_obsazene_pozice_do_sachovnice(obsazeno):
    obs = list(obsazeno)
    
    for i in range(0, len(obs)):
        sour[(obs[i][0])-1][(obs[i][1])-1] = "x"
        """        ff=obs[i]
        fx=int(ff[0])-1
        fy=int(ff[1])-1
        """ 
        #sour[ff[0]-1][ff[1]-1] = "x"
    
    print(f" {obs}")
    #print(ff)

if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    sachovnice_x = (1,2,3,4,5,6,7,8) # sloupec
    sachovnice_y = (1,2,3,4,5,6,7,8) # řádek
    y_obsazeno = (sachovnice_y[0], False)
    y_obsazeno2 = (sachovnice_y[1], False)
    obsazeno = []
    y3= []
    sach = []
    sach2 = []
    y4 = []
    y5 = []
    ostatni = False
    ostatni2 = []
    ostatni3 = []
    
    sour = []
    for i in range(8):
        sloupec = []
        for j in range(8):
            sloupec.append(0)
        sour.append(sloupec)    
    zadej_obsazene_pozice_do_sachovnice(obsazene_pozice)
    
    for p in sachovnice_y:
        ostatni2.append(ostatni)
    for p in sachovnice_x:    
        ostatni3.append(ostatni2)

    for p in sachovnice_y:
        y4.append((p,False))

    for p in sachovnice_y:
        y3.append(p)


    #for p in sachovnice_x:
     #   sach.append((p,y3) )

    sach2.append((1,y3))
    sach3=[] #{}
    sach3.append((1,y4))
    
    test1 = [[1,y_obsazeno], [2, y_obsazeno2]]

    test2 = ((1, (sachovnice_y, False)))

    #print(test2)
    #print(test2[1])
    print(f"Y3 = {y3}")
    #print(sach)
    #print(sach[0])

    #print(sach2)
    #print(sach2[0][1][2])

    #print("")
    #print(sach3)

    #print(sach3[0][1][3][1])

    #sach3[0][1][3] = (sach3[0][1][3][0],True)

    #print(sach3)

    sour[1][1] = "X"

    """print(ostatni3)
    print(ostatni3[0][1])
    print(ostatni3[0][7][1])
    ostatni3[0][0][2] = True
    print(ostatni3[0][7][1])
    print(ostatni3[1])"""
    #ostatni3[0][2] = True
    sloupce = len(sour)
    radky = 0
    text = ""
    
    print(f" osa y |")
    if sloupce:
        radky = len(sour[0])
    for j in range(radky):
        
        for i in range(sloupce):
            #print(sour[i][j], end=" ")
            text = text+str(sour[i][j])+" "
        print("  ",j+1,"  |",text)
        text=""    
    print(f"        ---------------- osa x |")
    print(f"         1 2 3 4 5 6 7 8 osa x |")
"""kinosaly = []

for i in range(5):
    kinosal = []
    for j in range(5):
        temp = []
        for k in range(5):
            temp.append(0)
        kinosal.append(temp)
    kinosaly.append(kinosal)

print(kinosaly)
"""





    

    #print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    #print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    #print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    #print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    #print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    #print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    #print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    #print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    #print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    #print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    #print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True