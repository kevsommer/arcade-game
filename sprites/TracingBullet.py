import math
import pygame

class TracingBullet(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface, game, x: int, y: int, speed: int, delay: int):
        super().__init__()

        self.screen = screen
        self.game = game
        self.image = pygame.image.load('assets/bullets/enemy_bullet.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.delay = delay
        self.last_player_pos = game.spriteHandler.spaceship.rect.center
        self.time_since_player_moved = 0
        self.type = 'tracing'
        self.lifetime = 0
    

    def update(self):
        self.lifetime += self.game.dt
        if self.lifetime >= 5000:
            self.kill()
        self.time_since_player_moved += self.game.dt
        if self.time_since_player_moved >= self.delay:
            self.last_player_pos = self.game.spriteHandler.spaceship.rect.center
            self.time_since_player_moved = 0

        dx = self.last_player_pos[0] - self.rect.centerx
        dy = self.last_player_pos[1] - self.rect.centery
        dist = math.sqrt(dx ** 2 + dy ** 2)
        if dist != 0:
            dx /= dist
            dy /= dist
        self.rect.move_ip(dx * self.speed * self.game.dt, dy * self.speed * self.game.dt)

        if not self.screen.get_rect().colliderect(self.rect):
            self.kill()