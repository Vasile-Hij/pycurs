#!/usr/bin/env python
"""String palindrome program"""


def palindrome(string):
    length = len(string)
    middle = length // 2

    first_part = string[length:(-middle + 1):1]
    last_part = string[1:middle - 1:1]
    return first_part == last_part


def ask_input():
    return input(f"Please insert a character to check if it is palindrome: ")


def valid_input(usr_input):
    return usr_input.isalnum()


def main():
    print(f"Type 'exit' in order to quit")
    while True:
        string = ask_input()
        if string == "exit":
            break
        if not len(string) > 1:
            print(f"Please insert minimum 2 characters!")
        if not valid_input(string):
            print(f"These characters '%s' are no allowed!" % string)
            print(f"Please try again!")

        if palindrome(string) and valid_input(string):
            print("String '%s' is palindrome" % string)
        else:
            print("String '%s' is not palindrome" % string)


if __name__ == '__main__':
    main()
