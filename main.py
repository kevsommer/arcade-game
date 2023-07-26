from constants import *
from utils import draw_text, initialise_game


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship Shoot 'em Up")

clock = pygame.time.Clock()

# Set up font
font_size = 36
font = pygame.font.Font(None, font_size)

def main():
    running = True
    clock, game_state_handler, sprite_handler, spaceship = initialise_game(screen)

    while running:
        clock.tick(60)  # Limit FPS to 60

        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game objects
        sprite_handler.update()
        spaceship.update()

        game_state_handler.update_background_position()

        current_time = pygame.time.get_ticks()
        if current_time > game_state_handler.next_enemy_spawn_time:
            game_state_handler.spawn_enemies()

        if current_time > game_state_handler.next_asteroid_spawn_time:
            game_state_handler.spawn_asteroids()

        collided_with_enemy = pygame.sprite.spritecollide(
            spaceship, sprite_handler.enemies, False)

        collided_with_asteroid = pygame.sprite.spritecollide(
            spaceship, sprite_handler.asteroids, False)

        if collided_with_enemy or collided_with_asteroid:
            running = False

        # Draw game objects
        screen.fill((0, 0, 0))
        screen.blit(space_background, (0, game_state_handler.background_pos))

        # Draw the text surface on the screen
        text = f"Score: {game_state_handler.score}"
        draw_text(text, font, WHITE, screen, 10, 10)
        
        # Draw the ammunition on the screen
        text = f"Ammunition: {game_state_handler.ammunition}"
        draw_text(text, font, WHITE, screen, 10, 50)


        sprite_handler.draw()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
