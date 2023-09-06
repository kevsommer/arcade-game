import math
import pygame

class TracingBullet(pygame.sprite.Sprite):
    def __init__(self, game, x: int, y: int, speed: int, delay: int):
        super().__init__()

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
        self.direction = pygame.math.Vector2(0, 1).normalize()
        self.target_direction = None
        self.update_direction_delay = 1000  # milliseconds
        self.update_direction_time = 0

    def update(self):
        self.lifetime += self.game.dt
        if self.lifetime >= 5000:
            self.kill()

        self.last_player_pos = self.game.spriteHandler.spaceship.rect.center

        self.update_direction_time += self.game.dt
        if self.update_direction_time >= self.update_direction_delay:
            self.target_direction = pygame.math.Vector2(self.last_player_pos) - pygame.math.Vector2(self.rect.center)
            self.target_direction.normalize_ip()
            self.update_direction_time = 0

        if self.target_direction is not None:
            self.direction = self.direction.lerp(self.target_direction, 0.05)

        self.rect.move_ip(self.direction * self.speed * self.game.dt)

        if not self.game.screen.get_rect().colliderect(self.rect):
            self.kill()