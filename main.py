# need to add:
# rects coords for each pin box
# a way to change between an IO being in or out (little I or O next to each IO pin - click on it to change DD)
# t e s t i n g
import gpiozero # pi GPIO
import pygame, sys
from time import sleep

black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("EEPROM viewer")
# pin maps
class IOSwitch:
    def __init__(self, rect, bound):
        self.rect = rect
        self.bound = bound
        return
    
    def onClick(self):
        if self.bound.OUTPUT:
            self.bound.input()
        else:
            self.bound.output()
        
        return
    
    def renderState(self):
        if self.bound.OUTPUT:
            # render an O next to the right pin
            pass
        else:
            # render an I next to the bound pin
            pass
        return

class outPin:
    def __init__(self, rect, state, type, gpioobject):
        self.rect = rect
        self.state = state
        self.type = type
        self.gpioobject = gpioobject
        if self.state:
            self.gpioobject.on() 
        else:
            self.gpioobject.off()
        return
    
    def onClick(self):
        self.state = not(self.state)
        self.gpioobject.toggle()
        return
    
    def renderState(self):
        if self.state:
            screen.blit(GREEN, self.rect)
        else:
            screen.blit(RED, self.rect)
        return
        

class IOPin:
    def __init__(self, rect, state, pin):
        self.rect = rect
        self.state = state
        self.pin = pin
        self.gpioobject = gpiozero.OutputDevice(self.pin)
        self.OUTPUT = True # by default, all io pins start as outputs
        return

    def renderState(self):
        if self.state:
            screen.blit(GREEN, self.rect)
        else:
            screen.blit(RED, self.rect)
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
            self.state = not(self.state)
            self.gpioobject.toggle()
            return
        else:
            return
    
    def setInputState(self):
        if self.OUTPUT:
            return
        else:
            self.state = bool(self.gpioobject.value())
            return

pins = [
    outPin(pygame.Rect(148,376,40,15), False, "ADDRESS", gpiozero.OutputDevice(21)),
    outPin(pygame.Rect(148,342,40,15), False, "ADDRESS", gpiozero.OutputDevice(20)),
    outPin(pygame.Rect(148,306,40,15), False, "ADDRESS", gpiozero.OutputDevice(26)),
    outPin(pygame.Rect(148,272,40,15), False, "ADDRESS", gpiozero.OutputDevice(16)),
    outPin(pygame.Rect(148,235,40,15), False, "ADDRESS", gpiozero.OutputDevice(19)),
    outPin(pygame.Rect(148,201,40,15), False, "ADDRESS", gpiozero.OutputDevice(13)),
    outPin(pygame.Rect(148,164,40,15), False, "ADDRESS", gpiozero.OutputDevice(12)),
    outPin(pygame.Rect(148,132,40,15), False, "ADDRESS", gpiozero.OutputDevice(6)),
    outPin(pygame.Rect(392,165,40,15), False, "ADDRESS", gpiozero.OutputDevice(5)),
    outPin(pygame.Rect(392,202,40,15), False, "ADDRESS", gpiozero.OutputDevice(7)),
    outPin(pygame.Rect(392,306,40,15), False, "ADDRESS", gpiozero.OutputDevice(8)),
    outPin(pygame.Rect(392,238,40,15), False, "ADDRESS", gpiozero.OutputDevice(11)),
    outPin(pygame.Rect(148,96,40,15), False, "ADDRESS", gpiozero.OutputDevice(25)),
    outPin(pygame.Rect(392,129,40,15), False, "ADDRESS", gpiozero.OutputDevice(9)),
    outPin(pygame.Rect(148,59,40,15), False, "ADDRESS", gpiozero.OutputDevice(10)),
    outPin(pygame.Rect(392,95,40,15), False, "WEB", gpiozero.OutputDevice(14)),
    outPin(pygame.Rect(392,273,40,15), False, "OEB", gpiozero.OutputDevice(3)),
    IOPin(pygame.Rect(148,413,40,15), False, 24),
    IOPin(pygame.Rect(148,448,40,15), False, 23),
    IOPin(pygame.Rect(148,484,40,15), False, 22),
    IOPin(pygame.Rect(392,519,40,15), False, 27),
    IOPin(pygame.Rect(392,485,40,15), False, 17),
    IOPin(pygame.Rect(392,449,40,15), False, 18),
    IOPin(pygame.Rect(392,415,40,15), False, 15),
    IOPin(pygame.Rect(392,379,40,15), False, 4)
]

IOSwitches = [
    IOSwitch(pygame.Rect(0,0,10,10), pins[17]),
    IOSwitch(pygame.Rect(0,10,10,10), pins[18]),
    IOSwitch(pygame.Rect(0,20,10,10), pins[19]),
    IOSwitch(pygame.Rect(0,30,10,10), pins[20]),
    IOSwitch(pygame.Rect(0,40,10,10), pins[21]),
    IOSwitch(pygame.Rect(0,50,10,10), pins[22]),
    IOSwitch(pygame.Rect(0,60,10,10), pins[23]),
    IOSwitch(pygame.Rect(0,70,10,10), pins[24])
]

# boxes are 40 wide by 15 tall
# eeprom image
GREEN = pygame.Surface((40,15))
GREEN.fill(green)
RED = pygame.Surface((40,15))
RED.fill(red)
BLACK = pygame.Surface((40,15))
BLACK.fill(black)
BLUE = pygame.Surface((40,15))
BLUE.fill(blue)
EEPROM = pygame.image.load("EEPROM.png")
EEPROM = pygame.transform.scale(EEPROM, (500, 600))
EEPROMrect = pygame.Rect(50,0,500,600)


while True:
    screen.fill(black)
    screen.blit(EEPROM, EEPROMrect)
    # go through the event queue and deal with clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN: 
            point = (event.pos[0], event.pos[1])
            # print(f'click at x: {event.pos[0]}, y: {event.pos[1]}')
            for pin in pins:
                if pin.rect.collidepoint(point):
                    pin.onClick()
    sleep(0.00001)
    # check inputs and render
    for pin in pins:
        if type(pin) == IOPin:
            pin.setInputState()
        pin.renderState()

    pygame.display.flip()