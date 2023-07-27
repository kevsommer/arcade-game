import pygame
from states.GameStateHandler import GameStateHandler
from states.SpriteHandler import SpriteHandler
from sprites.Spaceship import Spaceship
from sprites.Asteroid import Asteroid
from sprites.Enemy import Enemy

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def initialise_sprites(sprite_handler):
    for _ in range(4):
        asteroid = Asteroid()
        sprite_handler.all_sprites.add(asteroid)
        sprite_handler.asteroids.add(asteroid)

    for _ in range(4):
        enemy = Enemy()
        sprite_handler.all_sprites.add(enemy)
        sprite_handler.enemies.add(enemy)

def initialise_game(screen: pygame.Surface):
    clock = pygame.time.Clock()

    # game logic handler
    game_state_handler = GameStateHandler()

    # sprites
    sprite_handler = SpriteHandler(screen, game_state_handler)
    spaceship = Spaceship(screen, sprite_handler, game_state_handler=game_state_handler)
    sprite_handler.all_sprites.add(spaceship)

    initialise_sprites(sprite_handler)

    return  clock, game_state_handler, sprite_handler, spaceship