#!/usr/bin/env python3
"""Python week5/curs9 - Functions"""


def addition(num_1, num_2, num_3=0):
    """Count 2 numbers"""
    print('num 1:', num_1)
    print('num 2:', num_2)
    print('num 3:', num_3)
    print('-' * 10)
    return num_1 + num_2 + num_3


def main():
    """Entrypoint for the current script"""
    # do 1 + 2 + 3
    # result = addition(addition(1,2), 3)
    # print(result)

    # result = addition(1, 2)
    # print('result', result)

    # print(addition(1, 2, 3))

    addition(0, 1, 2)  # positional argument
    addition(num_3=3, num_1=1, num_2=2)  # defined
    print(addition(0, num_2=3, num_3=1))  # positional argument, num_1 is arg named


if __name__ == '__main__':
    main()