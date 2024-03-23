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

porta_esquerda = False
porta_direita = False

pos_seta_menu = 1
sorteio = 0

def reset_game():
    porta_direita = False
    porta_direita = False
    level_enhanced2 = False
    level_enhanced3 = False
    level_enhanced4 = False
    pos_bonnie = '1a'
    pos_freddy = '1a'
    pos_chica = '1a'
    pos_foxy = '1c'
    tempo_inicial = pygame.time.get_ticks() // 1000
    contador_segundos = 0
    horario = 0




while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if cena == 1:
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if pos_seta_menu == 1:
                        bonnie_level = 0
                        chica_level = 0
                        foxy_level = 0
                        freddy_level = 0
                        num_noite = 1
                        reset_game()
                        cena = 2
                    elif pos_seta_menu == 2:
                        bonnie_level = 3
                        chica_level = 1
                        foxy_level = 1
                        freddy_level = 0
                        num_noite = 2
                        reset_game()
                        cena = 2
                    elif pos_seta_menu == 3:
                        bonnie_level = 0
                        chica_level = 5
                        foxy_level = 2
                        freddy_level = 1
                        num_noite = 3
                        cena = 2
                        reset_game()
                    elif pos_seta_menu == 4:
                        bonnie_level = 2
                        chica_level = 4
                        foxy_level = 6
                        nivel_freddy = random.randint(1,2)
                        if nivel_freddy == 1:
                            nivel_freddy = 1
                        else:
                            nivel_freddy = 2
                        num_noite = 4
                        reset_game()
                        cena = 2
                    elif pos_seta_menu == 5:
                        bonnie_level = 5
                        chica_level = 7
                        foxy_level = 5
                        freddy_level = 3
                        num_noite = 5
                        reset_game()
                        cena = 2
                    elif pos_seta_menu == 6:
                        bonnie_level = 10
                        chica_level = 12
                        foxy_level = 16
                        freddy_level = 4
                        num_noite = 6
                        reset_game()
                        cena = 2
                elif event.key == K_UP:
                    if pos_seta_menu == 1:
                        pos_seta_menu = 6
                    elif pos_seta_menu == 2:
                        pos_seta_menu = 1
                    elif pos_seta_menu == 3:
                        pos_seta_menu = 2
                    elif pos_seta_menu == 4:
                        pos_seta_menu = 3
                    elif pos_seta_menu == 5:
                        pos_seta_menu = 4
                    elif pos_seta_menu == 6:
                        pos_seta_menu = 5



    if cena == 1:
        titulo = fonte.render("FNAF AI", True, (255, 255, 255))
        tela.blit(titulo, (65, 65))
        noite_1 = fonte.render("Noite 1", True, (255, 255, 255))
        tela.blit(noite_1, (65, 165))
        noite_2 = fonte.render("Noite 2", True, (255, 255, 255))
        tela.blit(noite_2, (65, 225))
        noite_3 = fonte.render("Noite 3", True, (255, 255, 255))
        tela.blit(noite_3, (65, 285))
        noite_4 = fonte.render("Noite 4", True, (255, 255, 255))
        tela.blit(noite_4, (65, 345))
        noite_5 = fonte.render("Noite 5", True, (255, 255, 255))
        tela.blit(noite_5, (65, 405))
        noite_6 = fonte.render("Noite 6", True, (255, 255, 255))
        tela.blit(noite_6, (65, 465))

        seta = fonte.render("<", True, (255, 255, 255))

        if pos_seta_menu == 1:
            tela.blit(seta, (255, 165))
        elif pos_seta_menu == 2:
            tela.blit(seta, (255, 225))
        elif pos_seta_menu == 3:
            tela.blit(seta, (255, 285))
        elif pos_seta_menu == 4:
            tela.blit(seta, (255, 345))
        elif pos_seta_menu == 5:
            tela.blit(seta, (255, 405))
        elif pos_seta_menu == 6:
            tela.blit(seta, (255, 465))

    elif cena == 2:

        relogio.tick(1)
        tempo_atual = pygame.time.get_ticks() // 1000  # Tempo em segundos
        contador_segundos: int = tempo_atual - tempo_inicial

        if contador_segundos % 5 == 0:
            numero_sorteado = random.randint(1, 20)
            sorteio = numero_sorteado
            if bonnie_level >= numero_sorteado:
                if pos_bonnie == '1a':
                    pos_bonnie = '1b'
                elif pos_bonnie == '1b':
                    bonnie_move = random.randint(1, 2)
                    if bonnie_move == 1:
                        pos_bonnie = '2a'
                    elif bonnie_move == 2:
                        pos_bonnie = '5'
                    elif bonnie_move == 3:
                        pos_bonnie = '1a'
                elif pos_bonnie == '2a':
                    bonnie_move = random.randint(1, 3)
                    if bonnie_move == 1:
                        pos_bonnie = '2b'
                    elif bonnie_move == 2:
                        pos_bonnie = '1b'
                    elif bonnie_move == 3:
                        pos_bonnie = '3'
                elif pos_bonnie == '3':
                    pos_bonnie = '2a'
                elif pos_bonnie == '5':
                    pos_bonnie = '1b'
                elif pos_bonnie == '2b':
                    if porta_esquerda:
                        pos_bonnie = '2a'
                    else:
                        cena = 3

            if chica_level >= numero_sorteado:
                if pos_chica == '1a':
                    pos_chica = '1b'
                elif pos_chica  == '1b':
                    chica_movimento = random.randint(1,4)
                    if chica_movimento == 1:
                        pos_chica = '7'
                    elif chica_movimento == 2:
                        pos_chica = '6'
                    elif chica_movimento == 3:
                        pos_chica = '4a'
                elif pos_chica == '7':
                    pos_chica = '1b'
                elif pos_chica == '6':
                    pos_chica = '1b'
                elif pos_chica == '4a':
                    chica_movimento = random.randint(1,2)
                    if chica_movimento == 1:
                        pos_chica = '4b'
                    else:
                        pos_chica = '1b'
                elif pos_chica == '4b':
                    if not porta_direita:
                        cena = 3
                    else:
                        pos_chica = '4a'


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

        mostrar_noite = fonte.render('Noite ' + str(num_noite), True, (255, 255, 255))
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
        elif pos_chica == '1b':
            pygame.draw.rect(tela, (255, 255, 0), (903, 237, 38, 38))
        elif pos_chica == '7':
            pygame.draw.rect(tela, (255, 255, 0), (1074, 236, 38, 38))
        elif pos_chica == '6':
            pygame.draw.rect(tela, (255, 255, 0), (1040, 451, 38, 38))
        elif pos_chica == '4a':
            pygame.draw.rect(tela, (255, 255, 0), (887, 441, 38, 38))
        elif pos_chica == '4b':
            pygame.draw.rect(tela, (255, 255, 0), (887, 575, 38, 38))


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

        numero_sort = fonte.render("Número: " + str(sorteio), True, (255, 255, 255))
        tela.blit(numero_sort, (pos_horaX, 240))
        nivel_bonnie = fonte.render("Bonnie: " + str(bonnie_level), True, (255, 255, 255))
        tela.blit(nivel_bonnie, (pos_horaX, 240+60))
        nivel_chica = fonte.render("Chica: " + str(chica_level), True, (255, 255, 255))
        tela.blit(nivel_chica, (pos_horaX, 300+60))
        nivel_foxy = fonte.render("Foxy: " + str(foxy_level), True, (255, 255, 255))
        tela.blit(nivel_foxy, (pos_horaX, 360+60))
        nivel_freddy = fonte.render("Freddy: " + str(freddy_level), True, (255, 255, 255))
        tela.blit(nivel_freddy, (pos_horaX, 420+60))

    elif cena == 3:
        game_over = fonte.render("Game Over" + str(bonnie_level), True, (255, 255, 255))
        tela.blit(game_over, (640, 360))

    pygame.display.update()
