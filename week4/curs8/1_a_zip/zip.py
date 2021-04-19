#!/usr/bin/env python3

def main():
    texts = "AAAABBBAAACCCCCDAAB"
    count = 0
    previous_char = ''

    for character in texts:
        if previous_char == character:
            count += 1
        else:
            if previous_char:
                print('%d%s' % (count, previous_char), end='')
            previous_char = character
            count = 1

    if previous_char:
        print('%d%s' % (count, previous_char), end='')


if __name__ == "__main__":
    main()