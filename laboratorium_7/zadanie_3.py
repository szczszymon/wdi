import random

nums = []
digits = []


# Funkcja sprawdzająca cyfry podanych liczb
def check_digits():
    for sublist in range(len(digits)):  # Wybór listy z którą sprawdzamy cyfry
        for checked in range(len(digits)):  # Wybór listy której cyfry są sprawdzane z inną listą
            if checked == sublist:
                continue

            for digit in digits[checked]:
                if digit not in digits[sublist]:
                    return False
    return True


# Funkcja generująca przykładowe liczby
def generate():
    generated_nums = [[], [], []]
    new_num = ""

    print("Podane liczby nie składają się z tych samych cyfr")

    for i in range(3):
        for j in range(3):
            while True:
                status = True

                # Pętla do różnych długości generowanych liczb
                # for k in range(random.randint(len(digits[i]), len(digits[i]) + 10)):
                for k in range(len(digits[i])):
                    new_num += digits[i][random.randint(0, len(digits[i]) - 1)]

                for digit in digits[i]:
                    if digit not in new_num:
                        status = False
                        new_num = ""
                        break

                if status:
                    break

            # Losowanie czy liczba ma być ujemna
            if random.randint(0, 1) == 1:
                new_num = int(new_num)
            else:
                new_num = int(new_num) * -1

            generated_nums[i].append(int(new_num))
            new_num = ""

        print(f"Liczby wygenerowane dla {nums[i]}: {generated_nums[i]}")


# Wprowadzanie i weryfikacja liczb
while True:
    try:
        for x in range(3):
            nums.append(int(input(f'Podaj {x + 1} liczbę: ')))
        print()
        break

    except ValueError:
        print("Podano liczbę niecałkowitą! Podaj liczby jeszcze raz\n")
        nums.clear()


# Lista dwuwymiarowa - rozdzielenie cyfr w liczbie
for number in nums:
    if number < 0:
        digits.append(list(str(number)[1:]))
    else:
        digits.append(list(str(number)))


if check_digits():
    print("Podane liczby składają się z tych samych cyfr")
else:
    generate()

# Przykłady:
# 1; 2,-22,222; 12,-12,2; 1234,12345,123456;
