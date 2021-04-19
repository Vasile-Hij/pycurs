#!/usr/bin/env python3

def main():
    while True:
        usr_input = input("Please insert a number: ")
        if usr_input.isnumeric():
            break
        else:
            print(f'The inserted %s is not a number' % usr_input)
    n = int(usr_input)

    while n >= 0:

        previous_num = 0
        current_num = 1

        for _ in range(0, n):
            current_num, previous_num = current_num + previous_num, current_num
            # print(current_num) # all numbers
        print(current_num) # result only
        break


if __name__ == '__main__':
    main()