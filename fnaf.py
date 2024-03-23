import pygame
from pygame.locals import *
from sys import exit
import time

pygame.init()

tela_largura = 1280
tela_altura = 720

tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption('FNAF')

caminho_fonte = "fonts/pixChicago.ttf"
fonte = pygame.font.Font(caminho_fonte, 32)
fundo = pygame.image.load("images/Background.png")

tempo_inicial = pygame.time.get_ticks() // 1000
contador_segundos = 0
horario = 0
num_noite = 1

cena = 1
camera = '1a'

pos_bonnie = '1a'
pos_freddy = '1a'
pos_chica = '1a'
pos_foxy = '1c'

bonnie_level = 0
chica_level = 0
freddy_level = 0
fox_level = 0

pos_horaX = 30
pos_horaY = 80
pos_noiteX = 30
pos_noiteY = 20


level_enhanced2 = False
level_enhanced3 = False
level_enhanced4 = False



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

        tempo_atual = pygame.time.get_ticks() // 1000  # Tempo em segundos
        contador_segundos: int = tempo_atual - tempo_inicial

        if 0 <= contador_segundos < 85:
            horario = 0
        elif 85 <= contador_segundos < 170:
            horario = 1
        elif 170 <= contador_segundos < 255:
            horario = 2
        elif 255 <= contador_segundos < 340:
            horario = 3
        elif 340 <= contador_segundos < 425:
            horario = 4
        elif 425 <= contador_segundos < 510:
            horario = 5
        elif contador_segundos == 595:
            horario = 6

        tela.blit(fundo, (0, 0))

        if num_noite == 1:
            mostrar_noite = fonte.render('Night 1', True, (255, 255, 255))
            tela.blit(mostrar_noite, (pos_noiteX, pos_noiteY))
            bonnie_level = 0
            chica_level = 0
            fox_level = 0
            freddy_level = 0

        if horario == 0:
            mostrar_horas = fonte.render('12 AM', True, (255, 255, 255))
            tela.blit(mostrar_horas, (pos_horaX, pos_horaY))
            level_enhanced2 = False
            level_enhanced3 = False
            level_enhanced4 = False
        elif horario == 1:
            mostrar_horas = fonte.render('1 AM', True, (255, 255, 255))
            tela.blit(mostrar_horas, (pos_horaX, pos_horaY))
        elif horario == 2:
            mostrar_horas = fonte.render('2 AM', True, (255, 255, 255))
            tela.blit(mostrar_horas, (pos_horaX, pos_horaY))
            if level_enhanced2 == False:
                level_enhanced2 = True
                bonnie_level += 1
        elif horario == 3:
            mostrar_horas = fonte.render('3 AM', True, (255, 255, 255))
            tela.blit(mostrar_horas, (pos_horaX, pos_horaY))
            if level_enhanced3 == False:
                level_enhanced3 = True
                bonnie_level += 1
                chica_level += 1
                fox_level += 1
        elif horario == 4:
            mostrar_horas = fonte.render('4 AM', True, (255, 255, 255))
            tela.blit(mostrar_horas, (pos_horaX, pos_horaY))
            if level_enhanced4 == False:
                level_enhanced4 = True
                bonnie_level += 1
                chica_level += 1
                fox_level += 1
        elif horario == 5:
            mostrar_horas = fonte.render('5 AM', True, (255, 255, 255))
            tela.blit(mostrar_horas, (pos_horaX, pos_horaY))
        elif horario == 6:
            cena = 1

        if pos_chica == '1a':
            pygame.draw.rect(tela, (255, 255, 0), (779, 80, 38, 38))
        if pos_freddy == '1a':
            pygame.draw.rect(tela, (139, 69, 19), (839, 80, 38, 38))
        if pos_bonnie == '1a':
            pygame.draw.rect(tela, (128, 0, 128), (719, 80, 38, 38))

        if pos_foxy == '1c':
            pygame.draw.rect(tela, (255, 54, 54), (503, 309, 38, 38))


    pygame.display.update()
