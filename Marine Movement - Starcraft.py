##### Starcraft #####
#The making of a Marine!

import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Marine Movement Example")

# Colors
white = (255, 255, 255)
marine_color = (0, 0, 255)

# Marine class
class Marine:
    def __init__(self, x, y):
        # Load marine sprite sheet
        sprite_sheet = pygame.image.load(os.path.join(os.path.dirname(__file__), "frames.png"))

        # Define the dimensions of each frame in the sprite sheet
        frame_width = sprite_sheet.get_width() // 17
        frame_height = sprite_sheet.get_height() // 14

        # Store each frame as a separate image in a list
        self.frames = []
        for row in range(14):
            for col in range(17 if row < 13 else 8):
                frame = sprite_sheet.subsurface((col * frame_width, row * frame_height, frame_width, frame_height))
                self.frames.append(frame)

        # Initialize frame index and image
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

        # Set the position of the marine
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

        # Animation-related variables
        self.animation_speed = 5  # Adjust the speed of animation

    def move_towards(self, target_x, target_y):
        angle = pygame.math.Vector2(target_x - self.rect.x, target_y - self.rect.y).angle_to((1, 0))
        self.rect.x += self.speed * pygame.math.Vector2(1, 0).rotate(-angle).x
        self.rect.y += self.speed * pygame.math.Vector2(1, 0).rotate(-angle).y

        # Update animation frame
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.image = self.frames[self.frame_index]

# Create a Marine
marine = Marine(50, 50)

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
        target_x, target_y = event.pos
        marine.move_towards(target_x, target_y)

    # Update display
    screen.fill(white)
    screen.blit(marine.image, marine.rect)

    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)