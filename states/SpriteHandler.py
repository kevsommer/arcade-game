import pygame
from sprites.Asteroid import Asteroid
from sprites.Enemy import Enemy
from states.GameStateHandler import GameStateHandler

class SpriteHandler():
    def __init__(self, screen: pygame.Surface, game_state_handler: GameStateHandler) -> None:
        self.screen = screen

        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
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

    def add_enemy(self, x: int):
        enemy = Enemy(x)
        self.all_sprites.add(enemy)
        self.enemies.add(enemy)

    def add_asteroid(self, x: int):
        asteroid = Asteroid(x)
        self.all_sprites.add(asteroid)
        self.asteroids.add(asteroid)
