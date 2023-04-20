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
    os.path.join("assets", "space_background.jpeg"))

asteroid_img = pygame.image.load(
    os.path.join("assets", "asteroid.png"))

bullet_img = pygame.image.load(
    os.path.join("assets", "bullet.png"))

enemy_img = pygame.image.load(
    os.path.join("assets", "enemy.png"))

spaceship_img = pygame.image.load(
    os.path.join("assets", "spaceship.png"))
