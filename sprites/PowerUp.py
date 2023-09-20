from constants import *

heart_bubble_img = pygame.image.load("assets/heart_bubble.png")
forcefield_bubble_img = pygame.image.load("assets/forcefield_bubble.png")
coin_img = pygame.image.load("assets/coin.png")
ammunition_bubble_img = pygame.image.load("assets/ammunition_bubble.png")

def get_img(type):
    if type == "heart":
        return heart_bubble_img
    elif type == "forcefield":
        return forcefield_bubble_img
    elif type == "coin":
        return coin_img
    elif type == "ammunition":
        return ammunition_bubble_img
    else:
        raise Exception("Invalid powerup type")

class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.type = random.choice(["heart", "forcefield", "coin", "ammunition"])
        self.image = get_img(self.type)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -200

    def update(self):
        self.rect.y += ASTEROID_SPEED
        if self.rect.top > HEIGHT:
            self.kill()