# Poprawki w zadaniu na potrzeby testów
import copy


def factorize(n, result, output, curr_sum, start):
    if curr_sum == n:
        result.append(copy.copy(output))

    for i in range(start, n):
        temp_sum = curr_sum + i

        if temp_sum <= n:
            output.append(i)

            factorize(n, result, output, temp_sum, i)

            output.pop()

        else:
            return


def print_res(result):
    output = ""
    for res in result:
        text = ""
        for element in res:
            text += f" + {element}"
        output += f"{text[3:]}\n"
    return output


def main():
    n = int(input("Podaj liczbę naturalną do rozkładu: "))
    if n == 1:
        print(1)
    else:
        result = []
        output = []

        factorize(n, result, output, 0, 1)

        print(print_res(result))


if __name__ == "__main__":
    main()
