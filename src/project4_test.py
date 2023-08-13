import project4
import random

def test_input(mocker, monkeypatch):
    """
    Test if the program asks the correct guiding question to the user.
    
    This test function mocks the input for the main game menu in `project4`. It checks 
    if the game prompts the user with the correct question when choosing a game.

    Parameters
    ----------
    mocker : object
        An object for creating patches in pytest.
    monkeypatch : object
        A utility to conveniently modify or override classes and functions during testing.

    Returns
    -------
    None
    """
    # Mock input calls
    inputs = iter(['1', 'quit'])
    input_mock = mocker.patch('project4.input', side_effect=inputs)

    # Mock NumGuess call
    monkeypatch.setattr('project4.NumGuess', lambda: None)

    # Call main function
    project4.main()

    # Assert that the input prompt was displayed correctly
    input_mock.assert_any_call('Which game do you want to play 1 for NumGuess, 2 for RPSLS, 3 for QuizGame. ')

def test_game_correctness(mocker, capfd):
    """
    Test if the program correctly picks and runs the chosen game.

    This test function mocks the input and random seed to control the flow of `project4`. It 
    checks if the game correctly picks the QuizGame and processes the answers correctly.

    Parameters
    ----------
    mocker : object
        An object for creating patches in pytest.
    capfd : object
        Captures the stdout and stderr.

    Returns
    -------
    None
    """
    random.seed(200)
    inputs = iter(['3', '4', 'quit'])
    input_mock = mocker.patch('project4.input', side_effect=inputs)

    project4.main()

    out, err = capfd.readouterr()

    # Some outputs to confirm if game runs correctly
    assert 'Name Something You Might Do With Your Days Off Around Christmas?' in out
    assert 'Shop was the answer you selected.\nComing in at 43 %!\nYou are correct!\nThe correct answer is Shop with a 43 %.' in out

def test_fluency(mocker, capfd):
    """
    Test the fluency of the program.

    This test checks if the program runs smoothly through various game sequences and does 
    not break until the user quits.

    Parameters
    ----------
    mocker : object
        An object for creating patches in pytest.
    capfd : object
        Captures the stdout and stderr.

    Returns
    -------
    None
    """
    # Some random seed
    random.seed(1000)
    # Random inputs which simulate a user's sequence for the game
    inputs = iter(['3','2','1','2','2','2','2','2','2','2','3','2','2','quit'])

    mocker.patch('project4.input', side_effect=inputs)

    project4.main()

    # With the captured output, we can check if the program is still running as expected
    out, err = capfd.readouterr()
