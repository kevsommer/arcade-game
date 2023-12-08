from constants import *
from sprites.Bullet import Bullet

spaceship_alt_center_img = pygame.transform.scale(pygame.image.load('assets/spaceship_alt/spaceship_alt_center.png'), (68, 80))
spaceship_alt_left_img = pygame.transform.scale(pygame.image.load('assets/spaceship_alt/spaceship_alt_left.png'), (68, 80))
spaceship_alt_right_img = pygame.transform.scale(pygame.image.load('assets/spaceship_alt/spaceship_alt_right.png'), (68, 80))

spaceship_alt_center_forcefield_img = pygame.transform.scale(pygame.image.load('assets/spaceship_alt/spaceship_alt_center_forcefield.png'), (128, 128))
spaceship_alt_left_forcefield_img = pygame.transform.scale(pygame.image.load('assets/spaceship_alt/spaceship_alt_left_forcefield.png'), (128, 128))
spaceship_alt_right_forcefield_img = pygame.transform.scale(pygame.image.load('assets/spaceship_alt/spaceship_alt_right_forcefield.png'), (128, 128))  

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game

        self.image = spaceship_alt_center_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        # Initialize timer for bullet spawning
        self.last_bullet_time = 0
        self.direction = 'center'

    def get_img(self):
        if self.game.gameStateHandler.forcefield:
            if self.direction == 'left':
                return spaceship_alt_left_forcefield_img
            elif self.direction == 'right':
                return spaceship_alt_right_forcefield_img
            else:
                return spaceship_alt_center_forcefield_img
        else:
            if self.direction == 'left':
                return spaceship_alt_left_img
            elif self.direction == 'right':
                return spaceship_alt_right_img
            else:
                return spaceship_alt_center_img
            
    def update(self):
        keys = pygame.key.get_pressed()
        self.direction = 'center'
        if keys[pygame.K_LEFT]:
            self.rect.x -= SPACESHIP_SPEED
            self.direction = 'left'
        if keys[pygame.K_RIGHT]:
            self.rect.x += SPACESHIP_SPEED
            self.direction = 'right'
        if keys[pygame.K_UP]:
            self.rect.y -= SPACESHIP_SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y += SPACESHIP_SPEED
            
        self.image = self.get_img()
        self.mask = pygame.mask.from_surface(self.image)

        if keys[pygame.K_SPACE]:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_bullet_time > MIN_BULLET_INTERVAL and self.game.gameStateHandler.ammunition > 0:
                self.last_bullet_time = current_time

                bullet = Bullet(self.rect.centerx, self.rect.top, type='player')
                self.game.spriteHandler.add_bullet(bullet)
                self.game.gameStateHandler.ammunition -= 1

        self.rect.clamp_ip(self.game.screen.get_rect())

    def reset(self):
        self.game.spriteHandler.add_explosion(center=self.rect.center, type='enemy')
        self.image = spaceship_alt_center_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.last_bullet_time = 0
