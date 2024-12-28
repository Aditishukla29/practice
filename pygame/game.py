
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Move Rectangle")

# Colors
red = (255, 0, 0)
background_color = (0, 0, 0)

# Rectangle settings
rect_width, rect_height = 50, 50
rect_x, rect_y = (screen_width - rect_width) // 2, (screen_height - rect_height) // 2
rect_speed = 5

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed
    keys = pygame.key.get_pressed()

    # Move the rectangle based on arrow key input
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    elif keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    elif keys[pygame.K_UP]:
        rect_y -= rect_speed
    elif keys[pygame.K_DOWN]:
        rect_y += rect_speed

    # Fill the background
    screen.fill(background_color)

    # Draw the rectangle
    pygame.draw.rect(screen, red, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()