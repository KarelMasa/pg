# Příklad 1: Práce s podmínkami a cykly
# Zadání:
# Napište funkci `process_numbers`, která přijme seznam celých čísel. 
# Funkce vrátí nový seznam, který obsahuje pouze čísla větší než 5, vynásobená 2.
# Pokud seznam obsahuje číslo 10, ukončete zpracování seznamu a vraťte dosud vytvořený seznam.

def process_numbers(numbers):
    # ZDE NAPIŠTE VÁŠ KÓD
    
    vysledek = []
    
    delka = len(numbers)
   
   
    for i in range(0, delka):
        if numbers[i] >=5:
            if numbers[i] == 10:
                return vysledek
            else:
                vysledek = vysledek.append(numbers[i]*2)
        #if  > 5:
            
        #    pom = pom.append(int(i)*2)
            #vysledek = vysledek.append(pom)
        #    print(pom)  
        #    print(vysledek)
             
    return vysledek



# Pytest testy pro Příklad 1
def test_process_numbers():
    assert process_numbers([1, 6, 3, 10, 8]) == [12]
    assert process_numbers([7, 8, 10, 12]) == [14, 16]
    assert process_numbers([1, 2, 3, 4]) == []
    assert process_numbers([5, 6, 7, 15]) == [12, 14, 30]