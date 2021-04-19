#!/usr/bin/env python
"""Strings in Python"""

string = '2'

def main():
    """Strings are immutable,
    so any modification it will generate a new strings
    """
    """Type 1"""
    strings1 = '%s has %s.'
    print(strings1 % ('Joe', 'apples'))

    """Type 2"""
    string2 = '%(name)s has %(fruit)s.'
    print(string2 % {'name': 'John', 'fruit': 'strawberries'})

    """Type 3"""
    string3 = '{} has {}.'
    print(string3.format('Daniel', 'lemons'))

    """Type 4"""
    string4 = '{name} has {fruit}.'
    print(string4.format(name='George', fruit='cranberries'))

    # print(string)
    # string = 'It will not work'
    # print(string)
    print('Inside of main')
    global string
    string = '1'
    print(string)
    print(id(string))


if __name__ == '__main__':
    print('Before main')
    print(string)
    print(id(string))

    main()

    print('After main')
    print(string)
    print(id(string))