from constants import *
from sprites.Spaceship import Spaceship
from sprites.Enemy import Enemy
from sprites.Asteroid import Asteroid


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship Shoot 'em Up")


# Set minimum time between bullet spawns (in milliseconds)
clock = pygame.time.Clock()

# Load images
space_background = pygame.image.load(
    os.path.join("assets", "space_background.jpeg"))


class SpriteHandler():
    def __init__(self, screen) -> None:
        self.screen = screen

        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.spaceship = Spaceship(screen, self)

    def draw(self):
        self.all_sprites.draw(self.screen)

    def update(self):
        self.all_sprites.update()
        self.check_collisions()

    def check_collisions(self):
        # Check for collisions
        pygame.sprite.groupcollide(
            self.bullets, self.asteroids, True, True)

        pygame.sprite.groupcollide(
            self.bullets, self.enemies, True, True)

    def add_bullet(self, bullet):
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)

    def add_enemy(self, enemy):
        self.all_sprites.add(enemy)
        self.enemies.add(enemy)

    def add_asteroid(self, asteroid):
        self.all_sprites.add(asteroid)
        self.asteroids.add(asteroid)


def main():
    clock = pygame.time.Clock()
    running = True

    sprite_handler = SpriteHandler(screen)
    spaceship = Spaceship(screen, sprite_handler)
    sprite_handler.all_sprites.add(spaceship)

    while running:
        clock.tick(60)  # Limit FPS to 60

        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game objects
        sprite_handler.update()
        spaceship.update()

        current_time = pygame.time.get_ticks()
        if current_time % 1000 == 0:
            enemy = Enemy()
            sprite_handler.all_sprites.add(enemy)
            sprite_handler.enemies.add(enemy)

        collided_with_enemy = pygame.sprite.spritecollide(
            spaceship, sprite_handler.enemies, False)

        collided_with_asteroid = pygame.sprite.spritecollide(
            spaceship, sprite_handler.asteroids, False)

        if collided_with_enemy or collided_with_asteroid:
            running = False

        # Draw game objects
        screen.fill((0, 0, 0))
        screen.blit(space_background, (0, 0))

        sprite_handler.draw()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
