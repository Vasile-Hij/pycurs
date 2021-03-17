#!/usr/bin/env python3

# correct usage of int() while user make an input avoiding collision

usr_input = input('Insert a number greater than 0: ')
number = int(usr_input)

if number % 2 == 0:
    print('The number %d is even' % number)
else:
    print('The number %d is odd' % number)