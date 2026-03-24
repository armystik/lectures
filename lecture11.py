class Postava:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.zdravi = 100
        self.hlad = 50
        self.energie = 50

    def stav(self):
        print(f"\n{self.jmeno}")
        print(f"Zdraví: {self.zdravi}")
        print(f"Hlad: {self.hlad}")
        print(f"Energie: {self.energie}")

    def jist(self):
        self.hlad -= 20
        self.zdravi += 10
        print(f"{self.jmeno} se najedl.")

    def spat(self):
        self.energie += 30
        self.hlad += 10
        print(f"{self.jmeno} se vyspal.")

    def pracovat(self):
        self.energie -= 20
        self.hlad += 15
        print(f"{self.jmeno} pracoval.")

    def kontrola(self):
        if self.hlad > 100:
            self.zdravi -= 10
            print(f"{self.jmeno} hladoví!")
        if self.energie <= 0:
            self.zdravi -= 10
            print(f"{self.jmeno} je vyčerpaný!")

 ### Zde zadávat jméno postavy ###

p = Postava("Jakub") # <----

while True:
    p.stav()

    print("\n1 - jíst")
    print("2 - spát")
    print("3 - pracovat")
    print("4 - konec")

    volba = input("Vyber akci: ")

    if volba == "1":
        p.jist()
    elif volba == "2":
        p.spat()
    elif volba == "3":
        p.pracovat()
    elif volba == "4":
        break

    p.kontrola()