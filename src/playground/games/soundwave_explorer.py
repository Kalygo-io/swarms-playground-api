import pygame
import numpy as np
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
SOUND_WAVE_RADIUS = 100
BACKGROUND_COLOR = (0, 0, 0)
HIDDEN_COLOR = (255, 255, 255)
REVEALED_COLOR = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SoundWave Explorer")

# Game variables
player_pos = [WIDTH // 2, HEIGHT // 2]
hidden_objects = []
revealed_objects = []

# Generate hidden objects
for _ in range(10):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    hidden_objects.append((x, y))

def draw_hidden_objects():
    for obj in hidden_objects:
        pygame.draw.circle(screen, HIDDEN_COLOR, obj, 5)

def reveal_objects():
    global revealed_objects
    for obj in hidden_objects:
        if np.linalg.norm(np.array(player_pos) - np.array(obj)) < SOUND_WAVE_RADIUS:
            revealed_objects.append(obj)
    hidden_objects[:] = [obj for obj in hidden_objects if obj not in revealed_objects]

def draw_revealed_objects():
    for obj in revealed_objects:
        pygame.draw.circle(screen, REVEALED_COLOR, obj, 5)

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BACKGROUND_COLOR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_pos[0] -= 5
        if keys[pygame.K_RIGHT]:
            player_pos[0] += 5
        if keys[pygame.K_UP]:
            player_pos[1] -= 5
        if keys[pygame.K_DOWN]:
            player_pos[1] += 5

        # Draw player
        pygame.draw.circle(screen, (0, 0, 255), player_pos, 10)

        # Reveal objects
        reveal_objects()

        # Draw hidden and revealed objects
        draw_hidden_objects()
        draw_revealed_objects()

        # Draw sound wave radius
        pygame.draw.circle(screen, (255, 0, 0), player_pos, SOUND_WAVE_RADIUS, 1)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()