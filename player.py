
import pygame

""" intialize the pygame and set up window """
pygame.init()

width = 1000
height = 600

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


"Global variable to hold the current client "
clientNumber = 0 

class Player():
    """
    initilaization of our game players
    """
    def __init__(self, pos_x, pos_y , width , height , color ):
        self.pos_x= pos_x
        self.pos_y = pos_y 
        self.width = width 
        self.height = height 
        self.color = color
        self.rectangle = (self.pos_x, self.pos_y, self.width, self.height)
        self.val = 1

    def draw(self, win):
        """
        Draw a rectangle which represents our character on the screen"""
        print(self.rectangle)
        pygame.draw.rect(win, self.color, self.rectangle)

    
    def move(self):
       """" 
       Get dict of all keys to check which keys are press to create different events "
       """
       keys = pygame.key.get_pressed()
       if keys[pygame.K_LEFT]: self.pos_x -= self.val
       if keys[pygame.K_RIGHT]: self.pos_x += self.val
       if keys[pygame.K_UP]: self.pos_y -= self.val
       if keys[pygame.K_DOWN]: self.pos_y += self.val
       self.update()

    def update(self):       
       self.rectangle = (self.pos_x, self.pos_y, self.width, self.height)