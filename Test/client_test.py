from turtle import st
import pygame
from Test.network_test import Network
# from pyparsing import col
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


def redrawWindow(window ,player, player2):
    """
    Drawing window, takes in a screen calledwindow and a player.
    Parameters
    ----------
        window: pygame surface
        the surface area to play on
        player: player in the game 
    """
    color = (0,1, 255)
    win.fill(color)
    player.draw(window)
    player2.draw(window)
    pygame.display.update()

def read_pos(strs):
    """
    takes in  a string inpurt and convert it to tuple of interger.
    Parameters
    ----------
        strs: str
        string input 
    """
    if strs is None:
        return
    strs = strs.split(",")
    return int(strs[0]), int(strs[1])

def make_pos(tup):
    """
    takes in a tuple and creates a string
    Parameters
    ----------
        tup: tuple
    """
    return str(tup[0]) + "," + str(tup[1])




def main():
    """
    Drawing background image, or color
    """
    run = True
    network_con = Network()
    start_pos = read_pos(network_con.get_pos())
    player1 = Player(start_pos[0],start_pos[1],100,100,(0,225,0))
    player2 = Player(0,0,100,100,(0,255,0))


    # game loop 
    while run :
        player2_pos = read_pos(network_con.send(make_pos((player1.pos_x, player1.pos_y))))
        player2.pos_x = player2_pos[0]
        player2.pos_y = player2_pos[1]
        player2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
       
        player1.move()
        redrawWindow(win, player1, player2)



main()