class GameStateHandler():
    def __init__(self) -> None:
        self.score: int = 0
        self.lives: int = 3
        self.background_pos: float = -2200
        self.ammunition: int = 100

    def update_score(self, amount: int):
        self.score += amount

    def update_lives(self, amount: int):
        self.lives += amount

    def update_background_position(self):
        self.background_pos += 0.5
