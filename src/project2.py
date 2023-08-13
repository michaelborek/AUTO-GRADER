import random

class GamesRules:
    """
    Represents the game logic and rules for Rock Paper Scissors Lizard Spock (RPSLS).

    This class provides mappings for game options to their respective numbers, as well as 
    the rules that determine the winner based on the chosen options.

    Attributes
    ----------
    RPSLS_dict : dict of {int: str}
        A mapping of integers (1-5) to their corresponding game options.
    RPSLS_rules_dict : dict of {str: dict}
        Rules that define which option defeats which in a dictionary format. 
        For example, 'rock' key has a dictionary value showing it 'crushes' 'lizard' and 'scissors'.
    computer_guess : int
        A random integer between 1 and 5, representing the computer's game option guess.
    computer_guess_name : str
        The textual representation (name) of the game option that the computer guessed.

    Methods
    -------
    __init__():
        Initialize a new instance, setting computer's guess and its name.
    """
    
    RPSLS_dict = {1: 'rock', 2: 'paper', 3: 'scissors', 4: 'lizard', 5: 'spock'}

    RPSLS_rules_dict = {
        "rock": {
            "lizard": "crushes",
            "scissors": "crushes"
        },
        "paper": {
            "rock": "covers",
            'spock': "disproves"
        },
        "scissors": {
            "paper": "cuts",
            'lizard': "decapitates"
        },
        "lizard": {
            "spock": "poisons",
            "paper": "eats"
        },
        "spock": {
            "scissors": "smashes",
            "rock": "vaporizes"
        }
    }

    def __init__(self):
        """
        Constructs a new GamesRules instance and sets the computer's guess and its corresponding name.
        """
        self.computer_guess = random.randint(1, 5)
        self.computer_guess_name = GamesRules.RPSLS_dict[self.computer_guess]

def main():
    """
    Implements the logic of the RPSLS (Rock Paper Scissors Lizard Spock) game.

    In this game, the player is asked to pick a number between 1 and 5 (inclusive), each corresponding to a
    choice of rock, paper, scissors, lizard, or spock. The computer also randomly selects a number, and a game
    between the computer-generated and player-generated numbers is played. The game provides feedback, indicating
    whether the player won or lost, or if it's a tie.

    Parameters
    ----------
    None

    Returns
    -------
    None

    User Interaction
    ----------------
    The game prompts the user to pick a number between 1 and 5, where each number corresponds to an option 
    (rock, paper, scissors, lizard, or spock).

    Depending on the player's and the computer's choices, the game will announce the results:
    - 'You win' if the player's choice beats the computer's.
    - 'You lose' if the computer's choice beats the player's.
    - 'Tie' if both the player and the computer make the same choice.
    """
    game = GamesRules() # Creates an instance of the GamesRules class

    player_guess_str = input('Enter your guess (1 for rock, 2 for paper, 3 for scissors, 4 for lizard, 5 for spock): ') # Player's choice
    player_guess_int = int(player_guess_str) # Converts the player's guess to an integer
    player_guess_name = game.RPSLS_dict[player_guess_int] # Chooses name from the dict

    print(f'I guessed {game.computer_guess_name}') # Prints tense with computers pick

    # If-else statements to check if the player's guess is higher, lower or equal to the secret number
    if player_guess_name == game.computer_guess_name:
        print(f'Tie! We both guessed {player_guess_name}.') # Tie logic information
    elif player_guess_name in game.RPSLS_rules_dict[game.computer_guess_name]:
        print(f'You lose because {game.computer_guess_name} {game.RPSLS_rules_dict[game.computer_guess_name][player_guess_name]} {player_guess_name}') # Prints 'You lose' if the computer's choice beats the player's
    else:
        print(f'You win because {player_guess_name} {game.RPSLS_rules_dict[player_guess_name][game.computer_guess_name]} {game.computer_guess_name}') # Prints 'You win' if the player's choice beats the computer's

if __name__ == '__main__':
    main()