from states.SpriteHandler import SpriteHandler
import random
import pygame

class SpawnHandler():
    def __init__(self, spriteHandler: SpriteHandler) -> None:
        self.spriteHandler = spriteHandler
        self.next_enemy_spawn_time = pygame.time.get_ticks() + 5000
        self.next_asteroid_spawn_time = pygame.time.get_ticks() + 5000
        

    def spawn_enemies(self) -> None:
        n_enemies = random.randint(1, 3)
        positions = random.sample(range(8), n_enemies)
        for pos in positions:
            self.spriteHandler.add_enemy(pos * 100)

        self.next_enemy_spawn_time += 5000

    def spawn_asteroids(self) -> None:
        n_asteroids = random.randint(1, 3)
        positions = random.sample(range(8), n_asteroids)
        for pos in positions:
            self.spriteHandler.add_asteroid(pos * 100)

        self.next_asteroid_spawn_time += 5000
    
