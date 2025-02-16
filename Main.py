from Zaklad import Zaklad


def show_menu() -> None:
    print('''
1. Wyświetl listę pracowników
2. Dodaj nowego pracownika
3. Usuń pracownika
4. Zaktualizuj dane pracownika (imię, wiek, zawód)
5. Opuść program''')

def perform_operation(z: Zaklad, op: int) -> None:
    match op:
        case 1:
            z.wyswietl_pracownikow()
        case 2:
            z.dodaj()
        case 3:
            z.usun()
        case 4:
            z.edytuj_dane()
        case 5:
            exit()
        case _: 
            print("Nieprawna operacja. Spróbuj ponownie\n")


def main():
    z = Zaklad()
    
    while True:
        show_menu()
        try:
            operacja = int(input("Wybierz operacje: "))
            perform_operation(z, operacja)
        except ValueError:
            print("Nieprawna operacja. Spróbuj ponownie\n")


if __name__ == "__main__":
    main()