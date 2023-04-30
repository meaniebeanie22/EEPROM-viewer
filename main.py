# need to add:
# rects for each pin box
# method of detecting which pin has been clicked
# doing something about it

# pygame setups
black = 0, 0, 0
import gpiozero # pi GPIO
import pygame, sys
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("EEPROM viewer")

# pin maps
ADDRESS = [gpiozero.OutputDevice(21), 
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
           gpiozero.OutputDevice(10)]
IO = [24, 23, 22, 27, 17, 18, 15, 4]
WE = gpiozero.OutputDevice(14, False, False)
OE = gpiozero.OutputDevice(3, False, False)



# eeprom image
EEPROM = pygame.image.load("EEPROM.png")
EEPROM = pygame.transform.scale(EEPROM, (500, 600))
EEPROMrect = pygame.Rect(50,0,500,600)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    screen.blit(EEPROM, EEPROMrect)
    pygame.display.flip()

