import pygame
from sprites.Spaceship import Spaceship
from sprites.Asteroid import Asteroid
from sprites.Enemy import Enemy
from states.GameStateHandler import GameStateHandler

class SpriteHandler():
    def __init__(self, screen: pygame.Surface, gameStateHandler: GameStateHandler) -> None:
        self.screen = screen

        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()

        self.spaceship: Spaceship = Spaceship(screen, spriteHandler=self, gameStateHandler=gameStateHandler)
        self.all_sprites.add_internal(self.spaceship)
        self.gameStateHandler = gameStateHandler

    def draw(self):
        self.all_sprites.draw(self.screen)

    def update(self):
        self.all_sprites.update()
        self.check_collisions()

    def check_collisions(self):
        # Check for collisions
        asteroid_collisions = pygame.sprite.groupcollide(
            self.bullets, self.asteroids, True, True)

        self.gameStateHandler.score += len(asteroid_collisions)

        enemy_collisions = pygame.sprite.groupcollide(
            self.bullets, self.enemies, True, True)

        self.gameStateHandler.score += len(enemy_collisions) * 2

        collision_with_enemy = pygame.sprite.spritecollide(
            self.spaceship, self.enemies, True)

        collision_with_asteroid = pygame.sprite.spritecollide(
            self.spaceship, self.asteroids, True)

        if collision_with_enemy or collision_with_asteroid:
            self.gameStateHandler.lives -= 1

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
