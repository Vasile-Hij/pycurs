#!/usr/bin/env python3

def main():

    while True:
        usr_input = input('Check if the number is prime: ')
        if usr_input.isnumeric():
            break
        else:
            print('The input character %s is not a number' % usr_input)

    dividend = int(usr_input)

    def is_prime(dividend):
        if dividend <= 1:
            return False
        if dividend <= 3:
            return True
        if dividend % 2 == 0 or dividend % 3 == 0:
            return False
        num_sqrt = 5
        while num_sqrt ** num_sqrt <= dividend:
            if dividend % num_sqrt == 0 or dividend % (num_sqrt + 2) == 0:
                return False
            num_sqrt += 6
        return True


    if is_prime(dividend):
        print("The number %d is prime" % dividend)
    else:
        print("The number %d is not prime" % dividend)


if __name__ == '__main__':
    main()