import project3
import random
from dataclasses import dataclass

@dataclass
class MockRandomQuestions:
    """
    A utility data class for mocking random questions during testing.

    Attributes
    ----------
    test_question_1 : int
        A predetermined random question.
    test_question_2 : int
        Another predetermined random question.
    test_question_3 : int
        Another predetermined random question.
    test_question_4 : int
        Another predetermined random question.
    """
    test_question_1 : int = 200
    test_question_2 : int = 300
    test_question_3 : int = 942
    test_question_4 : int = 942

@dataclass
class MockInput:
    """
    A utility data class for mocking user input during testing.

    Attributes
    ----------
    test_input_1 : str
        Mocked input.
    test_input_2 : str
        Another mocked input.
    test_input_3 : str
        Another mocked input.
    test_input_4 : str
        Another mocked input.
    """
    test_input_1 : str = '1'
    test_input_2 : str = '1'
    test_input_3 : str = '1'
    test_input_4 : str = '5'

@dataclass
class MockSeed:
    """
    A utility data class for mocking random seeds during testing.

    Attributes
    ----------
    test_seed_1 : int
        Mocked seed value.
    """
    test_seed_1 : int = 200

# Test 1: Checks if computer guesses are random (not hard-coded)
def test_computer_guess(mocker, capfd):
    """
    Test the Quiz game's workflow and correctness from `project3.py`.

    Parameters
    ----------
    mocker : fixture
        A pytest fixture for mocking. Used to mock `input` and `random.randint`.
    capfd : fixture
        A pytest fixture to capture stdout and stderr.

    Returns
    -------
    None
    """
    mock_random_questions = MockRandomQuestions()  # Creates an instance of the MockRandomQuestions class
    mock_input = MockInput()  # Creates an instance of the MockInput class

    mocker.patch('project3.random.randint', return_value=mock_random_questions.test_question_1)
    mocker.patch('project3.input', return_value=mock_input.test_input_1)
    project3.main()
    out, err = capfd.readouterr()
    question1 = out[:15]
    
    mocker.patch('project3.random.randint', return_value=mock_random_questions.test_question_2)
    mocker.patch('project3.input', return_value=mock_input.test_input_2)
    project3.main()
    out, err = capfd.readouterr()
    question2 = out[:15]
    
    assert question1 != question2

    # Checks if program prints appropriate messages
    mocker.patch('project3.random.randint', return_value=mock_random_questions.test_question_3)
    project3.main()

    out, err = capfd.readouterr()

    # Checks if program print all of the required messages
    assert 'was the answer you selected' in out 
    assert 'Coming in at' in out
    assert 'You are correct!' in out or 'You are incorrect.' in out
    assert 'The correct answer is' in out
    assert 'with a' in out 

def test_random_shuffle(mocker, capfd):
    """
    Test to check if the game shuffles the answers correctly.

    Parameters
    ----------
    mocker : fixture
        A pytest fixture for mocking. Used to mock `input` and `random.randint`.
    capfd : fixture
        A pytest fixture to capture stdout and stderr.

    Returns
    -------
    None
    """
    mock_input = MockInput() # Creates an instance of the MockInput class
    mock_seed = MockSeed() # Creates an instance of the MockSeed class
    mock_random_questions = MockRandomQuestions() # Creates an instance of the MockRandomQuestions class

    # Checks if user correctly shuffled list where correct answer is not at the first position
    random.seed(mock_seed.test_seed_1)
    mocker.patch('project3.random.randint', return_value=mock_random_questions.test_question_4)
    mocker.patch('project3.input', side_effect=mock_input.test_input_4)
    project3.main()
    out, err = capfd.readouterr()

    assert 'You are correct!' in out
    assert 'The correct answer is High Heels with a 45 %.' in out
