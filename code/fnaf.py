import pygame
from pygame.locals import *
from sys import exit

pygame.init()

tela_largura = 1280
tela_altura = 720

tela = pygame.display.set_mode((tela_largura, tela_altura))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

