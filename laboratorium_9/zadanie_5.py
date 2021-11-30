def fib(index):
    num = 1
    num2 = 0
    for a in range(index):
        tmp = num
        num += num2
        num2 = tmp
    return num


quantity = n = int(input('Wprowadź rozmiar nxn: '))
x = []

for i in range(n):
    x.append([])
    for j in range(n):
        x[i].append(None)

row = column = direction = inserted = side = 0

for i in range(n**2):
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

    match direction % 4:
        case 0:
            column += 1
        case 1:
            row += 1
        case 2:
            column -= 1
        case 3:
            row -= 1

for i in range(n):
    for j in range(n):
        print('{0: ^15}'.format(x[i][j]), end=" ")
    print()
