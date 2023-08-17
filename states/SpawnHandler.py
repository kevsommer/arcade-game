from states.SpriteHandler import SpriteHandler
import random
import pygame

class SpawnHandler():
    def __init__(self, spriteHandler: SpriteHandler) -> None:
        self.spriteHandler = spriteHandler
        self.next_enemy_spawn_time = pygame.time.get_ticks() + 5000
        self.next_asteroid_spawn_time = pygame.time.get_ticks() + 5000
        self.next_bubble_spawn_time = pygame.time.get_ticks() + random.randint(5000, 10000)

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

    def spawn_item_bubble(self) -> None:
        self.spriteHandler.add_item_bubble()

        self.next_bubble_spawn_time += random.randint(5000, 10000)
    
    def update(self) -> None: 
        current_time = pygame.time.get_ticks()
        if current_time > self.next_enemy_spawn_time:
            self.spawn_enemies()

        if current_time > self.next_asteroid_spawn_time:
            self.spawn_asteroids()

        if current_time > self.next_bubble_spawn_time:
            self.spawn_power_up()
