import sys
import pygame
#test van bunyamin 
pygame.init()

screensize = width, height = 1000, 600
circle = pygame.transform.scale(pygame.image.load('Images/circle.jpg'), (30,30))
board = pygame.transform.scale(pygame.image.load('Images/board.png'), (600,600))

startmenu = pygame.display
screen = pygame.display.set_mode(screensize)
#screen.fill(black)

def main():
    while True:#Main game loop
       screen.blit(board, (0, 0))
       screen.blit(circle, (10,10))
       pygame.display.update()
main()