from Pracownik import Pracownik

import json


def serialize() -> None:
    with open("pracownicy.json", "w") as file:
        json.dump([obj.__dict__ for obj in Zaklad.pracownicy], file, indent=4)


class Zaklad:
    pracownicy: Pracownik = []

    def wyswietl_pracownikow(self) -> None:
        with open("pracownicy.json", "r") as file:
            try:
                del Zaklad.pracownicy[:]
                dane = json.load(file)
                for val in dane:
                    Zaklad.pracownicy.append(Pracownik(val['imie'], val['wiek'], val['zawod'], val['id']))

                print("\nLista pracowników:")
                if len(Zaklad.pracownicy) == 0:
                    print("Brak pracowników.")
                else:
                    for i, pracownik in enumerate(Zaklad.pracownicy):
                        print(
                            f"{i + 1}. {pracownik.imie}, lat: {pracownik.wiek}, zawód: {pracownik.zawod}, "
                            f"ID: {pracownik.id}"
                        )
            except json.decoder.JSONDecodeError:
                print("Brak pracowników.")

    def dodaj(self) -> None:
        imie = input("\nPodaj imie: ")
        zawod = input("Podaj zawod: ")
        wiek = input("Podaj wiek: ")
        Zaklad.pracownicy.append(Pracownik(imie, zawod, wiek))
        serialize()

    def usun(self) -> None:
        self.wyswietl_pracownikow()
        id_pracownika = int(input("Podaj ID pracownika, który ma zostać usunięty: "))

        index: int = -1
        for i, pracownik in enumerate(Zaklad.pracownicy):
            if pracownik.id == id_pracownika:
                index = i

        if index != -1:
            Zaklad.pracownicy.pop(index)

        serialize()

    def edytuj_dane(self) -> None:
        self.wyswietl_pracownikow()
        id_pracownika = int(input("Podaj ID pracownika, którego dane chcesz edytować: "))
        imie = input("Podaj imie: ")
        zawod = input("Podaj zawod: ")
        wiek = input("Podaj wiek: ")

        for pracownik in Zaklad.pracownicy:
            if pracownik.id == id_pracownika:
                pracownik.imie = imie
                pracownik.zawod = zawod
                pracownik.wiek = wiek

        serialize()
