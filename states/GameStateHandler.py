class GameStateHandler():
    def __init__(self) -> None:
        self.score = 0
        self.lives = 3
        self.background_pos = -2200
        self.ammunition = 100

    def update_score(self, amount: int):
        self.score += amount

    def update_lives(self, amount: int):
        self.lives += amount

    def update_background_position(self):
        self.background_pos += 0.5
