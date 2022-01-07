code = open("kod.txt", "r")

text = "za z"

for k in range(0, len(text)):
    for line in code.readlines():
        if text[k] in line:
            if line[len(line) - 2] == text[k]:
                print(line[:-2])
    code.seek(0)
