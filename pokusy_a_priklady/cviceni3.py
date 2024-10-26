def faktorial(n):
    if n==1:
        return 1
    else:
        return n* faktorial(n-1)
    
def faktorial_for(n):
    vysledek = 1
    # for
    for x in range(1,n+1):
        vysledek=vysledek*(x)
    return vysledek

def faktorial_while(n):
    vysledek = 1
    while n > 0:
        vysledek = vysledek * n
        n -=1 
    return vysledek

if __name__ == "__main__":
    vysl = faktorial_for(5)
    print(vysl)
    vysl = faktorial_while(5)
    print(vysl)
    
