import project2
from dataclasses import dataclass

@dataclass
class MockInput:
    """
    A utility data class for mocking user input during testing.

    Attributes
    ----------
    test_rock_input : str
        Test case where player picks rock.
    test_paper_input : str
        Test case where player picks paper.
    test_scissors_input : str
        Test case where player picks scissors.
    test_lizard_input : str
        Test case where player picks lizard.
    test_spock_input : str
        Test case where player picks spock.
    """

    test_rock_input: str = '1'
    test_paper_input: str = '2'
    test_scissors_input: str = '3'
    test_lizard_input: str = '4'
    test_spock_input: str = '5'

@dataclass
class MockRandom:
    """
    A utility data class for mocking random numbers during testing.

    Attributes
    ----------
    test_rock_random : int
        Test case where computer picks rock.
    test_paper_random : int
        Test case where computer picks paper.
    test_scissors_random : int
        Test case where computer picks scissors.
    test_lizard_random : int
        Test case where computer picks lizard.
    test_spock_random : int
        Test case where computer picks spock.
    """

    test_rock_random: int = 1 
    test_paper_random: int = 2
    test_scissors_random: int = 3
    test_lizard_random: int = 4
    test_spock_random: int = 5

def test_RPSLS_game(mocker, capfd):
    """
    Test to verify the RPSLS game workflow and correctness from `project2.py`.

    This test ensures that the game randomly picks number, which refers to one of the five options, 
    prints correct outputs like 'I guessed...' as required, finds the winner correctly, 
    prints correct statements like 'scissors cuts paper' etc.
    
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
    Inputs_Mock = MockInput()
    Random_Mock = MockRandom()

    # Logic for checking if the game has random int for every game
    mocker.patch('project2.random.randint', return_value=Random_Mock.test_paper_random)
    mocker.patch('project2.input', side_effect=Inputs_Mock.test_rock_input)
    project2.main()
    out,err = capfd.readouterr()
    print(out)
    assert "I guessed paper" in out

    mocker.patch('project2.random.randint', return_value=Random_Mock.test_spock_random)
    mocker.patch('project2.input', side_effect=Inputs_Mock.test_spock_input)
    project2.main()
    out,err = capfd.readouterr()
    print(out)
    assert "I guessed spock" in out

    # Test 2: Checks if game has a correct logic for wins/loses/ties
    mocker.patch('project2.random.randint', return_value=Random_Mock.test_rock_random)
    mocker.patch('project2.input', side_effect=Inputs_Mock.test_rock_input)
    project2.main()
    out, err = capfd.readouterr()
    assert "Tie!" in out

    # Logic Win Paper over Rock
    mocker.patch('project2.random.randint', return_value=Random_Mock.test_rock_random)
    mocker.patch('project2.input', side_effect=Inputs_Mock.test_paper_input)
    project2.main()
    out, err = capfd.readouterr()
    assert "You win" in out

    # Logic Lose Rock over Scissors
    mocker.patch('project2.random.randint', return_value=Random_Mock.test_rock_random)
    mocker.patch('project2.input', side_effect=Inputs_Mock.test_scissors_input)
    project2.main()
    out, err = capfd.readouterr()
    assert "You lose" in out

    # Logic Lose Rock over Lizard
    mocker.patch('project2.random.randint', return_value=Random_Mock.test_rock_random)
    mocker.patch('project2.input', side_effect=Inputs_Mock.test_lizard_input)
    project2.main()
    out, err = capfd.readouterr()
    assert "You lose" in out

    # Logic Win Spocks over Rock
    mocker.patch('project2.random.randint', return_value=Random_Mock.test_rock_random)
    mocker.patch('project2.input', side_effect=Inputs_Mock.test_spock_input)
    project2.main()
    out, err = capfd.readouterr()
    assert "You win" in out

    # Test 3: Correct console outputs
    mocker.patch('project2.random.randint', return_value=Random_Mock.test_paper_random)
    mocker.patch('project2.input', side_effect=Inputs_Mock.test_scissors_input)
    project2.main()
    out, err = capfd.readouterr()
    assert 'I guessed paper' in out
    assert 'You win because scissors cuts paper' in out

    mocker.patch('project2.random.randint', return_value=Random_Mock.test_scissors_random)
    mocker.patch('project2.input', side_effect=Inputs_Mock.test_lizard_input)
    project2.main()
    out, err = capfd.readouterr()
    assert 'I guessed scissors' in out
    assert 'You lose because scissors decapitates lizard' in out