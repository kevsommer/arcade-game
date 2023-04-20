from constants import *
from sprites.Bullet import Bullet


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen, sprite_handler):
        super().__init__()
        self.image = spaceship_img
        self.screen = screen
        self.sprite_handler = sprite_handler
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        # Initialize timer for bullet spawning
        self.last_bullet_time = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= SPACESHIP_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += SPACESHIP_SPEED
        if keys[pygame.K_UP]:
            self.rect.y -= SPACESHIP_SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y += SPACESHIP_SPEED

        if keys[pygame.K_SPACE]:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_bullet_time > MIN_BULLET_INTERVAL:
                self.last_bullet_time = current_time

                bullet = Bullet(self.rect.centerx, self.rect.top)
                self.sprite_handler.add_bullet(bullet)

        self.rect.clamp_ip(self.screen.get_rect())
