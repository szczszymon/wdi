# Python 3.10

# Validating PIN
def pin_check():
    while True:
        print("\nPodaj kod PIN: ('anuluj' aby przerwać)")
        passwd = input()
        match passwd:
            case '1234':
                return True
            case 'anuluj':
                return False
            case __:
                print("\nWprowadzony kod PIN jest niepoprawny! Spróbuj ponownie")
        print('\n')


# Writing changes to file
def write_info(current_status):
    status = open('saldo.txt', 'w')
    current_status = round(current_status, 2)
    status.write(str(current_status))
    status.close()

    status = open('saldo.txt', 'r')
    print("\nAktualny stan konta: ", status.read())
    status.close()


def wplac():
    if pin_check():
        while True:
            print('\nWprowadź kwotę do dokonania wpłaty:')
            amount = input()

            try:
                float(amount)
                break

            except ValueError:
                print('Wprowadzone dane nie są liczbowe! Spróbuj ponownie\n')

        if float(amount) == 0.0:
            print('\nStan konta nie uległ zmianie')

        else:
            status = open('saldo.txt', 'r')
            current_status = status.read()
            current_status = float(current_status)
            current_status += float(amount)
            status.close()

            write_info(current_status)
    else:
        print('\nOperacja nie powiodła się! - nie podano kodu PIN')

    print('\n')


def wyplac():
    if pin_check():

        status = open('saldo.txt', 'r')
        current_status = status.read()
        current_status = float(current_status)
        status.close()

        while True:
            print('\nWprowadź kwotę do dokonania wypłaty:')
            amount = input()
            try:
                if float(current_status) < float(amount):
                    print("Wprowadzona kwota przewyższa stan konta! Spróbuj ponownie")
                    print('\n')
                else:
                    break
            except ValueError:
                print('Wprowadzone dane nie są liczbowe! Spróbuj ponownie\n')

        if float(amount) == 0.0:
            print('\nStan konta nie uległ zmianie')

        else:
            current_status -= float(amount)

            write_info(current_status)

    else:
        print('\nOperacja nie powiodła się! - nie podano kodu PIN')

    print('\n')


def saldo():
    if pin_check():
        status = open('saldo.txt')
        print("Stan konta: ", status.read())
        status.close()
    else:
        print('\nOperacja nie powiodła się! - nie podano kodu PIN')

    print('\n')


# Choice of operations
def operations():
    print('Co chcesz zrobić w kolejnym kroku? (wpłać, wypłać, sprawdź saldo, zakończ)')
    oper = input()

    match oper:
        case 'wpłać':
            wplac()
        case 'wypłać':
            wyplac()
        case 'sprawdź saldo':
            saldo()
        case 'zakończ':
            exit(0)
        case __:
            print('\nPodana operacja jest nieprawidłowa! Spróbuj ponownie')
            print('\n')


# Main structure of program
def main():
    print("Witaj!")
    while True:
        operations()


if __name__ == '__main__':
    main()
