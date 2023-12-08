import random

class GameStateHandler():
    def __init__(self) -> None:
        self.running: bool = True
        self.score: int = 0
        self.lives: int = 3
        self.background_pos: float = -2200
        self.ammunition: int = 100
        self.forcefield = True
        self.forcefield_timer = 0

        self.camera_offset = [0, 0]
        self.shake_duration = 0
        self.shake_intensity = 0

    def update(self):
        if self.forcefield:
            self.forcefield_timer += 1
            if self.forcefield_timer > 300:
                self.forcefield = False
                self.forcefield_timer = 0
                
        if (self.lives < 0):
            self.running = False
        self.background_pos += 0.5
        self.update_camera()

    def shake_camera(self, duration, intensity):
            self.shake_duration = duration
            self.shake_intensity = intensity

    def update_camera(self):
        if self.shake_duration > 0:
            self.camera_offset = [random.randint(-self.shake_intensity, self.shake_intensity), random.randint(-self.shake_intensity, self.shake_intensity)]
            self.shake_duration -= 1
        else:
            self.camera_offset = [0, 0]