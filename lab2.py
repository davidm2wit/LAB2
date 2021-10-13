import pygame
from pygame import draw

class Wall():
    def __init__(self, x, y, width, height, color, screen):
        # Init.
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.screen = screen
        # Create
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def draw(self):
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.width, self.height], 0)

pygame.init()

pygame.display.set_caption("lab2")
WIDTH = 800
HEIGHT = 480
BORDER = 20
COLOR = pygame.Color(255,0,245)
screen = pygame.display.set_mode((WIDTH,HEIGHT))

wall_top = Wall(0,0,WIDTH,BORDER,COLOR,screen)
wall_bottom = Wall(0,HEIGHT-BORDER,WIDTH,BORDER,COLOR,screen)
wall_left = Wall(0,0,BORDER,HEIGHT,COLOR,screen)

wall_top.draw()
wall_bottom.draw()
wall_left.draw()

pygame.display.update()


# define a variable to control the main loop
running = True
    
# main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False
    
     
