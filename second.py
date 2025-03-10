def cislo_text(cislo):
    cislo_Int = int(cislo)
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    #---------------------------------------------------

    #---------------------------------------------------  Rozdíly ve výslovnosti
    # 
    #   0   nula
    #   100 sto
    #--------------------------------------------------- rozdíly v jednotkách v 11-19 -------------------
    #   11   jedna   jede náct       náct    rozdíl
    #   12   dva     dva náct        náct    ok
    #   13   tři     tři náct        náct    ok
    #   14   čtyři   čtr náct        náct    rozdíl
    #   15   pět     pat náct        náct    rozdíl
    #   16   šest    šest náct       náct    ok
    #   17   sedm    sedm náct       náct    ok
    #   18   osm     osm náct        náct    ok
    #   19   devět   devate náct     náct    rozdíl
    #--------------------------------------------------- rozdíly v desítkách v 20-90 -------------------
    #   10  jedna   de set                      set     rozdíl  - do seznamu jednotek
    #   20  dva     dva cet                     cet     ok
    #   30  tři     tři cet                     cet     ok
    #   40  čtyři   čtyři cet                   cet     ok
    #   50  pět     pa desát                    desát   rozdíl
    #   60  šest    še desát                    desát   rozdíl
    #   70  sedm    sedm desát                  desát   ok
    #   80  osm     osm desát                   desát   ok
    #   90  devět   deva desát                  desát   rozdíl

    # Definice slovniku
    jednotky = {1 : "jedna", 2 : "dva", 3: "tři", 4: "čtyři", 5: "pět", 6:"šest", 7:"sedm", 8:"osm", 9:"devět", 10:"deset"}
    nestandardni = {11:"jede",14: "čtr", 15: "pat",19: "devate", 50: "pa", 60: "še", 90: "deva"}
    koncovka = ""
    
    # Nastaví desítky a jednotky 
    hodnota_jednotky = cislo_Int % 10
    hodnota_desitky = cislo_Int // 10
    hodnota_desitky_nestandardni = cislo_Int - hodnota_jednotky         # pro kontrolu nestandardních desítek

    # Testuje, zda je číslo v rozsahu dle zadání
    if cislo_Int > 100 or cislo_Int < 0:
        return "Zadané číslo není v rozsahu 0 až 100"
    else:
    # Pokud je v rozsahu
    #                       : vypíše text pro 0 a 100     
        if cislo_Int == 0: return "nula"
        if cislo_Int == 100: return "sto"
    #                       : vypíše text pro 1 až 10             
        if cislo_Int > 0 and cislo_Int < 11:
            return jednotky[cislo_Int]
    #                       : vypíše text pro 11 až 19             
        if cislo_Int >10 and cislo_Int < 20:
            koncovka = "náct"
    #   testuje, zda je nestandardní výslovnost. 
            vysledny_text = nestandardni.get(cislo_Int, jednotky.get(hodnota_jednotky))+koncovka
            return vysledny_text 
    #                       : vypíše text pro 21 až 99             
        if cislo_Int >=20 and cislo_Int < 100:
    #   nastaví koncovku pro řád desítek: 20 až 40 = "cet", 50 - 90 = "desát"
            if cislo_Int >=20 and cislo_Int <50: 
                koncovka = "cet" 
            else: 
                koncovka = "desát"
    #   Opět testuje nestandardní výslovnost v řádu desítek. Poskládá text pro desítky a přidá text pro jednotky. 
        vysledny_text = nestandardni.get(hodnota_desitky_nestandardni, jednotky.get(hodnota_desitky))+koncovka+" " + jednotky.get(hodnota_jednotky, "")
        return vysledny_text 


if __name__ == "__main__":

# tento cyklus je jen pro kontrolu, abych nemusel každá čísla zadávat zvlášť
#    for x in range(101):
#        text = cislo_text(x)
#        print(f"Zadané číslo: {x} = {text}")

    cislo = input("Zadej číslo: ")
    text = cislo_text(int(cislo))
    print(f"Zadané číslo: {cislo} = {text}")