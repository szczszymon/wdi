def pascal(n):
    if n == 0:
        return [[1]]

    triangle = []

    last = pascal(n-1)
    level = []

    for i in range(n+1):
        if i in [0, n]:
            level.append(1)
        else:
            level.append(last[n-1][i-1] + last[n-1][i])

    for element in last:
        triangle.append(element)

    triangle.append(level)

    return triangle


def fib(n):
    if n in [1, 2]:
        return 1

    triangle = pascal(n+1)

    value = 0
    i = n / 2

    if n % 2 == 1:
        for j in range(int(i), -1, -1):
            value += triangle[int(i)][j]
            i += 1
    else:
        for j in range(int(i - 1), -1, -1):
            value += triangle[int(i)][j]
            i += 1

    return value


def main():
    n = int(input("Podaj ile wyrazów ciągu wypisać: "))
    for i in range(1, n):
        print(f"{i} wyraz ciągu: {fib(i)}")


if __name__ == '__main__':
    main()
