import time
x=0     # na tomto místě jako globální proměnná


def vypis_text(text):
    print(f'text je: {text}')
    return 1

def proved_operaci(*cisla):
    vysledek = 0
    for c in cisla:
        vysledek += c
    return vysledek

if __name__ == "__main__":

    for x in [2,4,8,12,19]:
        print(x)
    maximum = 30
    for x in range(0,maximum+1,5):
        print(x)

    seznam = ["AAA", "BBB", "CCC", "DDD"]
    for index, hondota in enumerate(seznam):
        print(f"Index:  {index}  je  {hondota}")

    x = proved_operaci(1, 2, 3, 4, 5)
    print(x)

    seznam = [1,2,3,4,5]
    print(list(map(lambda x: x**2, seznam)))
#    vstup = input ("Zadej vstup: ")
#    vystup = vypis_text(vstup)