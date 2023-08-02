from constants import *
from utils import draw_text, initialise_game
from states.SpawnHandler import SpawnHandler


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship Shoot 'em Up")

clock = pygame.time.Clock()

# Set up font
font_size = 36
font = pygame.font.Font(None, font_size)

def main():
    clock, gameStateHandler, spriteHandler, spawnHandler = initialise_game(screen)

    while gameStateHandler.running:
        clock.tick(60)  # Limit FPS to 60

        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameStateHandler.running = False

        # Update game objects
        spawnHandler.update()
        spriteHandler.update()
        gameStateHandler.update()

        # Draw game objects
        screen.fill((0, 0, 0))
        screen.blit(space_background, (0, gameStateHandler.background_pos))

        # Draw the text surface on the screen
        draw_text(f"Score: {gameStateHandler.score}", font, WHITE, screen, 10, 10)
        draw_text(f"Ammunition: {gameStateHandler.ammunition}", font, WHITE, screen, 10, 50)
        draw_text(f"Lives: {gameStateHandler.lives}", font, WHITE, screen, 10, 90)

        spriteHandler.draw()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
