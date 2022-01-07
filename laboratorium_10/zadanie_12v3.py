# Proszę napisać program wczytujący tablicę dwuwymiarową o ustalonym wymiarze n×n wypełnioną liczbami naturalnymi.
# Dla danej tablicy należy napisać funkcję, która zeruje elementy nie posiadające liczby komplementarnej. Liczby
# naturalne a,b są komplementarne jeżeli ich suma jest liczbą pierwszą. Wymiar tablicy powinien być definiowany przez
# użytkownika.
import copy
import random


class NegativeNumberError(Exception):
    pass


# funkcja sprawdzajaca, czy liczba jest pierwsza
def prime(liczba):
    if liczba < 2:
        return 0  # liczba nie jest pierwsza

    for k in range(2, liczba):
        if (liczba % k) == 0:
            return 0
    return 1  # liczba jest pierwsza


# podawanie wymiarów macierzy
try:
    n = int(input("Wymiary macierzy n x n: "))
    if n <= 0:
        raise NegativeNumberError
except (ValueError, NegativeNumberError):
    print("Liczba nie jest całkowita dodatnia")
    exit()

macierz = []
for i in range(n):
    macierz.append([])
    for j in range(n):
        macierz[i].append(random.randint(1, 100))

#macierz = [[34, 15, 61, 38, 67], [98, 32, 40, 52, 36], [15, 27, 13, 46, 79], [46, 15, 78, 78, 77], [79, 25, 35, 99, 53]]
macierz = [[17, 25, 33], [6, 9, 45], [39, 56, 87]]
print(macierz)

kopia = copy.deepcopy(macierz)
#

for i in range(len(macierz)):
    for j in range(len(macierz[i])):
        wrong = True
        for x in range(len(macierz)):
            for y in range(len(macierz[x])):
                if macierz[i][j] != macierz[x][y]:
                    if prime(macierz[i][j] + macierz[x][y]) == 1:
                        wrong = False
        if wrong:
            kopia[i][j] = 0

print()
print("Podst:")
for i in macierz:
    print(i)

print()
print("Nowa:")
for i in kopia:
    print(i)
