# need to add:
# rects for each pin box
# method of detecting which pin has been clicked
# doing something about it
# map rects to a dictionary

import gpiozero # pi GPIO
import pygame

# pygame setup
pygame.init()
pygame.image.load("EEPROM.png")
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("EEPROM viewer")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()