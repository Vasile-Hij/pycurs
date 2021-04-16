#!/usr/bin/env python
"""String palindrome program by using mirroring method"""


def palindrome(string):
    return string == string[::-1]


def valid_input(usr_input):
    return usr_input.isalnum()


def ask_input():
    return input(f"Please check a string to check if it is palindrome: ")


def main():
    print(f"Type 'exit' in order to quit")
    while True:
        string = ask_input()
        if string == "exit":
            break
        if not valid_input(string):
            print(f"The inserted '%s' character is not a allowed!" % string)
            print(f"Please try again!")
        if not len(string) > 1:
            print(f"Please insert minimum 2 characters!")
        if palindrome(string) and valid_input(string):
            print(f"String '%s' is palindrome!" % string)
        else:
            print(f"String '%s' is not palindrome!" % string)


if __name__ == "__main__":
    main()