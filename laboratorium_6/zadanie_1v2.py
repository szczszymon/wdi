class DeltaTooSmall(Exception):
    pass


a = float(input('Wprowadz A: '))
b = float(input('Wprowadz B: '))
c = float(input('Wprowadz C: '))


try:
    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        raise DeltaTooSmall

    x1 = (-1 * b + (delta ** (1 / 2))) / (2 * a)
    x2 = (-1 * b - (delta ** (1 / 2))) / (2 * a)

    if x1 == x2:
        print('Rozwiązaniem jest x: ', x1)

    else:
        print('Rozwiązaniami są x1: ', x1, ', x2: ', x2)

except DeltaTooSmall:
    print('Liczby zespolone nie są obsługiwane')
