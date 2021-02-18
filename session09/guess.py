import random


def guess_number(max_number=20, total_tries=6):
    """
    A "Guess the Number" game.
    The program will think of a random number from 1 to max_number (default 20), and ask user to guess it.
    The program will tell user if each guess is too high or too low.
    The user wins if user can guess the number within total_tries (default 6) tries.
    """
    guesses_taken = 0
    print('Hello! What is your name?')
    name = input('>> ')

    number = random.randint(1, max_number)
    # print(number)
    print(f'Well, {name}, I am thinking of a number between 1 and {max_number}.')

    while guesses_taken < total_tries:
        print('Take a guess:')
        guess = input('>> ')
        while not guess.isdigit():
            print('Please enter an integer:')
            guess = input('>> ')
        guess = int(guess)

        guesses_taken += 1
        if guess < number:
            print('Your guess is too low.')
        elif guess > number:
            print('Your guess is too high.')
        else:
            print(
                f'Good job, {name} ! You guessed my number in {guesses_taken} guesses!'
            )
            break

    if guess != number:
        print(f'Nope. The number I was thinking was {number}.')


def main():
    # guess_number(10, 4)
    # guess_number()
    guess_number(total_tries=5, max_number=100)


if __name__ == "__main__":
    main()
