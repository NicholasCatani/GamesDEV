### Basic Collision Detection

import pygame
import sys

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Collision Detection Example")

# Define colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# Create rectangles for player and obstacle
player_rect = pygame.Rect(100, 100, 50, 50)
obstacle_rect = pygame.Rect(200, 200, 100, 100)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get pressed keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 1
    if keys[pygame.K_RIGHT]:
        player_rect.x += 1
    if keys[pygame.K_UP]:
        player_rect.y -= 1
    if keys[pygame.K_DOWN]:
        player_rect.y += 1

    # Check for collision
    if player_rect.colliderect(obstacle_rect):
        print("Collision!")

    # Update display
    screen.fill(white)
    pygame.draw.rect(screen, blue, player_rect)
    pygame.draw.rect(screen, red, obstacle_rect)
    pygame.display.flip()




