#!/usr/bin/env python3

def main():

    secret = 67
    tries = 7

    while tries > 0:
        user_input = input("Input a number from 0 to 100: ")
        tries -= 1

        if not (user_input.isnumeric() and int(user_input) >= 0):
            print("Input must be an integer greater than zero. Please try again!")
            print(f"{tries} tries left out of 7")
            continue

        guess = int(user_input)

        if guess == secret:
            print(f"You won with {tries} tries out of 7! \nNumber was {secret}")
            exit()
        elif guess < secret:
            print(f"Number {guess} is too low\n{tries} tries left out of 7.")
        else:
            if guess > secret:
                print(f"Number {guess} is too high\n{tries} tries left out of 7.")


    print(f"You lost! {tries} tries left")
    print(f"The secret number was {secret}.")


if __name__ == "__main__":
    main()