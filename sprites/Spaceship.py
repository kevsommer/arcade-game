from constants import *
from sprites.Bullet import Bullet

spaceship_alt_center_img = pygame.transform.scale(pygame.image.load('assets/spaceship_alt/spaceship_alt_center.png'), (68, 80))
spaceship_alt_left_img = pygame.transform.scale(pygame.image.load('assets/spaceship_alt/spaceship_alt_left.png'), (68, 80))
spaceship_alt_right_img = pygame.transform.scale(pygame.image.load('assets/spaceship_alt/spaceship_alt_right.png'), (68, 80))

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen, game):
        super().__init__()
        self.screen = screen
        self.game = game

        self.image = spaceship_alt_center_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        # Initialize timer for bullet spawning
        self.last_bullet_time = 0

    def update(self):
        keys = pygame.key.get_pressed()
        self.image = spaceship_alt_center_img
        if keys[pygame.K_LEFT]:
            self.rect.x -= SPACESHIP_SPEED
            self.image = spaceship_alt_left_img
        if keys[pygame.K_RIGHT]:
            self.rect.x += SPACESHIP_SPEED
            self.image = spaceship_alt_right_img
        if keys[pygame.K_UP]:
            self.rect.y -= SPACESHIP_SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y += SPACESHIP_SPEED
        self.mask = pygame.mask.from_surface(self.image)

        if keys[pygame.K_SPACE]:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_bullet_time > MIN_BULLET_INTERVAL:
                self.last_bullet_time = current_time

                bullet = Bullet(self.rect.centerx, self.rect.top, type='player')
                self.game.spriteHandler.add_bullet(bullet)
                self.game.gameStateHandler.ammunition -= 1

        self.rect.clamp_ip(self.screen.get_rect())

    def reset(self):
        self.game.spriteHandler.add_explosion(center=self.rect.center, type='enemy')
        self.image = spaceship_alt_center_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.last_bullet_time = 0
