import project2
from dataclasses import dataclass

@dataclass
class MockInput:
    """A utility data class for mocking user input during testing.

    Attributes
    ----------
    test_some_input : str
        Test case where player picks rock.
    """

    test_some_input: str = '1'  # Test case where player picks rock

def test_randomness_of_computer_guess(mocker):
    """Test the randomness of computer's guess by checking a set of 1000 guesses."""
    
    Mock_Input = MockInput()

    guesses = set()
    mocker.patch('project2.input', return_value=Mock_Input.test_some_input)

    for _ in range(1000):
        game = project2.GamesRules()
        guesses.add(game.computer_guess)

    assert len(guesses) >= 3

def test_game_logic(mocker, capfd):
    """Test the game logic based on RPSLS rules.
    
    The function patches the input and random.randint functions from project2 
    and checks the game's logic for certain matchups.
    """
    
    matchups = [
        (1, 3), (1, 4),  # Rock wins
        (2, 1), (2, 5),  # Paper wins
        (3, 2), (3, 4),  # Scissors wins
        (4, 2), (4, 5),  # Lizard wins
        (5, 1), (5, 3)   # Spock wins
    ]

    for player, computer in matchups:
        mocker.patch('project2.input', return_value=str(player))
        mocker.patch('project2.random.randint', return_value=computer)
        project2.main()
        
        out, _ = capfd.readouterr()
        assert 'You win' in out

def test_game_output_messages(mocker, capfd):
    """Test the game's output messages for various game outcomes.

    The function patches the input and random.randint functions from project2 
    and checks the game's output messages for each matchup in test_data.
    
    Parameters
    ----------
    mocker : object
        The mock object used to replace real functions or methods with mock calls.
    capfd : object
        Capture, as text, output to file descriptors 1 and 2.
        
    Notes
    -----
    The test checks if both the computer's move and the game outcome message 
    are correctly printed to the console.
    """
    
    test_data = [
        (1, 3, 'I guessed scissors', 'You win because rock crushes scissors'),
        (1, 4, 'I guessed lizard', 'You win because rock crushes lizard'),
        (1, 1, 'I guessed rock','Tie! We both guessed rock'),
        (3, 2, 'I guessed paper', 'You win because scissors cuts paper'),
        (3, 4, 'I guessed lizard', 'You win because scissors decapitates lizard')
        # Add other combinations as needed
    ]

    for player, computer, computer_message, outcome_message in test_data:
        mocker.patch('project2.input', return_value=str(player))
        mocker.patch('project2.random.randint', return_value=computer)
        
        project2.main()
        
        out, _ = capfd.readouterr()
        assert computer_message in out
        assert outcome_message in out
