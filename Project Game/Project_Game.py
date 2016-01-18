import sys
import pygame
import Tile

pygame.init()

screensize = width, height = 1000, 600
board = pygame.image.load('Images/board.jpg')
resizedboard = pygame.transform.scale(board, (600,600))

screen = pygame.display.set_mode(screensize)
#screen.fill(black)

def main():
    while True:#Main game loop
       screen.fill((0,0,0))
       screen.blit(resizedboard, (0, 0))
       pygame.display.flip()
main()