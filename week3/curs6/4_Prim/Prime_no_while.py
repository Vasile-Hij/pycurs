#!/usr/bin/env python3

def main():
    while True:
        usr_input = input('Check if the number is prime: ')
        if usr_input.isnumeric():
            break
        else:
            print('The input character %s is not numeric' % usr_input)

    dividend = int(usr_input)
    prim = True

    if dividend > 1:
        for divisor in range(2, dividend):
            if dividend % divisor == 0:
                prim = False
                break

    if prim:
        print('The number %d is prime' % dividend)
    else:
        print('The number %d is not prime' % dividend)
        print(divisor, 'multiplied by', dividend // divisor, 'is', dividend)


if __name__ == '__main__':
    main()
