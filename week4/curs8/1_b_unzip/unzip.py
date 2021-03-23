#!/usr/bin/env python3

def main():
    text_1 = "4A3B3A5C1D2A1B"
    text_2 = '15A30B'
    text_3 = ''
    text_4 = '14AA'
    counter = 0
    is_char = ''

    for character in text_4:
        if character.isdigit():
            # counter = 15
            # character = 5
            counter = counter * 10 + int(character)
        else:
            if counter:
                print(character * counter, end='')
            else:
                print(character, end='')
            counter = 0


if __name__ == "__main__":
    main()