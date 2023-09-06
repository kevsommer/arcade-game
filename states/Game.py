from states.GameStateHandler import GameStateHandler
from states.SpawnHandler import SpawnHandler
from states.CollisionHandler import CollisionHandler
from states.SpriteHandler import SpriteHandler
import pygame
from constants import WHITE, HEIGHT, WIDTH

heart_img = pygame.transform.scale(pygame.image.load('assets/heart.png'), (48, 48))
space_background = pygame.image.load("assets/space_background_chimera.png")


def initialise_sprites(spawnHandler: SpawnHandler):
    spawnHandler.spawn_asteroids()
    spawnHandler.spawn_enemies()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

class Game():
    def __init__(self) -> None:
        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Spaceship Shoot 'em Up")

        self.clock = pygame.time.Clock()
        self.dt = 0
        # game logic handler
        self.gameStateHandler = GameStateHandler()

        # sprites
        self.spriteHandler = SpriteHandler(self)
        self.spawnHandler = SpawnHandler(self)
        self.collisionHandler = CollisionHandler(self)

        # Set up font
        font_size = 36
        self.font = pygame.font.Font(None, font_size)


        initialise_sprites(spawnHandler=self.spawnHandler)

    def run(self):
        while self.gameStateHandler.running:
            # Handle input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameStateHandler.running = False

            # Update game
            self.update()

            # Draw screen
            self.draw()

        pygame.quit()

    def update(self):
        self.clock.tick(60) # 60 FPS
        self.dt = self.clock.get_time()
        self.gameStateHandler.update()
        self.spriteHandler.update()
        self.spawnHandler.update()
        self.collisionHandler.check_collisions()

    def draw(self):
        self.screen.fill((0, 0, 0))
        background_y = self.gameStateHandler.background_pos % space_background.get_rect().height
        self.screen.blit(space_background, (0 - self.gameStateHandler.camera_offset[0], background_y - space_background.get_rect().height - self.gameStateHandler.camera_offset[1]))
        self.screen.blit(space_background, (0 - self.gameStateHandler.camera_offset[0], background_y - self.gameStateHandler.camera_offset[1]))

        # Draw the text surface on the screen
        draw_text(f"Score: {self.gameStateHandler.score}", self.font, WHITE, self.screen, 10, 10)
        draw_text(f"Ammunition: {self.gameStateHandler.ammunition}", self.font, WHITE, self.screen, 10, 50)
        for i in range(self.gameStateHandler.lives):
            self.screen.blit(heart_img, (10 + 48 * i, 90))

        self.spriteHandler.draw()

        pygame.display.flip()
