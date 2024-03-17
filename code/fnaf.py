import pygame
from pygame.locals import *
from sys import exit

pygame.init()

tela_largura = 1280
tela_altura = 720

tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption('FNAF')

caminho_fonte = "/fonts/pixChicago.ttf"
fonte = pygame.font.Font(caminho_fonte, 22)

relogio = pygame.time.Clock()
cena = 1
camera = '1a'

pos_bonnie = '1a'
pos_freddy = '1a'
pos_chica = '1a'
pos_foxy = '1c'

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                tela.fill((0,0, 0))
                if cena == 1:
                    cena = 2
                elif cena == 2:
                    cena = 1

    if cena == 1:
        pygame.draw.rect(tela, (255, 0, 0), (400, 0, 100, 50))
    elif cena == 2:
        if camera == '1a':
            text_surface = fonte.render('Câmera 1a', True, (255,255,255))
            rect = pygame.Rect(100, 100, 200, 100)
            pygame.draw.rect(tela, (255,255,255), rect, 2)
            text_rect = text_surface.get_rect(center=rect.center)
            tela.blit(text_surface, text_rect)

            if pos_chica == '1a':
                pygame.draw.rect(tela, (255, 255, 0), (400, 400, 50, 50))
            if pos_freddy == '1a':
                pygame.draw.rect(tela, (139, 69, 19), (500, 400, 50, 50))
            if pos_bonnie == '1a':
                pygame.draw.rect(tela, (128, 0, 128), (300, 400, 50, 50))

    pygame.display.update()
