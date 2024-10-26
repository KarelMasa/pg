import time

def vypis_text(text):
    print(f'text je: {text}')
    return 1

if __name__ == "__main__":

    for x in [2,4,8,12,19]:
        print(x)
    maximum = 30
    for x in range(0,maximum+1,5):
        print(x)

#    vstup = input ("Zadej vstup: ")
#    vystup = vypis_text(vstup)