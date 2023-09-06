import pygame
from states.Game import Game
from sprites.Spaceship import Spaceship

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    
def initialise_game():
    game = Game()

    return game.gameStateHandler, game