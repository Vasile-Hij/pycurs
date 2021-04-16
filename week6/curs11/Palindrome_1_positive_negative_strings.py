#!/usr/bin/env python
"""String palindrome program by using positive-negative indexing"""


def palindrome(string):
    for position in range(0, len(string) // 2):
        char_1 = string[position]
        char_2 = string[-(position + 1)]
        print(f"Checking %s with %s is: " % (char_1, char_2))
        if char_1 == char_2:
            print(f"Ok")
        else:
            print(f"Here is the difference")


def valid_input(usr_input):
    return usr_input.isalnum()


def ask_input():
    return input(f"Please check a string if it is palindrome: ")


def main():
    print(f"Type 'exit' in order to quit!")
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
            return palindrome


if __name__ == '__main__':
    main()