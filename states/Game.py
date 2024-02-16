from states.GameStateHandler import GameStateHandler
from states.SpawnHandler import SpawnHandler
from states.CollisionHandler import CollisionHandler
from states.SpriteHandler import SpriteHandler
from states.Menu import Menu
import pygame
from constants import WHITE, HEIGHT, WIDTH, FONT_SIZE

ammunition_img = pygame.transform.scale(pygame.image.load('assets/bubbles/ammunition.png'), (48, 48))
coin_img = pygame.transform.scale(pygame.image.load('assets/bubbles/coin.png'), (30, 30))
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
        self.inMenu = True
        pygame.display.set_caption("Spaceship Shoot 'em Up")

        self.clock = pygame.time.Clock()
        self.dt = 0

        self.gameStateHandler = GameStateHandler()
        self.spriteHandler = SpriteHandler(self)
        self.spawnHandler = SpawnHandler(self)
        self.collisionHandler = CollisionHandler(self)
        self.menu  = Menu(self)

        # Set up font
        self.font = pygame.font.Font(None, FONT_SIZE)

        initialise_sprites(spawnHandler=self.spawnHandler)

    def run(self):
        while self.gameStateHandler.running:
            # Handle input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameStateHandler.running = False

            # Update game
            if not self.inMenu:
                self.update()
            else:
                self.menu.update()
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

    def draw_background(self):
        self.screen.fill((0, 0, 0))
        background_y = self.gameStateHandler.background_pos % space_background.get_rect().height
        self.screen.blit(space_background, (0 - self.gameStateHandler.camera_offset[0], background_y - space_background.get_rect().height - self.gameStateHandler.camera_offset[1]))
        self.screen.blit(space_background, (0 - self.gameStateHandler.camera_offset[0], background_y - self.gameStateHandler.camera_offset[1]))

    def draw_gui(self):
        self.screen.blit(coin_img, (18, 10))
        draw_text(str(self.gameStateHandler.score), self.font, WHITE, self.screen, 60, 16)
        self.screen.blit(ammunition_img, (10, 50))
        draw_text(str(self.gameStateHandler.ammunition), self.font, WHITE, self.screen, 60, 65)
        for i in range(self.gameStateHandler.lives):
            self.screen.blit(heart_img, (10 + 48 * i, 110))

    def toggle_menu(self):
        keys = pygame.key.get_pressed()
        if self.inMenu:
            self.menu.draw(self.screen)
            if keys[pygame.K_SPACE]:
                self.inMenu = False
        else: 
            if keys[pygame.K_ESCAPE]:
                self.inMenu = True

    def draw(self):
        self.draw_background()
        self.draw_gui()
        self.spriteHandler.draw()
        self.toggle_menu()

        pygame.display.flip()
