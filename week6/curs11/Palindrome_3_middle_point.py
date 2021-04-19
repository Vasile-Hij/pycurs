#!/usr/bin/env python
"""String palindrome program by using middle point method"""


def palindrome(string):
    if len(string) < 2:
        print(f'Please insert minimum 2 character')
        return False

    middle = len(string) // 2
    first_part = string[:middle:1]
    last_part = string[:-(middle + 1): -1]
    return first_part == last_part


def ask_input():
    return input("Please insert a string to check if it is palindrome: ")


def valid_input(usr_input):
    return usr_input.isalnum()


def main():
    print(f"Type 'exit' in order to quit")
    while True:
        string = ask_input()
        if string == "exit":
            break

        if not valid_input(string):
            print(f"These characters '%s' are no allowed!" % string)
            print(f"Please try again!")

        if palindrome(string) and valid_input(string):
            print("String '%s' is palindrome" % string)
        else:
            print("String '%s' is not palindrome" % string)


if __name__ == '__main__':
    main()