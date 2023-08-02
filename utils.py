import pygame
from states.GameStateHandler import GameStateHandler
from states.SpriteHandler import SpriteHandler
from states.SpawnHandler import SpawnHandler
from sprites.Spaceship import Spaceship

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def initialise_sprites(spawnHandler: SpawnHandler):
    spawnHandler.spawn_asteroids()
    spawnHandler.spawn_enemies()
    
def initialise_game(screen: pygame.Surface):
    clock = pygame.time.Clock()

    # game logic handler
    gameStateHandler = GameStateHandler()

    # sprites
    spriteHandler = SpriteHandler(screen, gameStateHandler)
    spawnHandler = SpawnHandler(spriteHandler)

    initialise_sprites(spawnHandler=spawnHandler)

    return  clock, gameStateHandler, spriteHandler, spawnHandler