# need to add:
# rects for each pin box
# method of detecting which pin has been clicked
# doing something about it
# map rects to a dictionary
black = 0, 0, 0
import gpiozero # pi GPIO
import pygame, sys
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("EEPROM viewer")

EEPROM = pygame.image.load("EEPROM.png")
EEPROMrect = EEPROM.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    screen.blit(EEPROM, EEPROMrect)
    pygame.display.flip()

