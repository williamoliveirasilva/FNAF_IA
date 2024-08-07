import pygame
from pygame.locals import *
from sys import exit
import time
import random
import draw
import config
from animatronic import Animatronic
from animatronic import Foxy

pygame.init()

tela_largura = 1280
tela_altura = 720

tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption('FNAF: Simulador de IA')
icone = pygame.image.load('images/spt_goldenfreddy.png')
pygame.display.set_icon(icone)

caminho_fonte = "fonts/pixChicago.ttf"
fonte = pygame.font.Font(caminho_fonte, 32)
fundo = pygame.image.load("images/Background.png")
fundo_apagado = pygame.image.load('images/Backgroud_SEnergia.png')
fundo_menu1 = pygame.image.load('images/background_menu1.png')
fundo_menu2 = pygame.image.load('images/background_menu2.png')
fundo_menu3 = pygame.image.load('images/background_menu3.png')

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
stg_foxy = '1'

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

left_door = False
right_door = False

pos_seta_menu = 1
sorteio = 0

bonnie_sprite = pygame.image.load('images/spt_bonnie.png')
chica_sprite = pygame.image.load('images/spt_chica.png')
freddy_sprite = pygame.image.load('images/spt_freddy.png')
foxy_sprite = pygame.image.load('images/spt_foxy.png')
piratecove1_sprite = pygame.image.load('images/spt_piratecove1.png')
piratecove2_sprite = pygame.image.load('images/spt_piratecove2.png')
piratecove3_sprite = pygame.image.load('images/spt_piratecove3.png')
piratecove4_sprite = pygame.image.load('images/spt_piratecove4.png')

image_gameOver = pygame.image.load('images/gameoverscreen.png')

som_movimentoBonnie = pygame.mixer.Sound('sounds/BonnieChicamoving.ogg')
som_menu = pygame.mixer.Sound('sounds/FNAFMenumusic.ogg')
som_chicaCozinha = pygame.mixer.Sound('sounds/ChicaKitchen.ogg')
som_gameOver = pygame.mixer.Sound('sounds/Static.ogg')
som_porta = pygame.mixer.Sound('sounds/PORTA.ogg')
som_vitoria = pygame.mixer.Sound('sounds/Chimes_2.ogg')
som_ambiente = pygame.mixer.Sound('sounds/EerieAmbienceLargeSca_MV005.ogg')
som_semEnergia = pygame.mixer.Sound('sounds/Powerdown.ogg')

som_ambiente.set_volume(0.15)

nivel_energia = 100

camera_1c = False


def draw_buttons():
    botao_esquerdo = pygame.Rect(543, 624, 31, 58)
    botao_direito = pygame.Rect(1021, 624, 31, 58)
    botao_base_esquerda = pygame.Rect(540, 619, 37, 69)
    botao_base_direita = pygame.Rect(1018, 619, 37, 69)

    pygame.draw.rect(tela, (155, 155, 155), botao_base_esquerda)
    pygame.draw.rect(tela, (155, 155, 155), botao_base_direita)

    if left_door:
        pygame.draw.rect(tela, (0, 255, 0), botao_esquerdo)
    else:
        pygame.draw.rect(tela, (255, 0, 0), botao_esquerdo)

    if right_door:
        pygame.draw.rect(tela, (0, 255, 0), botao_direito)
    else:
        pygame.draw.rect(tela, (255, 0, 0), botao_direito)


def draw_doors():
    if nivel_energia > 0:
        desenho_porta_direita = pygame.Rect(840, 591, 21, 16)
        desenho_porta_esquerda = pygame.Rect(734, 591, 21, 16)
        if right_door:
            pygame.draw.rect(tela, (155, 155, 155), desenho_porta_direita)

        if left_door:
            pygame.draw.rect(tela, (155, 155, 155), desenho_porta_esquerda)


bonnie = Animatronic()
chica = Animatronic()
foxy = Foxy()
freddy = Animatronic()

def reset_animatronics():
    bonnie.setPosition('1a')
    chica.setPosition('1a')
    foxy.position('1c')
    foxy.setStage('1')
    freddy.setPosition('1a')

def reset_game():
    porta_direita = False
    porta_direita = False
    level_enhanced2 = False
    level_enhanced3 = False
    level_enhanced4 = False
    reset_animatronics()
    tempo_inicial = pygame.time.get_ticks() // 1000
    contador_segundos = 0
    horario = 0
    nivel_energia = 100
    return


def mostrar_nivel():
    nivel_bonnie = fonte.render("Bonnie: " + str(bonnie.level), True, (255, 255, 255))
    tela.blit(nivel_bonnie, (pos_horaX, 240 + 60))
    nivel_chica = fonte.render("Chica: " + str(chica.level), True, (255, 255, 255))
    tela.blit(nivel_chica, (pos_horaX, 300 + 60))
    nivel_foxy = fonte.render("Foxy: " + str(foxy.level), True, (255, 255, 255))
    tela.blit(nivel_foxy, (pos_horaX, 360 + 60))
    nivel_freddy = fonte.render("Freddy: " + str(freddy.level), True, (255, 255, 255))
    tela.blit(nivel_freddy, (pos_horaX, 420 + 60))


def noite_cumprida():
    reset_animatronics()
    cena = 4

def draw_menu_text():
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

def draw_menu_arrow():
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

while True:

    if cena == 1:
        som_ambiente.stop()
        relogio.tick(1)
        tempo_atual = pygame.time.get_ticks() // 1000
        contador_segundos: int = tempo_atual - tempo_inicial

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
                            nivel_freddy = random.randint(1, 2)
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
                    elif event.key == K_DOWN:
                        if pos_seta_menu == 1:
                            pos_seta_menu = 2
                        elif pos_seta_menu == 2:
                            pos_seta_menu = 3
                        elif pos_seta_menu == 3:
                            pos_seta_menu = 4
                        elif pos_seta_menu == 4:
                            pos_seta_menu = 5
                        elif pos_seta_menu == 5:
                            pos_seta_menu = 6
                        elif pos_seta_menu == 6:
                            pos_seta_menu = 1
        if contador_segundos % 5 == 0:
            tela.blit(fundo_menu2, (0, 0))
        elif contador_segundos % 6 == 0:
            tela.blit(fundo_menu3, (0, 0))
        else:
            tela.blit(fundo_menu1, (0, 0))

        som_menu.play()

        draw_menu_text()
        draw_menu_arrow()

    elif cena == 2:

        som_menu.stop()
        som_ambiente.play()

        relogio.tick(1)
        tempo_atual = pygame.time.get_ticks() // 1000
        contador_segundos: int = tempo_atual - tempo_inicial

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_f:
                    noite_cumprida()

                if event.key == K_LEFT:
                    if nivel_energia > 0:
                        som_porta.play()
                        if left_door:
                            left_door = False
                        else:
                            left_door = True
                if event.key == K_RIGHT:
                    if nivel_energia > 0:
                        som_porta.play()
                        if right_door:
                            right_door = False
                        else:
                            right_door = True

        if contador_segundos % 3 == 0:
            numero_sorteado = random.randint(1, 20)

            if foxy_level >= numero_sorteado:
                if not camera_1c:
                    if stg_foxy == '1':
                        stg_foxy = '2'
                    elif stg_foxy == '2':
                        stg_foxy = '3'
                    elif stg_foxy == '3':
                        stg_foxy = '4'

        if contador_segundos % 5 == 0:
            numero_sorteado = random.randint(1, 20)
            sorteio = numero_sorteado
            if bonnie_level >= numero_sorteado:
                som_movimentoBonnie.play()
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
                    if left_door:
                        pos_bonnie = '1b'
                    else:
                        cena = 3

            if chica_level >= numero_sorteado:
                som_movimentoBonnie.play()
                if pos_chica == '1a':
                    pos_chica = '1b'
                elif pos_chica == '1b':
                    chica_movimento = random.randint(1, 4)
                    if chica_movimento == 1:
                        pos_chica = '7'
                    elif chica_movimento == 2:
                        pos_chica = '6'
                        som_chicaCozinha.play()
                    elif chica_movimento == 3:
                        pos_chica = '4a'
                elif pos_chica == '7':
                    pos_chica = '1b'
                elif pos_chica == '6':
                    pos_chica = '1b'
                elif pos_chica == '4a':
                    chica_movimento = random.randint(1, 2)
                    if chica_movimento == 1:
                        pos_chica = '4b'
                    else:
                        pos_chica = '1b'
                elif pos_chica == '4b':
                    if not right_door:
                        cena = 3
                    else:
                        pos_chica = '1b'

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

        if nivel_energia < 1:
            som_ambiente.stop()
            bonnie_level = 0
            chica_level = 0
            foxy_level = 0
            freddy_level = 0
            stg_foxy = '1'
            pos_chica = '1a'
            pos_bonnie = '1a'
            pos_freddy = '1a'
            som_movimentoBonnie.stop()
            som_chicaCozinha.stop()
            som_semEnergia.play()
            stg_foxy = '0'
            pos_chica = 'x'
            pos_bonnie = 'x'
            pos_freddy = 'x'
            left_door = False
            right_door = False

        if nivel_energia > 0:
            tela.blit(fundo, (0, 0))
        else:
            tela.blit(fundo_apagado, (0,0))

        mostrar_noite = fonte.render('Noite ' + str(num_noite), True, (255, 255, 255))
        tela.blit(mostrar_noite, (pos_noiteX, pos_noiteY))

        if nivel_energia > 0:
            if num_noite == 2:
                if contador_segundos % 6 == 0:
                    nivel_energia -= 1
            elif num_noite == 3:
                if contador_segundos % 5 == 0:
                    nivel_energia -= 1
            elif num_noite == 4:
                if contador_segundos % 4 == 0:
                    nivel_energia -= 1
            elif num_noite == 5 or num_noite == 6:
                if contador_segundos % 3 == 0:
                    nivel_energia -= 1

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
            noite_cumprida()

        if pos_chica == '1a':
            tela.blit(chica_sprite, (779 - 37, 80 - 37))

        elif pos_chica == '1b':
            tela.blit(chica_sprite, (903 - 37, 237 - 37))
        elif pos_chica == '7':
            tela.blit(chica_sprite, (1074 - 37, 236 - 37))
        elif pos_chica == '6':
            tela.blit(chica_sprite, (1040 - 37, 451 - 37))
        elif pos_chica == '4a':
            tela.blit(chica_sprite, (887 - 37, 441 - 37))
        elif pos_chica == '4b':
            tela.blit(chica_sprite, (887 - 37, 575 - 37))

        if pos_freddy == '1a':
            tela.blit(freddy_sprite, (839 - 37, 80 - 37))

        if pos_bonnie == '1a':
            tela.blit(bonnie_sprite, (719 - 37, 80 - 55))
        elif pos_bonnie == '1b':
            tela.blit(bonnie_sprite, (651 - 37, 237 - 55))
        elif pos_bonnie == '5':
            tela.blit(bonnie_sprite, (475 - 37, 171 - 55))
        elif pos_bonnie == '3':
            tela.blit(bonnie_sprite, (563 - 37, 482 - 55))
        elif pos_bonnie == '2a':
            tela.blit(bonnie_sprite, (670 - 37, 441 - 55))
        elif pos_bonnie == '2b':
            tela.blit(bonnie_sprite, (670 - 37, 564 - 55))

        if stg_foxy == '1':
            tela.blit(piratecove1_sprite, (503 - 37, 309 - 37))
        elif stg_foxy == '2':
            tela.blit(piratecove2_sprite, (503 - 37, 309 - 37))
        elif stg_foxy == '3':
            tela.blit(piratecove3_sprite, (503 - 37, 309 - 37))
        elif stg_foxy == '4':
            tela.blit(piratecove4_sprite, (503 - 37, 309 - 37))
            if contador_segundos % 25 == 0:
                if not left_door:
                    cena = 3
                else:
                    stg_foxy = '1'

        if contador_segundos % 1 == 0:
            if left_door:
                nivel_energia -= 1
            if right_door:
                nivel_energia -= 1

        numero_sort = fonte.render("Energia: " + str(nivel_energia) + "%", True, (255, 255, 255))
        tela.blit(numero_sort, (pos_horaX, 240))

        draw_buttons()
        draw_doors()
        mostrar_nivel()

    elif cena == 3:
        som_ambiente.stop()
        nivel_foxy = 0
        nivel_chica = 0
        nivel_bonnie = 0
        nivel_freddy = 0
        som_chicaCozinha.stop()
        som_movimentoBonnie.stop()
        tela.blit(image_gameOver, (0, 0))
        game_over = fonte.render("Game Over", True, (255, 255, 255))
        tela.blit(game_over, (60, 350))
        game_over = fonte.render("Precione qualquer tecla", True, (255, 255, 255))
        tela.blit(game_over, (60, 400))
        som_gameOver.play()

    elif cena == 4:
        som_ambiente.stop()
        six_am = fonte.render("6 AM", True, (255, 255, 255))
        tela.blit(six_am, (60, 350))
        som_vitoria.play()

    pygame.display.update()
