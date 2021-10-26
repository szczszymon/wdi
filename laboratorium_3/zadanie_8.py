import random

x = int(input("Wprowadz liczbe całkowita: "))

# k - liczba znaków * w linii
k = 1

for i in range(x):
    line = ""

    for j in range(x - i):
        line += " "

# o - losowo wybierana pozycja bombki w linii (1 na linię)
    if k > 1:
        o = int(random.randrange(1, k))

    for j in range(k):
        if k != 1:
            if j == o:
                line += "O"
            else:
                line += "*"
        else:
            line += "X"

    k += 2

    print(line)

print(" " * (x - 1), "U")
