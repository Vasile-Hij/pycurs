#!/usr/bin/env python
"""String palindrome program from middle of the string"""


def palindrome(string):
    for position in range(0, len(string)-1 // 2):
        if string[position] == string[len(string) - position - 1]:
            return False
    return True


def valid_input(usr_input):
    return usr_input.isalnum()


def ask_input():
    return input(f"Please insert a string to check if it is palindrome: ")


def main():
    print(f"Type 'exit' in order to quit")
    while True:
        string = ask_input()
        if string == "exit":
            break
        if len(string) < 2:
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