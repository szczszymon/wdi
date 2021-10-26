# Poczatek programu
# # Print pustych linii
# Ich generacja ułatwi odnalezienie początku programu w terminalu
print("\n\n")
# Wprowadzenie liczb

numb1 = float(input("Pierwsza liczba: "))
numb2 = float(input("Druga liczba: "))

# Sprawdzenie warunków liczb

if numb1 <= 0 and numb2 <= 0:
    print("Obie liczby są <= 0, kończenie programu")
    exit(0)

elif 0 > numb1 and 0 < numb2:
    print("Liczba 1 jest < 0 , wykorzystana zostanie jej wartosc bezwzgledna")
    numb1 = abs(numb1)

elif 0 > numb2 and 0 < numb1:
    print("Liczba 2 jest < 0 , wykorzystana zostanie jej wartosc bezwzgledna")
    numb2 = abs(numb2)

# Obliczenie i wypisanie wyników
print("Suma liczb: ", numb1 + numb2)
print("Różnica liczb (numb1 - numb2): ", numb1 - numb2)
print("Iloczyn liczb: ", numb1 * numb2)

if (numb1 * numb2) == 10:
    print("Yay!")

print("Iloraz liczb (numb1 / numb2): ", numb1 / numb2)
print("Kwadrat liczby 1: ", numb1 ** 2, "\nKwadrat libczy 2: ", numb2 ** 2)
print("Pierwiastekj liczby 1: ", numb1 ** (1/2), "\nPierwiastek liczby 2: ", numb2 ** (1/2))
