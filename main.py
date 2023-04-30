# need to add:
# rects for each pin box
# method of detecting which pin has been clicked
# doing something about it
# pygame setups
black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
import gpiozero # pi GPIO
import pygame, sys
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("EEPROM viewer")
Rect = pygame.Rect
# pin maps

class Pin:
    def __init__(self, rect, state, type, gpioobject):
        self.rect = rect
        self.state = state
        self.type = type
        self.gpioobject = gpioobject

outpins = [
    Pin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(21)),
    Pin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(20)),
    Pin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(26)),
    Pin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(16)),
    Pin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(19)),
    Pin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(13)),
    Pin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(12)),
    Pin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(6)),
    ]
"""
ADDRESS = [
           gpiozero.OutputDevice(21), 
           gpiozero.OutputDevice(20), 
           gpiozero.OutputDevice(26), 
           gpiozero.OutputDevice(16), 
           gpiozero.OutputDevice(19), 
           gpiozero.OutputDevice(13), 
           gpiozero.OutputDevice(12), 
           gpiozero.OutputDevice(6), 
           gpiozero.OutputDevice(5), 
           gpiozero.OutputDevice(7), 
           gpiozero.OutputDevice(8), 
           gpiozero.OutputDevice(11), 
           gpiozero.OutputDevice(25), 
           gpiozero.OutputDevice(9), 
           gpiozero.OutputDevice(10)
           ]
IO = [24, 23, 22, 27, 17, 18, 15, 4]
WE = gpiozero.OutputDevice(14, False, False)
OE = gpiozero.OutputDevice(3, False, False)
"""
# boxes are 40 wide by 15 tall
# eeprom image
GREEN = pygame.Surface((40,15)).fill(green)
RED = pygame.Surface((40,15)).fill(red)
BLACK = pygame.Surface((40,15)).fill(black)
BLUE = pygame.Surface((40,15)).fill(blue)
EEPROM = pygame.image.load("EEPROM.png")
EEPROM = pygame.transform.scale(EEPROM, (500, 600))
EEPROMrect = pygame.Rect(50,0,500,600)


while True:
    screen.fill(black)
    screen.blit(EEPROM, EEPROMrect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: 
            point = (event.pos[0], event.pos[1])
            print(f'click at x: {event.pos[0]}, y: {event.pos[1]}')


    
    
    pygame.display.flip()

