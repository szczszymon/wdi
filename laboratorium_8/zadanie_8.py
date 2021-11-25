class UnevenNoOfParentheses(Exception):
    pass


class BadPlacement(Exception):
    pass


def check_parentheses(data):
    try:
        if data.count('(') != data.count(')'):
            raise UnevenNoOfParentheses

        return False

    except UnevenNoOfParentheses:
        return True


def clustering(data):
    if check_parentheses(data):
        return 'Nie można utworzyć zbalansowanych klastrów! [Nierówna ilość znaków "(" i ")"]'

    clusters = []
    cluster = ""
    i = 0

    try:
        for char in data:
            match char:
                case '(':
                    i += 1
                    cluster += char
                case ')':
                    i -= 1
                    cluster += char
                    if i == 0:
                        clusters.append(cluster)
                        cluster = ""
                    elif i < 0:
                        raise BadPlacement

        return clusters

    except BadPlacement:
        print('Wystąpił błąd przy tworzeniu klastrów! [Nawias zamka się bez uprzedniego otwarcia]')
        try_anyway = input('Wypisać utworzone klastry? (y/n): ')

        if try_anyway in ['y', 'Y']:
            return clusters

        elif try_anyway in ['n', 'N']:
            exit(0)


def drop_different(data):
    new_data = ""

    for char in data:
        if char in ['(', ')']:
            new_data += char

    return new_data


def main():
    data = input('Wprowadź napis do podziału na klastry: ')
    data = drop_different(data)
    print(f'Napis przekazany do poklastrowania: {data}')
    print(clustering(data))


if __name__ == '__main__':
    main()

# Przykłady:
# ()()()    ->    ['()', '()', '()']
# ((QW(asd))ERT)    ->    ['((()))']
# ((()))(())()()(()())    ->    ['((()))', '(())', '()', '()', '(()())']
# ((())())(()(()()))    ->    ['((())())', '(()(()()))']
# ((()())())))))))    ->    Nierówna ilość znaków
# )()()(    ->    Nawias zamyka się bez uprzedniego otwarcia
# (-(()())-()())-)(-((()))    ->    Nawias zamyka się bez uprzedniego otwarcia    ->    ['((()())()())']
# (((())(())))((())))()(()    ->    Nawias zamyka się bez uprzedniego otwarcia    ->    ['(((())(())))', '((()))']
