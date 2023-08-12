from constants import *

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, type: str):
        super().__init__()
        self.images = []
        for i in range(8):
            img = pygame.image.load(f"assets/{type}_explosion/explosion_{i}.png")
            img = pygame.transform.scale(img, (100, 100))
            self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0
        self.index = 0
    
    def update(self):
        self.counter += 1
        if (self.counter == 8):
            self.index += 1
            if (self.index) == len(self.images):
                self.index = 0
                self.kill()
            self.image = self.images[self.index]
            self.counter = 0

    def draw(self, screen):
        screen.blit(self.image[self.counter // 8], self.rect)
