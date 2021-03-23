#!/usr/bin/env python3

# 1000-9999

def main():
    lower_limit = 100
    upper_limit = 1000

    for the_num in range(lower_limit, upper_limit):
        copy_nums = the_num
        while copy_nums >= 100:
            copy_nums = copy_nums // 10

        first_num = the_num // 10
        second_num = copy_nums % 10

        second_last_num = (the_num // 10) % 10
        last_num = the_num % 10

        if first_num + second_num == second_last_num - last_num:
            print(the_num)


if __name__ == '__main__':
    main()