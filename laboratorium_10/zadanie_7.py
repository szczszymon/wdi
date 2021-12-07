def file_read(filename):
    vowels = ('A', 'a', 'Ą', 'ą', 'E', 'e', 'Ę', 'ę', 'I', 'i', 'O', 'o', 'Ó', 'ó', 'U', 'u', 'Y', 'y')
    text = ""

    file = open(f'{filename}.txt', 'r')
    for line in file:
        for word in line.split():
            symbol = ""

            if word[-1] in [',', '.', ':', ';', '?', '!']:
                symbol = word[-1]
                word = word[:-1]

            if word[0] in vowels and word[-1] in vowels:
                new_word = word[::-1].upper()

            elif word[0] in vowels:
                new_word = word[::-1].lower()

            else:
                new_word = word

            if symbol != "":
                new_word = f'{new_word}{symbol}'

            text += f'{new_word} '
        text = text[:-1] + '\n'

    file_write(filename, text)
    file.close()


def file_write(name, text):
    wynik = open(f'{name}.txt', 'w')
    wynik.write(text)
    wynik.close()


def main():
    files = input('Wprowadź pliki .txt (rozdzielane przecinkami): ')
    filenames = files.split(', ')
    print('Zmieniono wskazane pliki.')

    for name in filenames:
        file_read(name)


if __name__ == '__main__':
    main()
