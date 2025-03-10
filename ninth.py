def dec_to_bin(cislo):
    # funkce prevede cislo na binarni reprezentaci (cislo muze byt str i int!!!)
    # 7 -> "111"
    # 5 -> "101"
    cislo = int(cislo)
    if cislo == 0:
        return "0"
    vysledek = ""
    while cislo > 0:
        vysledek = str(cislo % 2) + vysledek  # zbytek po deleni je 1 nebo 0
        cislo = cislo // 2
    return vysledek

def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"


if __name__ == "__main__":
    print(dec_to_bin(1))
    print(dec_to_bin(1354))
    print(dec_to_bin("2541"))
    print(dec_to_bin("3246"))
    print(dec_to_bin("127"))