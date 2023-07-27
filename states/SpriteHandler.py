import pygame
from sprites.Asteroid import Asteroid
from sprites.Enemy import Enemy
import random

class SpriteHandler():
    def __init__(self, screen, game_state_handler) -> None:
        self.screen = screen

        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.next_enemy_spawn_time = pygame.time.get_ticks() + 5000
        self.next_asteroid_spawn_time = pygame.time.get_ticks() + 5000
        self.game_state_handler = game_state_handler

    def draw(self):
        self.all_sprites.draw(self.screen)

    def update(self):
        self.all_sprites.update()
        self.check_collisions()

    def check_collisions(self):
        # Check for collisions
        asteroid_collisions = pygame.sprite.groupcollide(
            self.bullets, self.asteroids, True, True)

        self.game_state_handler.update_score(len(asteroid_collisions))

        enemy_collisions = pygame.sprite.groupcollide(
            self.bullets, self.enemies, True, True)

        self.game_state_handler.update_score(len(enemy_collisions) * 2)

    def add_bullet(self, bullet):
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)

    def add_enemy(self):
        enemy = Enemy()
        self.all_sprites.add(enemy)
        self.enemies.add(enemy)

    def add_asteroid(self):
        asteroid = Asteroid()
        self.all_sprites.add(asteroid)
        self.asteroids.add(asteroid)

    def spawn_enemies(self):
        for _ in range(random.randint(1, 3)):
            self.add_enemy()
        
        self.next_enemy_spawn_time += 5000

    def spawn_asteroids(self):
        for _ in range(random.randint(1, 3)):
            self.add_asteroid()

        self.next_asteroid_spawn_time += 5000