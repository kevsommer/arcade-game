from states.GameStateHandler import GameStateHandler

def test_GameStateHandler():
    testGameStateHandler = GameStateHandler()
    assert testGameStateHandler.score == 0

def test_updateScoreFunctionality():
    test_GameStateHandler = GameStateHandler()
    test_GameStateHandler.update_score(1)
    assert test_GameStateHandler.score == 1
    test_GameStateHandler.update_score(4)
    assert test_GameStateHandler.score == 5

def test_updateLivesFunctionality():
    test_GameStateHandler = GameStateHandler()
    test_GameStateHandler.update_lives(-1)
    assert test_GameStateHandler.lives == 2
    test_GameStateHandler.update_lives(1)
    assert test_GameStateHandler.lives == 3
