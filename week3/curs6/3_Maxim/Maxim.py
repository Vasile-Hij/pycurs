#!/usr/bin/env python3

def main():
    index = 1
    maximum = 0

    while True:
        max_inputs = input('How many numbers you want to compare: ')
        if max_inputs.isnumeric():
            max_inputs = int(max_inputs)
            break
        print('You have not inserted a valid number')
        print('Type another one')

    while index < max_inputs + 1:
        num = input('Insert a number %d: ' % index)
        is_valid = True
        for position, character in enumerate(num):
            if position == 0:
                if not (character.isdigit() or character in '-+'):
                    is_valid = False
            else:
                if not character.isdigit():
                    is_valid = False

        if not is_valid:
            print("Number you inserted is not valid")
            print('Try again')
        else:
            num = int(num)
            if index == 1:
                maximum = num
            else:
                if maximum < num:
                    maximum = num
            index += 1

    print('The maximum number %d from input is: %s' % (index-1, maximum,))


if __name__ == "__main__":
    main()