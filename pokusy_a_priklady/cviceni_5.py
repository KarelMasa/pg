
class Zvire:
    def __init__(self, Jmeno):
        self.jmeno = Jmeno
        print(f"Zvire {self.jmeno} bylo vytvroreno")

class Pes(Zvire):
    def __init__(self, Jmeno, rasa):
        super().__init__(Jmeno)
        self.rasa = rasa
        print(f"Pes rasy {self.rasa} bylo vytvroreno")

if __name__ == "__main__":
    #test
    pes = Pes("Alik", "jezevcik")
    #pes.jmeno
