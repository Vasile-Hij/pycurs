#!/usr/bin/env python3

def main():

    user_input = input('Please insert the number: ')
    if not user_input.isnumeric():
        print('The number is valid: ')
    else:
        print('The number is not valid')
        print('Try again')
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
        print('The number %d is palindrom' % num_to_check)
    else:
        print('The number %d is not palindrom'% num_to_check)


if __name__ == "__main__":
    main()