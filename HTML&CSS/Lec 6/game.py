import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size
player_speed = 5

# Enemy
enemy_size = 50
enemy_speed = 3

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, player_size, player_size])

def draw_enemy(x, y):
    pygame.draw.rect(screen, RED, [x, y, enemy_size, enemy_size])

def game_loop():
    enemy_x = random.randint(0, WIDTH - enemy_size)
    enemy_y = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += player_speed

        # Move enemy
        enemy_y += enemy_speed
        if enemy_y > HEIGHT:
            enemy_x = random.randint(0, WIDTH - enemy_size)
            enemy_y = 0

        # Collision detection
        if (
            player_x < enemy_x + enemy_size
            and player_x + player_size > enemy_x
            and player_y < enemy_y + enemy_size
            and player_y + player_size > enemy_y
        ):
            print("Game Over!")
            pygame.quit()
            sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Draw player and enemy
        draw_player(player_x, player_y)
        draw_enemy(enemy_x, enemy_y)

        # Update the display
        pygame.display.flip()

        # Set the frame rate
        clock.tick(FPS)

# Run the game loop
game_loop()
