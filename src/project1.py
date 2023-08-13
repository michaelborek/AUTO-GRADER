import random

class GamesRules:
    """
    Represents the game's rule set with a randomly generated secret number.

    This class provides a defined number of maximum guesses allowed and 
    randomly determines a secret number for gameplay.

    Attributes
    ----------
    maximum_guesses : int
        The maximum number of allowed guesses.
    secret_number : int
        A randomly generated number between 0 and 99 that the player has to guess.

    Methods
    -------
    __init__():
        Initialize a new instance, generating a secret number for gameplay.
    """
    
    maximum_guesses = 6

    def __init__(self):
        """
        Constructs a new GamesRules instance and sets the secret number.
        """
        self.secret_number = random.randint(0, 99)


def main():
    """
    Implements the logic of the NumGame.

    In this game, the player is asked to guess a secret number that is randomly selected 
    between 0 and 99 (inclusive). For each guess made by the player, the game provides feedback, 
    informing the player if the secret number is 'Higher' or 'Lower' than the number guessed.

    The player is allowed a maximum of 6 guesses to identify the secret number. The game ends 
    either when the player has successfully guessed the secret number or when the player has 
    exhausted all of their available guesses.

    The game uses the `random.randint` function from the `random` module to generate the secret number.

    Parameters
    ----------
    None

    Returns
    -------
    None

    User Interaction
    ----------------
    Asks the user to guess a number between 0 and 99.

    If the guessed number is less than the secret number, it prints 'Higher' and the number of remaining guesses.
    If the guessed number is greater than the secret number, it prints 'Lower' and the number of remaining guesses.
    If the guessed number is equal to the secret number, it prints 'Correct' and the game ends.

    If all guesses are exhausted, it reveals the secret number and ends the game.
    """
    games_rules = GamesRules() # Creates an instance of the GamesRules class

    print(f'Guess a number between 0 and 99') # Asks the user to guess a number between 0 and 99

    guess_counter = 1 # Counter for number of guesses

    # While loop to check if the player's guess is higher, lower or equal to the secret number
    while guess_counter <= games_rules.maximum_guesses:
        player_guess = input('What is your guess? ') # Asks the user for their guess
        player_number = int(player_guess) # Converts the player's guess to an integer

        # If-else statements to check if the player's guess is higher, lower or equal to the secret number
        if player_number < games_rules.secret_number:
            print(f'Higher') # Prints 'Higher' if the player's guess is lower than the secret number
            print(f'You have {games_rules.maximum_guesses-guess_counter} number of guesses.') # Prints the number of remaining guesses
            guess_counter += 1 # Increments the guess counter by 1
        elif player_number > games_rules.secret_number:
            print(f'Lower') # Prints 'Lower' if the player's guess is higher than the secret number
            print(f'You have {games_rules.maximum_guesses-guess_counter} number of guesses.') # Prints the number of remaining guesses
            guess_counter +=1 # Increments the guess counter by 1
        else:
            print(f'Correct') # Prints 'Correct' if the player's guess is equal to the secret number
            break
    else:
        print(f'You lost') # Prints 'You lost' if the player exhausts all available guesses
        print(f'Secret number was', games_rules.secret_number) # Prints the secret number

if __name__ == '__main__':
    main()