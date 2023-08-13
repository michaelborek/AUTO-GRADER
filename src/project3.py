import random

class GamesRules:
    """
    Represents a game rule set with a randomly determined integer value.

    This class initializes a random number from a predefined interval, which can be 
    used in the gameplay or game's logic.

    Attributes
    ----------
    rand_int : int
        A random number chosen from the interval [1, 1049].

    Methods
    -------
    __init__():
        Initialize a new instance, generating a random integer for gameplay.
    """

    def __init__(self):
        """
        Constructs a new GamesRules instance and sets a random integer value for gameplay.
        """
        self.rand_int = random.randint(1, 1049)

def main():
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
    games_rules = GamesRules()  # Creates an instance of the GamesRules class

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

if __name__ == '__main__':
    main()