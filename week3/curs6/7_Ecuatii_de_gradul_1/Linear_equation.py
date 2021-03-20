#!/usr/bin/env python3

# a * x + b = c
# a * x = b - c
# x = (b-c) / a
def main():
    while True:
        a = input(f'Insert a: ')
        b = input(f'Insert b: ')
        c = input(f'Insert c: ')

        if a.isalpha() or b.isalpha() or c.isalpha():
            print('Try again!')
            continue

        a = float(a)
        b = float(b)
        c = float(c)

        result = c - b

        if (a < 0 or a > 0) and (b <= 0 or b >= 0) and (c <= 0 or c >= 0):
            x = result / a
            print(f"X is {x}\n{a * x} is equal to {result}.")
        if a == 0 and (b <= 0 or b >= 0) and (c >= 0 or c <= 0) and b != c:
            x = 0
            print(f"X is 0\n{a * x} is not equal to {result}.")
        if a == 0 and (b <= 0 or b >= 0) and (c >= 0 or c <= 0) and b == c:
            x = 0
            print(f"X is 0\n{a * x} is equal to {result}.")
        break


if __name__ == '__main__':
    main()