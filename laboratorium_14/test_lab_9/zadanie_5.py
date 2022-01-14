# Poprawki w zadaniu na potrzeby testów
def fib(index):

    if type(index) != int:
        raise TypeError

    num = 1
    num2 = 0
    for a in range(index):
        tmp = num
        num += num2
        num2 = tmp
    return num


def fill(x, quantity, n):
    row = column = direction = inserted = side = 0

    for i in range(n ** 2):
        x[row][column] = fib(i)
        inserted += 1

        if inserted == quantity:
            direction += 1

        if side % 2 == 0 and inserted == quantity:
            quantity -= 1
            inserted = 0
            side += 1

        elif side % 2 == 1 and inserted == quantity:
            inserted = 0
            side += 1

        if direction % 4 == 0:
            column += 1
        elif direction % 4 == 1:
            row += 1
        elif direction % 4 == 2:
            column -= 1
        elif direction % 4 == 3:
            row -= 1

    return x


def main():
    n = int(input('Wprowadź rozmiar nxn: '))
    x = []

    for i in range(n):
        x.append([])
        for j in range(n):
            x[i].append(None)

    x = fill(x, n, n)

    print(x)
    print()
    for i in range(n):
        for j in range(n):
            print('{0: ^15}'.format(x[i][j]), end=" ")
        print()


if __name__ == "__main__":
    main()
