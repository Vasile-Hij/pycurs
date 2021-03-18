#!/usr/bin/env python3

# correct usage of int() while user make an input avoiding collision

def main():

    while True:
        usr_input = input('Scrie un numar mai mare sau egal ca 0: ')
        if usr_input.isnumeric():
            break
        else:
            print('The input character `%s` is not valid' % usr_input)

    number = int(usr_input)

    if number % 2 == 0:
        print('The number %d is even' % number)
    else:
        print('The number %d is odd' % number)


if __name__ == '__main__':
    main()