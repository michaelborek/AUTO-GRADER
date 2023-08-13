import random
import project1
import project2
import project3

def NumGuess():
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
    games_rules = project1.GamesRules() # Creates an instance of the GamesRules class

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

def RPSLS():
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
    game = project2.GamesRules() # Creates an instance of the GamesRules class

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

def QuizGame():
    """
    Implements the logic of the QuizGame.

    The game reads a question bank from a data file, where each question has multiple answers with 
    their respective percentages. The computer randomly selects a question from the bank. The player 
    is then presented with five answers in a random order and has to pick one. The game provides 
    feedback, indicating whether the player selected the most popular answer and its percentage.

    The game uses the `random.randint` function from the `random` module to select a random question 
    from the question bank.

    It also uses the built-in `open` function to read the data file.

    Parameters
    ----------
    None

    Returns
    -------
    None

    User Interaction
    ----------------
    The game prompts the user to select an answer between 1 and 5, where each number corresponds to 
    a different answer option.

    Depending on the player's choice and the popularity of the selected answer, the game will announce the results:
    - 'You are correct' if the player's choice has the highest percentage.
    - 'You are incorrect' if the player's choice doesn't have the highest percentage.

    File Interaction
    ----------------
    The game interacts with a data file 'data.txt' which is expected to be in the same directory. This 
    file is assumed to contain a bank of questions, with each question having multiple answers, 
    each with their respective popularity percentage. Each question and its answers are expected 
    to be on a new line in the data file.
    """
    games_rules = project3.GamesRules()  # Creates an instance of the GamesRules class

    # Reads the data file
    with open('data.txt', 'r') as f:
        lines = f.readlines()  # Reads all lines at once

    quiz_row = lines[games_rules.rand_int]  # Directly accesses the required line

    question = quiz_row.split('\t')  # Splits file
    question[-1] = question[-1].replace('\n', '')  # Replaces last element's \n

    correct_answer = question[1]  # Correct answer
    answer_list = [question[i] for i in range(1,10, 2)]  # Adds answers to the list/ skips percentage

    random.shuffle(answer_list)  # Shuffles list

    print()
    print(question[0])  # Prints a question
    print()

    # Prints nice answers table
    for i, answer in enumerate(answer_list):
        print(f'{i+1}  {answer}')

    print()
    guess = int(input('What is your guess: '))  # Asks for number
    print(f'{answer_list[guess-1]} was the answer you selected.')  # Prints text
    index_of_answer = question.index(answer_list[guess - 1])  # Gets the index of the chosen number to find its percentage
    print(f'Coming in at {question[index_of_answer + 1]} %!')  # Prints text

    # Logic for correct/incorrect
    if answer_list[guess - 1]==correct_answer:
        print('You are correct!')
    else:
        print('You are incorrect.')

    # Prints last text
    print(f'The correct answer is {correct_answer} with a {question[2]} %.')

def main():
    game = input('Which game do you want to play 1 for NumGuess, 2 for RPSLS, 3 for QuizGame. ')

    while game != 'quit':

        if game == '1':
            NumGuess()
        elif game == '2':
            RPSLS()
        elif game == '3':
            QuizGame()
        
        game = input('Which game do you want to play 1 for NumGuess, 2 for RPSLS, 3 for QuizGame. Type quit to leave. ')

if __name__ == '__main__':
    main()