import pygame 

class CollisionHandler():
    def __init__(self, game) -> None:
        self.game = game
        
    def check_collisions(self):
        self.check_player_bullet_collisions()
        self.check_enemy_bullet_collisions()
        self.check_player_collisions()

    def check_asteroid_p_bullet_collisions(self):
        asteroid_collisions = pygame.sprite.groupcollide(
        self.game.spriteHandler.bullets, self.game.spriteHandler.asteroids, True, True, collided=pygame.sprite.collide_mask)

        for asteroid in asteroid_collisions:
            self.game.spriteHandler.add_explosion(center=asteroid.rect.center, type='asteroid')
            self.game.gameStateHandler.score += 2

    def check_enemy_p_bullet_collisions(self):
        enemy_collisions = pygame.sprite.groupcollide(
        self.game.spriteHandler.bullets, self.game.spriteHandler.enemies, True, True, collided=pygame.sprite.collide_mask)

        for enemy in enemy_collisions:
            self.game.spriteHandler.add_explosion(center=enemy.rect.center, type='enemy')
            self.game.gameStateHandler.score += 2

    def check_player_bullet_collisions(self):
        self.check_asteroid_p_bullet_collisions()
        self.check_enemy_p_bullet_collisions()
    
    def check_enemy_bullet_collisions(self):
        enemy_bullet_collisions = pygame.sprite.spritecollide(self.game.spriteHandler.spaceship, self.game.spriteHandler.enemy_bullets, True, collided=pygame.sprite.collide_mask)
        for collision in enemy_bullet_collisions:
            self.game.gameStateHandler.lives -= 1
            self.game.spriteHandler.spaceship.reset()
    
    def check_player_collisions(self):
        collision_with_enemy = pygame.sprite.spritecollide(
            self.game.spriteHandler.spaceship, self.game.spriteHandler.enemies, True, collided=pygame.sprite.collide_mask)

        collision_with_asteroid = pygame.sprite.spritecollide(
            self.game.spriteHandler.spaceship, self.game.spriteHandler.asteroids, True, collided=pygame.sprite.collide_mask)

        if collision_with_enemy or collision_with_asteroid:
            self.game.gameStateHandler.lives -= 1
            self.game.spriteHandler.spaceship.reset()