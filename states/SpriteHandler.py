import pygame
import random
from sprites.Spaceship import Spaceship
from sprites.Asteroid import Asteroid
from sprites.Explosion import Explosion
from sprites.Enemy import Enemy
from sprites.AltEnemy import AltEnemy
from sprites.AsymEnemy import AsymEnemy
from sprites.PowerUp import PowerUp

class SpriteHandler():
    def __init__(self, game) -> None:
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.power_ups = pygame.sprite.Group()
        self.game = game

        self.spaceship: Spaceship = Spaceship(game)
        self.all_sprites.add_internal(self.spaceship)

    def draw(self):
        self.all_sprites.draw(self.game.screen)

    def update(self):
        self.all_sprites.update()

    def add_bullet(self, bullet):
        if (bullet.type == 'player'):
            self.bullets.add(bullet)
        else:
            self.enemy_bullets.add(bullet)
        self.all_sprites.add(bullet)

    def add_enemy(self, x: int):
        enemy = random.choice([AltEnemy, AsymEnemy, Enemy])(x, spriteHandler=self)
        self.all_sprites.add(enemy)
        self.enemies.add(enemy)

    def add_asteroid(self, x: int):
        asteroid = Asteroid(x)
        self.all_sprites.add(asteroid)
        self.asteroids.add(asteroid)
    
    def add_explosion(self, center, type: str):
        explosion = Explosion(center=center, type=type)
        self.all_sprites.add(explosion)

    def add_power_up(self):
        power_up = PowerUp()
        self.power_ups.add(power_up)
        self.all_sprites.add(power_up)