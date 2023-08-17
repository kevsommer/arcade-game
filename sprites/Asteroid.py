from constants import *

asteroid_img = pygame.transform.scale(pygame.image.load("assets/asteroid.png"), (50, 50))

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
           self.kill() 