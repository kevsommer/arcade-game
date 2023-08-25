from constants import *

heart_bubble_img = pygame.image.load("assets/heart_bubble.png")
forcefield_bubble_img = pygame.image.load("assets/forcefield_bubble.png")

class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.type = random.choice(["heart", "forcefield"])
        self.image = heart_bubble_img if self.type == "heart" else forcefield_bubble_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -200

    def update(self):
        self.rect.y += ASTEROID_SPEED
        if self.rect.top > HEIGHT:
            self.kill()