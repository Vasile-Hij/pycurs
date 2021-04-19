#!/usr/bin/env python3
"""2players hot seat"""

def in_dictionary(word):
    """Reading a dictionary to check if words
    inserted by user exits in it"""
    f = open('file_input.txt', 'r')
    while True:
        files = f.readline()
        if not files:
            break
        files = files.strip()
        if files.lower() == word.lower():
            f.close()
            return True
    f.close()
    return False


def is_valid(word, prefix):
    """Checking if the word is valid """
    if not in_dictionary(word):
        return False, 'This word does not exist!'
    if not word.startswith(prefix):
        return False, 'The inserted word ' \
                      'does not respect the rule of the game'
    return True, 'The word is valid'


def start_round():
    """Beginning a new round"""
    while True:
        first_letter = input('insert a letter: ')
        if len(first_letter) > 1 or not first_letter.isalpha():
            print('The character is not valid')
            continue
        break

    first_letter = first_letter.lower()
    print('Chosen letter %s is not valid ' % first_letter)
    print('Player 2: Say a word begin with  %s' % first_letter)
    word = input('~')
    step, message = is_valid(word, prefix=first_letter)
    if step:
        return True, word
    return False, message


def main_game(word): #OK full - bucla_principala()
    while True:
        #FIXME - validate word with minimum 2 characters
        prefix = word[-2:]
        print('Write a word that start with %s' % prefix)
        word = input('~')
        step, message = is_valid(word, prefix=prefix)
        if not step:
            print('> %s' % message)
            print('> Th round has ended.' )
            break


def legend(): #ok
    """Rules of the game"""
    print("2 players hot seat game")


def help_game(): # ok
    """Help message"""
    print('Options')
    print('\t start - Start game')
    print('\t exit - Leave game')
    print('\t legend - Display game rules')
    print('\t help - this menu')



def playing_game():
    """2 players hot seat game"""
    print('Rules')
    player_1_score= []
    player_2_score = []

    while len(player_1_score) < 5 and len(player_2_score) < 5:
        step, word = start_round()
        if not step:
            print(word)
            continue
        main_game(word)


def main(): # ok
    while True:
        commands = input('~')
        if commands == 'start':
            playing_game()
        elif commands == 'help':
            help_game()
        elif commands == 'legend':
            legend()
        elif commands == 'exit':
            break
        else:
            print('> This commands does not exists!')
            print('Please use help for more details!')


if __name__ == "__main__":
    main()