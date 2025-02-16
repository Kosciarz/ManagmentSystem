

class Pracownik:
    ilosc_pracownikow = 0

    def __init__(self, imie: str, wiek: int, zawod: str, ID=0):
        Pracownik.ilosc_pracownikow += 1
        self.imie = imie
        self.wiek = wiek
        self.zawod = zawod
        if ID == 0:
            self.id = Pracownik.ilosc_pracownikow
        else:
            self.id = ID