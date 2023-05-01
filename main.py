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

class outPin:
    def __init__(self, rect, state, type, gpioobject):
        self.rect = rect
        self.state = state
        self.type = type
        self.gpioobject = gpioobject
        return
    
    def onClick(self):
        self.state = not(self.state)
        if self.state:
            screen.blit(GREEN, self.rect)
            self.gpioobject.on() 
        else:
            screen.blit(RED, self.rect)
            self.gpioobject.off()
        return
        

class IOPin:
    def __init__(self, rect, state, pin):
        self.rect = rect
        self.state = state
        self.pin = pin
        self.gpioobject = gpiozero.OutputDevice(self.pin)
        return
    
    def output(self):
        self.OUTPUT = True
        self.gpioobject.close()
        self.gpioobject = gpiozero.OutputDevice(self.pin)
        return
    
    def input(self):
        self.OUTPUT = False
        self.gpioobject.close()
        self.gpioobject = gpiozero.InputDevice(self.pin)
        return
    
    def onClick(self):
        if self.OUTPUT:
            pass
        else:
            return
        



pins = [
    outPin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(21)),
    outPin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(20)),
    outPin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(26)),
    outPin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(16)),
    outPin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(19)),
    outPin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(13)),
    outPin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(12)),
    outPin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(6)),
    outPin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(5)),
    outPin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(7)),
    outPin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(8)),
    outPin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(11)),
    outPin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(25)),
    outPin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(9)),
    outPin(Rect(), False, "ADDRESS", gpiozero.OutputDevice(10)),
    outPin(Rect(), False, "WE", gpiozero.OutputDevice(14, False, False)),
    outPin(Rect(), False, "OE", gpiozero.OutputDevice(3, False, False)),
    IOPin(Rect(), False, 24),
    IOPin(Rect(), False, 23),
    IOPin(Rect(), False, 22),
    IOPin(Rect(), False, 27),
    IOPin(Rect(), False, 17),
    IOPin(Rect(), False, 18),
    IOPin(Rect(), False, 15),
    IOPin(Rect(), False, 4)
    ]

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
            for pin in pins:
                if pin.rect.collidepoint(point):
                    pin.onClick()


    
    
    pygame.display.flip()

