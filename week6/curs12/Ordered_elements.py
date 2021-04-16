#!/usr/bin/env python3
"""
The program take a list from user input with strings and/or numbers,
 then it is checking as below:
- check given if the input is ordered (ascending or descending);
- print given if the input is ordered (ascending or descending);
- print given if the input in both cases (if string is not ordered);
- print the other case if it is ordered.


Hint:
 - compare in between characters and numbers -ord();
 - print an ASCII as a character - chr();
 - can use for string ->help(''.split()).

 E.g.
    - input: 12 a 1 b
    - output: not ordered ascending
    - not ordered descending
    - string ordered: 1 12 1 b
    - string unordered: b a 12 1
"""


def get_ascii_or_value(caracter):
    if caracter.isnumeric():
        return int(caracter)
    return ord(caracter)


def characters_respect_order(first, second, order=False):
    first = get_ascii_or_value(first)
    second = get_ascii_or_value(second)
    print("Compare %s with %s" % (first, second))
    print("Received from ordered() order = %s " % order)

    return first >= second if order else first <= second


def ordered(element_list, reverse=False):
    current_element = element_list[0]

    for next_element in element_list[1:]:
        print("Current element: %s" % current_element)
        print("The next element %s" % next_element)
        if reverse:
            print("Call characters_respect_orders to check %s >= %s."
                  % (current_element, next_element))
        else:
            print("Call characters_respect_order to check %s <= %s."
                  % (current_element, next_element))
        if not characters_respect_order(current_element, next_element, order=reverse):
            return False
        current_element = next_element
    return True


def main():
    usr_input = input("Insert a string with space in between characters: ")
    element_list = usr_input.split()
    print("Checking if the list is ascending order...")
    if ordered(element_list):
        print("The list is ascending order.")
    else:
        print("THe list is not ascending order.")
    if ordered(element_list, reverse=True):
        print("The list is descending order.")
    else:
        print("The list is not descending order.")


if __name__ == "__main__":
    main()