import copy     # Do wykonania "twardej kopii" - lista bez naśladowania operacji
import random


# Funkcja wyszukująca potrzebne liczby pierwsze (od najmniejszej możliwej, któ©a będzie potrzebna do największej)
def primes(tab_max, tab_min):
    prime_nums = []
    for i in range(2 * tab_min, 2 * tab_max):
        war = True
        for j in range(2, i):
            if i % j == 0:
                war = False
        if war:
            prime_nums.append(i)
    return prime_nums


# Wpisywanie i reszta operacji
def main():
    n = int(input('Wprowadź wymiar tablicy n x n: '))
    x = []

    # Tworzenie listy n x n i jej wypełnianie
    for i in range(n):
        x.append([])
        for j in range(n):
            x[i].append(random.randint(1, 1000))

    # Poniższa linijka do testów na danych liczbach
    # x = [[1, 3, 5], [7, 8, 9], [11, 13, 15]]
    y = copy.deepcopy(x)    # Twarda kopia listy - operacje nie będą naśladowane

    # Wypisanie listy przed zmianą
    for i in range(n):
        for j in range(n):
            print('{0: ^6}'.format(x[i][j]), end=" ")
        print()

    # Wyszukiwane najmniejszej i największej wartości w liście - do szukania pierwszych
    tab_max = 0
    tab_min = 99999999999999999999999999999999999999999999999999999999999
    for i in range(n):
        if tab_max < max(x[i]):
            tab_max = max(x[i])
        if tab_min > min(x[i]):
            tab_min = min(x[i])

    prime_nums = primes(tab_max, tab_min)

    print(f'\n{prime_nums}\n')

    # Przejście przez każdy element i jego sprawdzenie z całą tablicą (kopia y), m,o do sterowania pozycją kopii
    # Zmiany są robione na kopii, aby dalej dobrze sprawdzało
    for i in range(n):
        for j in range(n):
            stat = False    # Do kontroli zamiany liczby na 0 w liście
            m = o = 0
            for k in range(n**2):
                if (x[i][j] + x[m][o]) in prime_nums:
                    stat = True
                    break
                o += 1
                if o == n: # Przejście do następnych komórek w kopii bez 50 tys pętli
                    m += 1
                    o = 0

            if not stat:
                y[i][j] = 0

    # Wypisanie listy po wykonanych operacjach
    for i in range(n):
        for j in range(n):
            print('{0: ^6}'.format(y[i][j]), end=" ")
        print()


if __name__ == '__main__':
    main()


# Przykłady: (Do sprawdzenia czy one są git)

# [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
# [ 1,  3,  5]          [0, 0, 0]
# [ 7,  9, 11]    ->    [0, 0, 0]
# [13, 15, 17]          [0, 0, 0]

# [[1, 3, 5], [7, 8, 9], [11, 13, 15]]
# [ 1,  3,  5]          [1,  3,  5]
# [ 7,  8,  9]    ->    [0,  8,  9]
# [11, 13, 15]          [11, 0, 15]

# [[422, 720, 454], [262,  31, 470], [121, 722, 664]]
# [422, 720, 454]          [0,  720, 0]
# [262,  31, 470]    ->    [262, 31, 0]
# [121, 722, 664]          [121,  0, 0]
