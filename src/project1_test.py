import project1
from dataclasses import dataclass, field

@dataclass
class MockInput:
    """
    A utility data class for mocking user input during testing.

    Attributes
    ----------
    test_input_list_1 : list[str]
        A list of test inputs to simulate player guesses.
    test_input_list_2 : list[str]
        A different set of test inputs to simulate player guesses.
    test_input_list_3 : list[str]
        Another set of test inputs to simulate player guesses.
    """
    test_input_list_1: list = field(default_factory=lambda: ['50', '40', '30', '20', '10', '0'])
    test_input_list_2: list = field(default_factory=lambda: ['30', '80', '90', '50', '50', '50', '50'])
    test_input_list_3: list = field(default_factory=lambda: ['28', '40', '90'])

@dataclass
class MockRandom:
    """
    A utility class for mocking random number generation during testing.

    Attributes
    ----------
    test_random_number_1 : int
        A predetermined test random number.
    test_random_number_2 : int
        Another predetermined test random number.
    test_random_number_3 : int
        Another predetermined test random number.
    """
    test_random_number_1: int = 70
    test_random_number_2: int = 85
    test_random_number_3: int = 90

def test_NumGame(mocker, capfd):
    """
    Test the NumGame from `project1.py`.

    This function tests the workflow and correctness of the NumGame. It verifies that 
    the game accurately reads the player's guesses, provides feedback, 
    and concludes the game appropriately.

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
    Inputs_Mock = MockInput() # Creates an instance of the MockInput class
    Random_Mock = MockRandom() # Creates an instance of the MockRandom class
    games_rules = project1.GamesRules() # Creates an instance of the GamesRules class

    # Checks if user has correctly set random number range
    for i in range(1000000):  # Repeat test 1000000 times for good measure
        assert 0 <= games_rules.secret_number <= 99, "Secret number is out of range!"

    mocker.patch('project1.random.randint', return_value=Random_Mock.test_random_number_1)
    mocker.patch('project1.input', side_effect=Inputs_Mock.test_input_list_1)
    project1.main()
    # Assertions as required
    out, err = capfd.readouterr()
    assert 'You lost' in out, "Expected 'You lost' in the output, but it was missing."
    assert 'Secret number was' in out, "Expected 'Secret number was' in the output, but it was missing." 
    assert 'You have 0 number of guesses.' in out, "Expected 'You have 0 number of guesses.' in the output, but it was missing."

    # Checks if the game reads 'playerguess' and prints wanted results
    mocker.patch('project1.random.randint', return_value=Random_Mock.test_random_number_2)
    mocker.patch('project1.input', side_effect=Inputs_Mock.test_input_list_2)
    project1.main()
    out, err = capfd.readouterr()
    # Assertions as required
    assert 'Higher' in out, "Expected 'Higher' in the output, but it was missing."
    assert 'Lower' in out, "Expected 'Lower' in the output, but it was missing."
    assert 'You have 5 number of guesses.' in out, "Expected 'You have 5 number of guesses' in the output, but it was missing."
    assert 'You have 4 number of guesses.' in out, "Expected 'You have 4 number of guesses' in the output, but it was missing."

    # Checks if the game ends when the player guesses the correct number
    mocker.patch('project1.random.randint', return_value=Random_Mock.test_random_number_3)
    mocker.patch('project1.input', side_effect=Inputs_Mock.test_input_list_3)
    project1.main()
    out, err = capfd.readouterr()
    assert 'Correct' in out, "Expected 'Correct' in the output, but it was missing."
