import sys
import pygame

pygame.init()

screensize = width, height = 500, 500
board = pygame.image.load('Images/test.png')

screen = pygame.display.set_mode(screensize)
#screen.fill(black)

def main():
    while True:
        screen.fill([255,255,255])
        screen.blit(board, (0,0))
        pygame.display.flip()

main()