#!/usr/bin/env python3

def main():
    while True:
        usr_input = input("Please insert a number: ")
        if usr_input.isnumeric():
            break
        else:
            print('The inserted %s is not a number!' % usr_input)
            print('Try again with a number bigger or equal to 0: ')

    n = int(usr_input)

    previous_pos = 0
    current_num = 1
    if n < 0:
        print('Try again with a number bigger or equal to 0: ')
    elif n == 0:
        return 0
    elif n == 1:
        return current_num
    else:
        for _ in range(0, n):
            new_num = previous_pos + current_num
            previous_pos = current_num
            current_num = new_num
        return current_num


if __name__ == "__main__":
    print(main())