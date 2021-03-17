#!/usr/bin/env python3

usr_input = int(input('Check if the number is prime: '))
dividend = usr_input

def is_prime(dividend):
    if dividend <= 3:
        return dividend > 1
    if dividend % 2 == 0 or dividend % 3 == 0:
        return False
    num_sqrt = 5
    while num_sqrt ** 2 <= dividend:
        if dividend % num_sqrt == 0 or dividend % (num_sqrt + 2) == 0:
            return False
        num_sqrt += 6
    return True


if (is_prime(dividend)):
    print("The number %d isprime" % dividend)
else:
    print("The number %d is not prime" % dividend)