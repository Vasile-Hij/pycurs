#!/usr/bin/env python
"""Strings in Python"""

def main():
    string = 'This is a string'
    for character in string:
        # print(character)
        pass

    """positive: 0 to n-1
       negative: -n to -1
    """

    print(string)
    print(string[::2])
    print(string[0:2])
    print(string[1::-1])
    print(string[1:2])
    print(string[0:2])


if __name__ == '__main__':
    main()