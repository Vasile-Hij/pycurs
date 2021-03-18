#!/usr/bin/env python3

def main():
    while True:
        user_input = input('Please insert the number: ')
        if user_input.isnumeric():
            break
        else:
            print('%s is not a valid number!' % user_input)
    usr_input = int(user_input)
    # store the initial value
    num_to_check = usr_input

    reverse_num = 0
    while usr_input > 0:
        # extract last digit
        digit = usr_input % 10
        # adding last digit to previous digit
        reverse_num = reverse_num * 10 + digit
        # floor divide the number leave out the last digit from number
        usr_input = usr_input // 10

    if num_to_check == reverse_num:
        print('The number %d is palindrome' % num_to_check)
    else:
        print('The number %d is not palindrome' % num_to_check)


if __name__ == "__main__":
    main()
