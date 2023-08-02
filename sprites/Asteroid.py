from constants import *


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = asteroid_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = random.randint(-200, -100)

    def update(self):
        self.rect.y += ASTEROID_SPEED
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-200, -100)
