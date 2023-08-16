import pygame
from sprites.Spaceship import Spaceship
from sprites.Asteroid import Asteroid
from sprites.Explosion import Explosion
from sprites.Enemy import Enemy
from states.GameStateHandler import GameStateHandler

class SpriteHandler():
    def __init__(self, screen: pygame.Surface, gameStateHandler: GameStateHandler) -> None:
        self.screen = screen

        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
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
        asteroid_collisions = pygame.sprite.groupcollide(
            self.bullets, self.asteroids, True, True)

        for asteroid in asteroid_collisions:
            self.add_explosion(center=asteroid.rect.center, type='asteroid')
            self.gameStateHandler.score += 2

        enemy_collisions = pygame.sprite.groupcollide(
            self.bullets, self.enemies, True, True)
        
        for enemy in enemy_collisions:
            self.add_explosion(center=enemy.rect.center, type='enemy')
            self.gameStateHandler.score += 2

        enemy_bullet_collisions = pygame.sprite.spritecollide(
            self.spaceship, self.enemy_bullets, True
        )
        
        for bullet in enemy_bullet_collisions: 
            self.gameStateHandler.lives -= 1

        collision_with_enemy = pygame.sprite.spritecollide(
            self.spaceship, self.enemies, True)

        collision_with_asteroid = pygame.sprite.spritecollide(
            self.spaceship, self.asteroids, True)

        if collision_with_enemy or collision_with_asteroid:
            self.gameStateHandler.lives -= 1

    def add_bullet(self, bullet):
        if (bullet.type == 'player'):
            self.bullets.add(bullet)
        else:
            self.enemy_bullets.add(bullet)
        self.all_sprites.add(bullet)

    def add_enemy(self, x: int):
        enemy = Enemy(x, spriteHandler=self)
        self.all_sprites.add(enemy)
        self.enemies.add(enemy)

    def add_asteroid(self, x: int):
        asteroid = Asteroid(x)
        self.all_sprites.add(asteroid)
        self.asteroids.add(asteroid)
    
    def add_explosion(self, center, type: str):
        explosion = Explosion(center=center, type=type)
        self.all_sprites.add(explosion)
