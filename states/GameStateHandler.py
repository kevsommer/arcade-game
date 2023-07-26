import pygame
import random

class GameStateHandler():
    def __init__(self) -> None:
        self.score = 0
        self.lives = 3
        self.background_pos = -2200
        self.sprite_handler = None
        self.next_enemy_spawn_time = pygame.time.get_ticks() + 5000
        self.next_asteroid_spawn_time = pygame.time.get_ticks() + 5000
        self.ammunition = 100

    def set_sprite_handler(self, sprite_handler):
        self.sprite_handler = sprite_handler

    def update_score(self, amount: int):
        self.score += amount

    def update_lives(self, amount: int):
        self.lives += amount

    def update_background_position(self):
        self.background_pos += 0.5

    def spawn_enemies(self):
        for _ in range(random.randint(1, 3)):
            self.sprite_handler.add_enemy()
        
        self.next_enemy_spawn_time += 5000

    def spawn_asteroids(self):
        for _ in range(random.randint(1, 3)):
            self.sprite_handler.add_asteroid()

        self.next_asteroid_spawn_time += 5000