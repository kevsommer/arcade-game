from constants import *
from sprites.Bullet import Bullet

enemy_img = pygame.transform.scale_by(pygame.transform.rotate(pygame.image.load("assets/enemy_alt.png"), 180), 1.25)

class AltEnemy(pygame.sprite.Sprite):
    def __init__(self, x: int, spriteHandler):
        super().__init__()
        self.image = enemy_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = random.randint(-100, -50)
        self.spriteHandler = spriteHandler
        self.last_bullet_time = 0

    def update(self):
        self.rect.y += ENEMY_SPEED
        if self.rect.top > HEIGHT:
            self.kill()

        current_time = pygame.time.get_ticks()
        if current_time - self.last_bullet_time > MIN_BULLET_INTERVAL * 2:
            self.last_bullet_time = current_time
            if (random.random() < 0.2):

                bullet = Bullet(self.rect.centerx - 0.35 * self.rect.width, self.rect.centery, type="enemy")
                self.spriteHandler.add_bullet(bullet)
                bullet = Bullet(self.rect.centerx + 0.35 * self.rect.width, self.rect.centery, type="enemy")
                self.spriteHandler.add_bullet(bullet)