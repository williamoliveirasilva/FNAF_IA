import pygame
from pygame.locals import *
from sys import exit
import time
import random

pygame.init()

tela_largura = 1280
tela_altura = 720

tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption('FNAF')

caminho_fonte = "fonts/pixChicago.ttf"
fonte = pygame.font.Font(caminho_fonte, 32)
fundo = pygame.image.load("images/Background.png")

relogio = pygame.time.Clock()
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
foxy_level = 0

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

        relogio.tick(1)
        tempo_atual = pygame.time.get_ticks() // 1000  # Tempo em segundos
        contador_segundos: int = tempo_atual - tempo_inicial


        if contador_segundos % 5 == 0:
            numero_sorteado = random.randint(1, 20)
            if bonnie_level >= numero_sorteado:
                if pos_bonnie == '1a':
                    pos_bonnie = '1b'
                if pos_bonnie == '1b':
                    bonnie_move = random.randint(1,3)
                    if bonnie_move == 1:
                        pos_bonnie = '1a'
                    elif bonnie_move == 2:
                        pos_bonnie = '5'
                    elif bonnie_move == 3:
                        pos_bonnie = '2a'
                if pos_bonnie == '2a':
                    bonnie_move = random.randint(1,3)
                    if bonnie_move == 1:
                        pos_bonnie = '2b'
                    elif bonnie_move == 2:
                        pos_bonnie = '1b'
                    elif bonnie_move == 3:
                        pos_bonnie = '3'



            if chica_level >= numero_sorteado:
                if chica_level == '1a':
                    chica_level = '1b'


        if contador_segundos % 3 == 0:
            numero_sorteado = random.randint(1, 20)
            if freddy_level >= numero_sorteado:
                print("Freddy se moveu")

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
            if not level_enhanced2:
                level_enhanced2 = True
                bonnie_level += 1
        elif horario == 3:
            mostrar_horas = fonte.render('3 AM', True, (255, 255, 255))
            tela.blit(mostrar_horas, (pos_horaX, pos_horaY))
            if not level_enhanced3:
                level_enhanced3 = True
                bonnie_level += 1
                chica_level += 1
                foxy_level += 1
        elif horario == 4:
            mostrar_horas = fonte.render('4 AM', True, (255, 255, 255))
            tela.blit(mostrar_horas, (pos_horaX, pos_horaY))
            if not level_enhanced4:
                level_enhanced4 = True
                bonnie_level += 1
                chica_level += 1
                foxy_level += 1
        elif horario == 5:
            mostrar_horas = fonte.render('5 AM', True, (255, 255, 255))
            tela.blit(mostrar_horas, (pos_horaX, pos_horaY))
        elif horario == 6:
            cena = 1

        if pos_chica == '1a':
            pygame.draw.rect(tela, (255, 255, 0), (779, 80, 38, 38))
        elif chica_level == '1b':
            pygame.draw.rect(tela, (255, 255, 0), (903, 237, 38, 38))

        if pos_freddy == '1a':
            pygame.draw.rect(tela, (139, 69, 19), (839, 80, 38, 38))

        if pos_bonnie == '1a':
            pygame.draw.rect(tela, (128, 0, 128), (719, 80, 38, 38))
        elif pos_bonnie == '1b':
            pygame.draw.rect(tela, (128, 0, 128), (651, 237, 38, 38))
        elif pos_bonnie == '5':
            pygame.draw.rect(tela, (128, 0, 128), (475, 171, 38, 38))
        elif pos_bonnie == '3':
            pygame.draw.rect(tela, (128, 0, 128), (563, 482, 38, 38))
        elif pos_bonnie == '2a':
            pygame.draw.rect(tela, (128, 0, 128), (670, 441, 38, 38))
        elif pos_bonnie == '2b':
            pygame.draw.rect(tela, (128, 0, 128), (670, 564, 38, 38))

        if pos_foxy == '1c':
            pygame.draw.rect(tela, (255, 54, 54), (503, 309, 38, 38))

        nivel_bonnie = fonte.render("Bonnie: " + str(bonnie_level), True, (255, 255, 255))
        tela.blit(nivel_bonnie, (pos_horaX, 240))
        nivel_chica = fonte.render("Chica: " + str(chica_level), True, (255, 255, 255))
        tela.blit(nivel_chica, (pos_horaX, 300))
        nivel_foxy = fonte.render("Foxy: " + str(foxy_level), True, (255, 255, 255))
        tela.blit(nivel_foxy, (pos_horaX, 360))
        nivel_freddy = fonte.render("Freddy: " + str(freddy_level), True, (255, 255, 255))
        tela.blit(nivel_freddy, (pos_horaX, 420))



    pygame.display.update()
