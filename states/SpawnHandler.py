import random
import pygame

class SpawnHandler():
    def __init__(self, game) -> None:
        self.game = game
        self.next_enemy_spawn_time = pygame.time.get_ticks() + 5000
        self.next_asteroid_spawn_time = pygame.time.get_ticks() + 5000
        self.next_power_up_spawn_time = pygame.time.get_ticks() + random.randint(5000, 10000)

    def spawn_enemies(self) -> None:
        n_enemies = random.randint(1, 3)
        positions = random.sample(range(8), n_enemies)
        for pos in positions:
            self.game.spriteHandler.add_enemy(pos * 100)

        self.next_enemy_spawn_time += 5000

    def spawn_asteroids(self) -> None:
        n_asteroids = random.randint(1, 3)
        positions = random.sample(range(8), n_asteroids)
        for pos in positions:
            self.game.spriteHandler.add_asteroid(pos * 100)

        self.next_asteroid_spawn_time += 5000

    def spawn_power_up(self) -> None:
        self.game.spriteHandler.add_power_up()
        self.next_power_up_spawn_time += random.randint(5000, 10000)
    
    def update(self) -> None: 
        current_time = pygame.time.get_ticks()
        if current_time > self.next_enemy_spawn_time:
            self.spawn_enemies()

        if current_time > self.next_asteroid_spawn_time:
            self.spawn_asteroids()

        if current_time > self.next_power_up_spawn_time:
            self.spawn_power_up()
