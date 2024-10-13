def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    return "dvacet pět"

if __name__ == "__main__":
    nestandardni = {0 : "nula", 11:"jedenáct"}
    jednotky = {1 : "jedna", 2 : "dva", 3: "tři", 4: "čtyři", 5: "pět", 6:"šest", 7:"sedm", 8:"osm", 9:"devět", 10:"deset"}
    desitky = {}

    #cislo = input("Zadej číslo: ")
    #text = cislo_text(cislo)
    text = jednotky[11]
    print(text)