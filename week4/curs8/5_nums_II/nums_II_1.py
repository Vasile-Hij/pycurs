#!/usr/bin/env python3

# a, b, c : a + b + c = n

def main():
    n = 10

    for a in range(0, n+1):
        for b in range(0, n+1):
            for c in range(0, n+1):
                if a + b + c == n:
                    print('%d %d %d' % (a, b, c))


if __name__ == '__main__':
    main()