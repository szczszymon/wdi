#!/usr/bin/python3.10
def main():
    n2 = 0
    n3 = i = 1
    while n3 < 1000000:
        print(i, ': ', n3)
        n = n3
        n3 += n2
        n2 = n
        i += 1


if __name__ == '__main__':
    main()
