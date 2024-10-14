def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    #---------------------------------------------------

    #---------------------------------------------------  Rozdíly ve skloňování
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
    hodnota_jednotky = cislo % 10
    hodnota_desitky = cislo // 10
    hodnota_desitky_nestandardni = cislo - hodnota_jednotky         # pro kontrolu nestandardních desítek

    # Testuje, zda je číslo v rozsahu dle zadání
    if cislo > 100 or cislo < 0:
        return "Zadané číslo není v rozsahu 0 až 100"
    else:
    
    # Pokud je v rozsahu
    #                       : vypíše text pro 0 a 100     
        if cislo == 0: return "nula"
        if cislo == 100: return "sto"

    #                       : vypíše text pro 1 až 10             
        if cislo > 0 and cislo < 11:
            return jednotky[cislo]
        
    #                       : vypíše text pro 11 až 19             
        if cislo >10 and cislo < 20:
            koncovka = "náct"
    
    #   testuje, zda je nestandardní skloňování. Pokud ano, vypíše základ z proměnné "nestandardni" a doplní "koncovka", jinak vypíše "jednotky" a doplní koncovku
    #   př. pro číslo 14: vypíše z "nestandardni" podle hodnoty klíče "čtr" + doplní "náct" = čtrnáct
    #   př. pro číslo 18: vypíše z "jednotky" podle hodnoty klíče "osm" + doplní "náct" = osmnáct
            vysledny_text = nestandardni.get(cislo, jednotky.get(hodnota_jednotky))+koncovka
            return vysledny_text 
        
    #                       : vypíše text pro 21 až 99             
        if cislo >=20 and cislo < 100:
    
    #   nastaví koncovku pro řád desítek: 20 až 40 = "cet", 50 - 90 = "desát"
            if cislo >=20 and cislo <50: 
                koncovka = "cet" 
            else: 
                koncovka = "desát"
    
    #   Opět testuje nestandardní skloňování v řádu desítek. Poskládá text pro desítky a přidá text pro jednotky. 
    #   Pokud se jednotky = 0 (např u čísla 40), vrátí za jednotky prázdný řetězec.
        vysledny_text = nestandardni.get(hodnota_desitky_nestandardni, jednotky.get(hodnota_desitky))+koncovka+" " + jednotky.get(hodnota_jednotky, "")
        return vysledny_text 


if __name__ == "__main__":

# tento cyklus je jen pro kontrolu, abych nemusel každá čísla zadávat uvlášť
#    for x in range(101):
#        text = cislo_text(x)
#        print(f"Zadané číslo: {x} = {text}")

    cislo = input("Zadej číslo: ")
    text = cislo_text(int(cislo))
    print(f"Zadané číslo: {cislo} = {text}")
