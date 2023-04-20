from constants import *
# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship Shoot 'em Up")


# Set minimum time between bullet spawns (in milliseconds)
clock = pygame.time.Clock()

# Load images
space_background = pygame.image.load(
    os.path.join("assets", "space_background.jpeg"))


def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)  # Limit FPS to 60

        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw game objects
        screen.fill((0, 0, 0))
        screen.blit(space_background, (0, 0))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
