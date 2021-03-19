#!/usr/bin/env python3

def main():
    num = 25
    num_div = 0

    divisor = 2
    while divisor <= num // 2:
        if num % divisor == 0:
            num_div += 1
            break
        divisor += 1

    if num_div == 0 and num >= 1:
        print('The number is %d is prime' % num)
    else:
        print('The number is %d is not prime' % num)


if __name__ == "__main__":
    main()