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

# Set up the font
font_size = 36
font = pygame.font.Font(None, font_size)

# Set up the text and color
text_color = (255, 255, 255)  # White color
bg_color = (0, 0, 0)  # Black background color


class SpriteHandler():
    def __init__(self, screen, game_state_handler) -> None:
        self.screen = screen

        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.game_state_handler = game_state_handler

    def draw(self):
        self.all_sprites.draw(self.screen)

    def update(self):
        self.all_sprites.update()
        self.check_collisions()

    def check_collisions(self):
        # Check for collisions
        asteroid_collisions = pygame.sprite.groupcollide(
            self.bullets, self.asteroids, True, True)

        self.game_state_handler.update_score(len(asteroid_collisions))

        enemy_collisions = pygame.sprite.groupcollide(
            self.bullets, self.enemies, True, True)

        self.game_state_handler.update_score(len(enemy_collisions) * 2)

    def add_bullet(self, bullet):
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)

    def add_enemy(self, enemy):
        self.all_sprites.add(enemy)
        self.enemies.add(enemy)

    def add_asteroid(self, asteroid):
        self.all_sprites.add(asteroid)
        self.asteroids.add(asteroid)


class GameStateHandler():
    def __init__(self) -> None:
        self.score = 0
        self.lives = 3
        self.background_pos = -2200
        self.sprite_handler = None
        self.next_enemy_spawn_time = pygame.time.get_ticks() + 5000
        self.next_asteroid_spawn_time = pygame.time.get_ticks() + 5000
        self.ammunition = 100

    def set_sprite_handler(self, sprite_handler):
        self.sprite_handler = sprite_handler

    def update_score(self, amount: int):
        self.score += amount

    def update_lives(self, amount: int):
        self.lives += amount

    def update_background_position(self):
        self.background_pos += 0.5

    def spawn_enemies(self):
        for _ in range(random.randint(1, 3)):
            enemy = Enemy()
            self.sprite_handler.add_enemy(enemy)
        
        self.next_enemy_spawn_time += 5000

    def spawn_asteroids(self):
        for _ in range(random.randint(1, 3)):
            asteroid = Asteroid()
            self.sprite_handler.add_asteroid(asteroid)

        self.next_asteroid_spawn_time += 5000

def initialise_sprites(sprite_handler):
    for _ in range(4):
        asteroid = Asteroid()
        sprite_handler.all_sprites.add(asteroid)
        sprite_handler.asteroids.add(asteroid)

    for _ in range(4):
        enemy = Enemy()
        sprite_handler.all_sprites.add(enemy)
        sprite_handler.enemies.add(enemy)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main():
    clock = pygame.time.Clock()
    running = True

    # game logic handler
    game_state_handler = GameStateHandler()

    # sprites
    sprite_handler = SpriteHandler(screen, game_state_handler)
    game_state_handler.set_sprite_handler(sprite_handler)
    spaceship = Spaceship(screen, sprite_handler, game_state_handler=game_state_handler)
    sprite_handler.all_sprites.add(spaceship)

    initialise_sprites(sprite_handler)

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
        draw_text(text, font, text_color, screen, 10, 10)
        
        # Draw the ammunition on the screen
        text = f"Ammunition: {game_state_handler.ammunition}"
        draw_text(text, font, text_color, screen, 10, 50)


        sprite_handler.draw()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
