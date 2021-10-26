num1 = int(input("Podaj 1 liczbe: "))
num2 = int(input("Podaj 2 liczbe: "))

if abs(num2 - num1 + 1) > 20:
    avg = int((num2 + num1) / 2)
    j = -3
    for i in range(7):
        if j != 0:
            print(avg + j)
        j += 1

else:
    i = num1
    while i <= num2:
        print(i)
        i += 1
