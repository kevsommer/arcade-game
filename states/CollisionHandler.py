import pygame 
from states.SpriteHandler import SpriteHandler
from states.GameStateHandler import GameStateHandler

class CollisionHandler():
    def __init__(self, spriteHandler: SpriteHandler, gameStateHandler: GameStateHandler) -> None:
        self.spriteHandler = spriteHandler
        self.gameStateHandler = gameStateHandler

    def check_collisions(self):
        self.check_player_bullet_collisions()
        self.check_enemy_bullet_collisions()
        self.check_player_collisions()

    def check_asteroid_p_bullet_collisions(self):
        asteroid_collisions = pygame.sprite.groupcollide(
        self.spriteHandler.bullets, self.spriteHandler.asteroids, True, True)

        for asteroid in asteroid_collisions:
            self.spriteHandler.add_explosion(center=asteroid.rect.center, type='asteroid')
            self.gameStateHandler.score += 2

    def check_enemy_p_bullet_collisions(self):
        enemy_collisions = pygame.sprite.groupcollide(
        self.spriteHandler.bullets, self.spriteHandler.enemies, True, True)

        for enemy in enemy_collisions:
            self.spriteHandler.add_explosion(center=enemy.rect.center, type='enemy')
            self.gameStateHandler.score += 2

    def check_player_bullet_collisions(self):
        self.check_asteroid_p_bullet_collisions()
        self.check_enemy_p_bullet_collisions()
    
    def check_enemy_bullet_collisions(self):
        enemy_bullet_collisions = pygame.sprite.spritecollide(self.spriteHandler.spaceship, self.spriteHandler.enemy_bullets, True)
        for collision in enemy_bullet_collisions:
            self.gameStateHandler.lives -= 1
            self.spriteHandler.spaceship.reset()
    
    def check_player_collisions(self):
        collision_with_enemy = pygame.sprite.spritecollide(
            self.spriteHandler.spaceship, self.spriteHandler.enemies, True)

        collision_with_asteroid = pygame.sprite.spritecollide(
            self.spriteHandler.spaceship, self.spriteHandler.asteroids, True)

        if collision_with_enemy or collision_with_asteroid:
            self.gameStateHandler.lives -= 1
            self.spriteHandler.spaceship.reset()