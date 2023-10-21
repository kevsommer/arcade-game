import math
from constants import *
from sprites.Bullet import Bullet
from sprites.TracingBullet import TracingBullet

enemy_img = pygame.transform.scale_by(pygame.transform.rotate(pygame.image.load("assets/enemies/enemy_asym.png"), 180), 1.25)

class AsymEnemy(pygame.sprite.Sprite):
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
            if (random.random() < 0.1):
                bullet = TracingBullet(self.spriteHandler.game, self.rect.centerx, self.rect.centery, 0.2, 1000)
                self.spriteHandler.add_bullet(bullet)