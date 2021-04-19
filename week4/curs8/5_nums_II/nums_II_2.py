#!/usr/bin/env python3

# a, b, c : a + b + c = n

def main():
    n = 15

    for a in range(1, n + 1):
        for b in range(1, n - a):
            # n = 15, a = 5, b <- n - a, c = n - a - b
            c = n - a - b
            if a + b + c == n:
                print('%d %d %d' % (a, b, c))


if __name__ == '__main__':
    main()
