from states.GameStateHandler import GameStateHandler
from states.SpawnHandler import SpawnHandler
from states.CollisionHandler import CollisionHandler
from states.SpriteHandler import SpriteHandler
import pygame

def initialise_sprites(spawnHandler: SpawnHandler):
    spawnHandler.spawn_asteroids()
    spawnHandler.spawn_enemies()

class Game():
    def __init__(self, screen) -> None:
        self.clock = pygame.time.Clock()

        # game logic handler
        self.gameStateHandler = GameStateHandler()

        # sprites
        self.spriteHandler = SpriteHandler(screen, self)
        self.spawnHandler = SpawnHandler(game=self)
        self.collisionHandler = CollisionHandler(self)

        initialise_sprites(spawnHandler=self.spawnHandler)
