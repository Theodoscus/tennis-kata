class TennisGame:
    points = ["Love", "15", "30", "40"]

    def __init__(self):
        self.player1 = 0
        self.player2 = 0

    def player1_scores(self):
        self.player1 += 1
    
    def player2_scores(self):
        self.player2 += 1

    def score(self):
        difference = self.player1 - self.player2

        if self.player1 >= 4 and difference >= 2:
            return "Win for Player 1"

        if self.player2 >= 4 and difference <= -2:
            return "Win for Player 2"

        # From 40-40 onwards, the difference decides deuce or advantage.
        if self.player1 >= 3 and self.player2 >= 3:
            if difference == 0:
                return "Deuce"

            if difference == 1:
                return "Advantage Player 1"

            if difference == -1:
                return "Advantage Player 2"

        if self.player1 == self.player2:
            return f"{self.points[self.player1]}-All"

        return f"{self.points[self.player1]}-{self.points[self.player2]}"

#Tests for TennisGame class

#Basic scoring tests
def test_new_game():
    game = TennisGame()

    assert game.score() == "Love-All"

def test_player1_scoring():
    game = TennisGame()

    game.player1_scores()
    assert game.score() == "15-Love"

    game.player1_scores()
    assert game.score() == "30-Love"

    game.player1_scores()
    assert game.score() == "40-Love"

def test_player2_scoring():
    game = TennisGame()

    game.player2_scores()
    assert game.score() == "Love-15"

    game.player2_scores()
    assert game.score() == "Love-30"

    game.player2_scores()
    assert game.score() == "Love-40"

def test_mixed_score():
    game = TennisGame()

    game.player1_scores()
    game.player1_scores()
    game.player2_scores()

    assert game.score() == "30-15"


def test_equal_score():
    game = TennisGame()

    game.player1_scores()
    game.player1_scores()
    game.player2_scores()
    game.player2_scores()

    assert game.score() == "30-All"

#Deuce and advantage tests
    
def test_deuce():
    game = TennisGame()
    
    for _ in range(3):
        game.player1_scores()
        game.player2_scores()

    assert game.score() == "Deuce"

def test_advantage_player1():
    game = TennisGame()

    for _ in range(3):
        game.player1_scores()
        game.player2_scores()

    game.player1_scores()

    assert game.score() == "Advantage Player 1"

def test_advantage_player2():
    game = TennisGame()

    for _ in range(3):
        game.player1_scores()
        game.player2_scores()

    game.player2_scores()

    assert game.score() == "Advantage Player 2"

def test_back_to_deuce():
    game = TennisGame()

    for _ in range(3):
        game.player1_scores()
        game.player2_scores()

    game.player1_scores()
    game.player2_scores()

    assert game.score() == "Deuce"
    
def test_player1_wins():
    game = TennisGame()

    for _ in range(4):
        game.player1_scores()

    assert game.score() == "Win for Player 1"


def test_player2_wins():
    game = TennisGame()

    for _ in range(4):
        game.player2_scores()

    assert game.score() == "Win for Player 2"