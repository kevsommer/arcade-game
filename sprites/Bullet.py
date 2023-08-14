from constants import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, type='player'):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.type = type

    def update(self):
        if (self.type == 'player'):
            self.rect.y -= BULLET_SPEED
        else:
            self.rect.y += BULLET_SPEED * 0.5

        if self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()
