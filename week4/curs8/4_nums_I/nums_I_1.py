#!/usr/bin/env python3

# 1000-9999

def main():
    lower_limit = 100
    upper_limit = 1000

    for the_num in range(lower_limit, upper_limit):
        # Finding first 2 digits from num
        # Finding the num
        # Finding first and second digit
        nums = 0
        copy_nums = the_num
        while copy_nums:
            nums += 1
            copy_nums = copy_nums // 10

        first_num = the_num // (10 ** (nums - 1))
        second_num = (the_num // (10 ** (nums - 2))) % 10

        # Finding the last 2 digits
        second_last_num = (the_num // 10) % 10
        last_num = the_num % 10

        if first_num + second_num == second_last_num - last_num:
            print(the_num)


if __name__ == '__main__':
    main()