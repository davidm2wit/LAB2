import pygame
from Ball import *
from pygame import draw
from random import randint
import random
import numpy as np
from pygame import color


BLACK = (0,0,0)
WHITE = (255,255,255)
WIDTH = 800
HEIGHT = 480
BORDER = 20
COLOR = pygame.Color(255,0,245)
VELOCITY = 5

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


def main(): 
    pygame.init()

    pygame.display.set_caption("pong")




    surface = pygame.display.set_mode((WIDTH,HEIGHT))
    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    wall_top = Wall(0,0,WIDTH,BORDER,COLOR,screen)
    wall_bottom = Wall(0,HEIGHT-BORDER,WIDTH,BORDER,COLOR,screen)
    wall_left = Wall(0,0,BORDER,HEIGHT,COLOR,screen)

    
    #ball init
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT//2 
    angle = random.randrange(-45,45)
    vx0 = -VELOCITY * np.abs(np.cos(angle))
    vy0 = VELOCITY * np.abs(np.sin(angle))
    print(angle)
    ball = Ball(x0,y0,vx0,vy0,surface,COLOR,BLACK)

    ball.show(COLOR)
    pygame.display.update()
    



    # define a variable to control the main loop
    running = True

    clock = pygame.time.Clock()
    
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            #all_sprites_list.update()
        screen.fill(BLACK)
        wall_left.draw()
        wall_top.draw()
        wall_bottom.draw()
        ball.update()


        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
