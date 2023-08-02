class GameStateHandler():
    def __init__(self) -> None:
        self.running: bool = True
        self.score: int = 0
        self.lives: int = 3
        self.background_pos: float = -2200
        self.ammunition: int = 100

    def update(self):
        if (self.lives < 0):
            self.running = False
        self.background_pos += 0.5
