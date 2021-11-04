# Python 3.10

import random


# Wprowadzanie liczb
def number():
    while True:
        x = input('Wprowadź liczbę: ')
        try:
            x = float(x)
            break
        except ValueError:
            print('Podane dane nie są liczbowe! Spróbuj ponownie\n')
    return x


# Menu wyboru działania, wykonywanie obliczeń
def menu(num1, num2):
    while True:
        choice = input('Wprowadź symbol działania które chcesz wykonać ("z" aby zakończyć): ')

        match choice:
            case '+':
                print(num1, ' + ', num2, ' = ', num1 + num2, '\n')
                break
            case '-':
                print(num1, ' - ', num2, ' = ', num1 - num2, '\n')
                break
            case '*':
                print(num1, ' * ', num2, ' = ', num1 * num2, '\n')
                break
            case '/':
                print(num1, ' / ', num2, ' = ', num1 / num2, '\n')
                break
            case '**':
                print(num1, ' ** ', num2, ' = ', num1 ** num2, '\n')
                break
            case '^':
                print(num1, ' ^ ', num2, ' = ', num1 ** (1 / num2), '\n')
                break
            # Losowanie liczby z zakresu mniejsza-większa, gdzie liczby zamieniane są na całkowite
            case 'x':
                if int(num1) > int(num2):
                    res = random.randint(int(num2), int(num1))
                    print('Losowa liczba z zakresu ', int(num2), '-', int(num1), ": ", res, end=" ")
                    print(f'(liczby są konwertowane: {num1} = {int(num1)}, {num2} = {int(num2)})\n')
                elif int(num1) < int(num2):
                    res = random.randint(int(num1), int(num2))
                    print('Losowa liczba z zakresu ', int(num1), '-', int(num2), ": ", res, end=" ")
                    print(f'(liczby są konwertowane: {num1} = {int(num1)}, {num2} = {int(num2)})\n')
                else:
                    print(f'Podany zakres jest zbyt mały! (liczby są konwertowane: {num1} = {num2} = {int(num1)})\n')
                break
            case 'z':
                exit(0)
            case _:
                print('Niepoprawny symbol działania! Spróbuj ponownie\n')


# Sprawdzenie potrzeby nowych danych
def new_data():
    while True:
        r = input('Czy chcesz wprowadzić nowe dane? (T/N) ')
        if r == 'T':
            return True
        elif r == 'N':
            return False
        else:
            print('Niepoprawny wybór! Spróbuj ponownie\n')
    

# Struktura główna, program działa aż do momentu zakończenia go przez użytkownika
def main():
    while True:
        a = number()
        b = number()
        while True:
            menu(a, b)
            if new_data():
                break


if __name__ == '__main__':
    main()
