from Table import Table

class Main:
    def __init__(self):
        self.table = Table()

    def main(self):
        try:
            value_to_find = int(input("Podaj liczbę całkowitą do wyszukania w tablicy: "))
        except ValueError:
            print("Wprowadzono nieprawidłową wartość. Uruchom program ponownie.")
            return

        index = self.table.Search(value_to_find)

        print("Zawartość tablicy:")
        print(", ".join(map(str, self.table.get_n())))

        if index != -1:
            print(f"Liczba {value_to_find} została znaleziona na indeksie: {index}")
        else:
            print(f"Liczba {value_to_find} nie została znaleziona w tablicy.")


if __name__ == "__main__":
    main_program = Main()
    main_program.main()
