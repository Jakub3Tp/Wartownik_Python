import random


def fill_array(size=50, min_value=1, max_value=100):
    return [random.randint(min_value, max_value) for _ in range(size)]


def search_element(array, value):
    for index, element in enumerate(array):
        if element == value:
            return index
    return -1


def main():
    print("Program do wyszukiwania pierwszego wystąpienia liczby w tablicy.\n")

    array = fill_array()
    print("Tablica została wypełniona losowymi liczbami.\n")

    try:
        value_to_find = int(input("Podaj liczbę całkowitą do wyszukania w tablicy: "))
    except ValueError:
        print("Wprowadzono nieprawidłową wartość. Uruchom program ponownie.")
        return

    index = search_element(array, value_to_find)

    print("\nZawartość tablicy:")
    print(", ".join(map(str, array)))
    if index != -1:
        print(f"\nLiczba {value_to_find} została znaleziona na indeksie: {index}")
    else:
        print(f"\nLiczba {value_to_find} nie została znaleziona w tablicy.")


if __name__ == "__main__":
    main()
