#!/usr/bin/env python3

def main():

    secret = 67
    tries = 7

    while tries > 0:
        user_input = input("Input a number from 0 to 100: ")
        print(user_input[1:])
        tries -= 1

        if user_input.startswith('-'):
            if not user_input[1:].isnumeric():
                print("Input must be an integer!")
                continue
        else:
            if not user_input.isnumeric():
                print("Input must be an integer!")
                print(f"{tries} tries left out of 7")
                continue

        guess = int(user_input)

        if guess == secret:
            print(f"You won with {tries} tries out of 7! \nNumber was {secret}")
            exit()
        if guess > 100:
            print(f"Number must be between 0 and 100!\n{tries} tries left out of 7.")
        if 0 <= guess < secret:
            print(f"Number {guess} is too low\n{tries} tries left out of 7.")
        if guess > secret:
            print(f"Number {guess} is too high\n{tries} tries left out of 7.")
        if guess < 0:
            print(f"You are out of range 0-100!\n {tries} tries left out of 7.")

    print(f"You lost! {tries} tries left")
    print(f"The secret number was {secret}.")


if __name__ == "__main__":
    main()