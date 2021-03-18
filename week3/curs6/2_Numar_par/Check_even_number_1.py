#!/usr/bin/env python3

# forma simpla de verificare a unui numar par

def main():

    while True:
        usr_input = input('Scrie un numar mai mare sau egal ca 0: ')
        if usr_input.isnumeric():
            break
        else:
            print('The input character `%s` is not valid' % usr_input)

    number = int(usr_input)

    if number % 2 == 0:
        print('numarul %d este par' % number)
    else:
        print('numarul %d nu este par' % number)


if __name__ == '__main__':
    main()