#!/usr/bin/env python3

def main():
    text = 'Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit'

    letter = input('Insert a letter: ')
    if not letter.isalpha() or len(letter) > 1:
        print('This %d is not a letter' % letter)
    else:
        print('Start again ')
        print('Times for %r is %d times' % (letter, text.count(letter)))
    times = 0
    for character in text:
        if character == letter:
            times += 1
    print('Times for %r is %d' % (letter, times))

    minimum = len(text) + 1
    maximum = -1
    maximum_letter = ''
    minimum_letter = ''

    valid_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    #for position in range(ord('a'), ord('z') + 1):
        # character = chr(position)
    for character in valid_letters:
        times_char = 0
        for element in text:
            if element == character:
                times_char += 1
        if times_char > maximum:
            maximum = times_char
            maximum_letter = character
        if times_char < minimum:
            minimum = times_char
            minimum_letter = character

    print(f'Most frequent letter', maximum_letter, maximum)
    print(f'Less frequent letter', minimum_letter, minimum)


if __name__ == "__main__":
    main()