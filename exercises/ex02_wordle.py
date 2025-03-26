"""The purpose of this exercise is to create a Wordle-like game"""

__author__: str = "730707069"


def contains_char(search_string: str, target_letter: str) -> bool:
    """This function searches the guess word for a character"""
    assert len(target_letter) == 1, f"len('{target_letter}') is not 1"
    idx: int = 0
    while idx < len(search_string):
        if search_string[idx] == target_letter:
            return True  # Found the letter, so return True
        idx += 1  # Continues to check the next character
    return False  # Letter  wasn't found, so return False


def emojified(guess: str, secret: str) -> str:
    """This function is given two strings of equal length and will return a string of emoji whose color codifies the result of a guess"""
    assert len(guess) == len(secret), "Guess must be same length as secret"

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    result: str = ""
    idx: int = 0
    while idx < len(guess):
        if guess[idx] == secret[idx]:
            result += GREEN_BOX  # Correct letter in the correct position
        elif contains_char(secret, guess[idx]):
            result += YELLOW_BOX  # Letter is in the secret but in the wrong position
        else:
            result += WHITE_BOX  # Letter is not in the secret
        idx += 1  # Move to the next character
    return result


def input_guess(expected_length: int) -> str:
    """This function will prompt the user for a guess and continue prompting until a guess of the expected length is given"""
    # Initial prompt
    guess = input(f"Enter a {expected_length} character word: ")
    # Keep prompting until the guess has the correct length
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")

    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns_left: int = 6
    won: bool = False
    turn_count: int = 1

    while turns_left > 0:
        print(f"=== Turn {turn_count}/6 ===")

        guess = input_guess(len(secret))
        result = emojified(guess, secret)
        print(result)

        if guess == secret:
            won = True  # Set won to True if the guess is correct

        turns_left -= 1
        turn_count += 1

        if won == True:  # If the user wins, exit while loop by setting turns_left to 0
            turns_left = 0

    if won == True:
        print(f"You won in {turn_count - 1}/6 turns!")
    else:
        print(f"X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
