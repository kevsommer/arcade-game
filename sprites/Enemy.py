from constants import *
from sprites.Bullet import Bullet

enemy_img = pygame.transform.scale(pygame.image.load("assets/enemy.png")), (100, 73))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x: int, spriteHandler):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = random.randint(-100, -50)
        self.spriteHandler = spriteHandler
        self.last_bullet_time = 0

    def update(self):
        self.rect.y += ENEMY_SPEED
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -50)

        current_time = pygame.time.get_ticks()
        if current_time - self.last_bullet_time > MIN_BULLET_INTERVAL * 4:
            self.last_bullet_time = current_time
            if (random.random() < 0.1):

                bullet = Bullet(self.rect.centerx, self.rect.bottom, type="enemy")
                self.spriteHandler.add_bullet(bullet)