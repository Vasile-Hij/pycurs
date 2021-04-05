#!/usr/bin env python3

SECRET = 'Secretword'


def valid_char(character):
    """Validate the user input """

    return len(character) == 1 and character.isalpha()


def check_char(word, character):
    """Check if char is included in secret word"""
    return character.lower() in word.lower()


def current_pos(secret_word, guessed_char):
    """Display partially result
        secret_word : 'se'
        display: se__e_ ____
    """
    for character in secret_word:
        if check_char(guessed_char, character):
            print(character, end="")
        else:
            print("_", end=" ")
    print("")


def completed_word(secret_word, guessed_char):
    """Checking if all characters from secret_word
    can be found in guessed_char"""
    for character in secret_word:
        if not check_char(guessed_char, character):
            return False
        return True


def hangman(wrong_char):
    """ Display hangman
    wrong_char: 1
    display: lost a leg
    """
    if wrong_char == 0:
        pass
    elif wrong_char == 1:
        pass


def ask_input():
    return input(f"Insert a word: ")


def guessed_secret(secret_word, guessed_char):
    # SecretWord    SW
    for character in secret_word:
        if not character(guessed_char, character):
            return False
        return True


def chances_left(maximum, current):
    return maximum - current


def begin():
    """Start a new game Hangman"""
    chance = 7
    moved = 0
    correct_char = ''
    tried_char = ''
    parts = ['freedom', 'head', 'body', 'left_hand', 'right_hand', 'left_leg', 'right_leg']

    print(f"Weclome to Hangman!")
    print(f"You have to guess the word to complete the game")
    current_pos(SECRET, correct_char)
    print(f"Chances left %d" % chances_left(chance, moved))

    parts_counter = 0
    while moved < chance:

        character = ask_input()
        if valid_char(character):
            if check_char(tried_char, character):
                print(f"You have already tried this character %s" % character)
            else:
                tried_char = "%s%s" % (tried_char, character)
                if check_char(SECRET, character):
                    correct_char = "%s%s" % (correct_char, character)
                    if completed_word(SECRET, correct_char):
                        print(f"Congratulations, you have won the game! The secret word was: ", end="\n")
                        current_pos(SECRET, correct_char)
                        break
                    else:
                        print(f"You have guessed a correct character %s:" % character)
                        current_pos(SECRET, correct_char)
                else:
                    moved += 1
                    parts_counter += 1
        else:
            print("You have not inserted a character %s" % character)
        print(f"\nChances left: {chances_left(chance, moved)}")

        if parts_counter == 0:
            print(f"You are ok", end="\n")
        else:
            print(f"You've lost: {', '.join(parts[:parts_counter])}")

    if chance == moved:
        print(f"You have lost the game!")


def main():
    begin()


if __name__ == "__main__":
    main()
