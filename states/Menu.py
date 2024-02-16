
import pygame 
from constants import HEIGHT, WIDTH

START = 0
HIGHSCORES = 1
QUIT = 2

def draw_menu_box(text, font, color, bgcolor, surface, x, y, width, height):
    pygame.draw.rect(surface, bgcolor, (x, y, width, height))
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x + width / 2, y + height / 2)
    
    surface.blit(textobj, textrect)

class Menu:
    def __init__(self, game) -> None:
        self.selected_menu_item = START
        self.menu_items = ["Start", "Highscores", "Quit"]
        self.font = pygame.font.Font(None, 36)
        self.game = game

    def action(self):
        if self.selected_menu_item == START:
            self.game.inMenu = False
        elif self.selected_menu_item == HIGHSCORES:
            pass
        elif self.selected_menu_item == QUIT:
            pygame.quit()

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            pygame.time.delay(150)
            self.selected_menu_item = (self.selected_menu_item + 1) % len(self.menu_items)
        if keys[pygame.K_UP]:
            pygame.time.delay(150)
            self.selected_menu_item = (self.selected_menu_item - 1) % len(self.menu_items)
        if keys[pygame.K_RETURN]:
            self.action()
    
    def draw(self, screen):
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 64))

        screen.blit(overlay, (0, 0))
        for i, item in enumerate(self.menu_items):
            color = (255, 255, 255) if i == self.selected_menu_item else (100, 100, 100)
            draw_menu_box(item, self.font, color, (0, 0, 0), screen, WIDTH / 2 - 100, HEIGHT / 2 - 150 + 100 * i, 200, 50)