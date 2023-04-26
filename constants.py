import pygame
import random
import os

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60
SPACESHIP_SPEED = 2
BULLET_SPEED = 10
ENEMY_SPEED = 2
ASTEROID_SPEED = 4
MIN_BULLET_INTERVAL = 200

# Colors
WHITE = (255, 255, 255)

# Load Images
space_background = pygame.image.load(
    os.path.join("assets", "space_background_SLSOS.png"))

asteroid_img = pygame.transform.scale_by(pygame.image.load(
    os.path.join("assets", "asteroid.png")), 0.5)

bullet_img = pygame.transform.scale_by(pygame.image.load(
    os.path.join("assets", "bullet.png")), 0.125)

enemy_img = pygame.transform.scale_by(pygame.image.load(
    os.path.join("assets", "enemy.png")), 0.5)

spaceship_img = pygame.transform.scale_by(pygame.image.load(
    os.path.join("assets", "spaceship.png")), 0.5)
