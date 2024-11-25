
def zapis_soubor(jmeno_souboru):
    fp = open(jmeno_souboru, "w")
    fp.write("ahoj Vsichni!\n")        #\t - tabulátor, n\ - konec řádku
    fp.write("ahoj Ostatni!\n")
    fp.close

def precti_soubor(jmeno_souboru):
        with open(jmeno_souboru, "r") as fp:
             data = fp.read()
             print(data)
             fp.seek(0)
             for line in fp:
                  line = line.strip()
                  print(line)
                  


if __name__ == "__main__":
    """    
    fp = open("data.txt", "w")
    fp.write("ahoj Vsichni!\n")        #\t - tabulátor, n\ - konec řádku
    fp.write("ahoj Ostatni!\n")
    fp.close"""
    zapis_soubor("data.txt")
    precti_soubor("data.txt")