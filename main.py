from constants import *
from utils import draw_text, initialise_game
from states.SpawnHandler import SpawnHandler


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
heart_img = pygame.transform.scale(pygame.image.load('assets/heart.png'), (48, 48))
space_background = pygame.image.load("assets/space_background_chimera.png")
pygame.display.set_caption("Spaceship Shoot 'em Up")

clock = pygame.time.Clock()

# Set up font
font_size = 36
font = pygame.font.Font(None, font_size)

def main():
    clock, gameStateHandler, spriteHandler, spawnHandler, collisionHandler = initialise_game(screen)

    while gameStateHandler.running:
        clock.tick(60)  # Limit FPS to 60

        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameStateHandler.running = False

        # Update game objects
        collisionHandler.check_collisions()
        spawnHandler.update()
        spriteHandler.update()
        gameStateHandler.update()

        # Draw game objects
        screen.fill((0, 0, 0))
        background_y = gameStateHandler.background_pos % space_background.get_rect().height
        screen.blit(space_background, (0 - gameStateHandler.camera_offset[0], background_y - space_background.get_rect().height - gameStateHandler.camera_offset[1]))
        screen.blit(space_background, (0 - gameStateHandler.camera_offset[0], background_y - gameStateHandler.camera_offset[1]))

        # Draw the text surface on the screen
        draw_text(f"Score: {gameStateHandler.score}", font, WHITE, screen, 10, 10)
        draw_text(f"Ammunition: {gameStateHandler.ammunition}", font, WHITE, screen, 10, 50)
        for i in range(gameStateHandler.lives):
            screen.blit(heart_img, (10 + 48 * i, 90))

        spriteHandler.draw()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
