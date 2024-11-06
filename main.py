from recursos.funcoes import limparTela
import pygame
import random
import time

pygame.init()
tamanho = (1000,592)
clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
icone = pygame.image.load("recursos/icone.ico")

pygame.display.set_icon(icone)
pygame.display.set_caption("Corrida Maluca")

branco = (255,255,255)
preta = (0,0,0)
fundo = pygame.image.load("recursos/fundo.png")
carro1 = pygame.image.load("recursos/carro1.png")
carro2 = pygame.image.load("recursos/carro2.png")
carro3 = pygame.image.load("recursos/carro3.png")
fundo2 = pygame.image.load("recursos/fundo2.png")

#Valores:
movXCar1 = 0
movXCar2 = 0
movXCar3 = 0
posYCar1 = 45
posYCar2 = 120
posYCar3 = 185



vitoria = pygame.mixer.Sound("recursos/vitoria.mp3")
vitoria.set_volume(0.5)
pygame.mixer.music.load("recursos/trilha.mp3")
pygame.mixer.music.play(-1) #-1 looping, 1,2 3 vezes
somDaVitoria = False

acabou = False


while True:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            quit()
   
    tela.fill( branco )
    tela.blit(fundo, (0,0))
    tela.blit(carro1, (movXCar1,posYCar1))
    tela.blit(carro2, (movXCar2,posYCar2))
    tela.blit(carro3, (movXCar3,posYCar3))
    
    #fórmulas:
    dist_1_2 = abs(movXCar1 - movXCar2)
    dist_1_3 = abs(movXCar1 - movXCar3)
    dist_2_3 = abs(movXCar2 - movXCar3)
    
    d1_2 = f"Distância Carro Vermelho-Amarelo: {dist_1_2}"
    d1_3 = f"Distância Carro Vermelho-Azul: {dist_1_3}"
    d2_3 = f"Distância Carro Amarelo-Azul: {dist_2_3}"
    
    if not acabou :
        movXCar1 = movXCar1 + random.randint(0,8)
        movXCar2 = movXCar2 + random.randint(0,8)
        movXCar3 = movXCar3 + random.randint(0,8)
    else:
        pygame.mixer.music.stop()
        if somDaVitoria == False:
            pygame.mixer.Sound.play(vitoria)
            somDaVitoria = True
        
    
    if movXCar1 > 1000:
        movXCar1 = 0
        posYCar1 = 340
        
    if movXCar2 > 1000:
        movXCar2 = 0
        posYCar2 = 420
    
    if movXCar3 > 1000:
        movXCar3 = 0
        posYCar3 = 490
    
    fonte = pygame.font.Font("freesansbold.ttf",40)
    textoVermelho = fonte.render("Vermelho Ganhou!", True, branco)
    textoAmarelo = fonte.render("Amarelo Ganhou!", True, branco)
    textoAzul = fonte.render("Azul Ganhou!", True, branco)
    
    #variavel das dist
    textoDist_1_2 = fonte.render(d1_2, True, branco)
    textoDist_1_3 = fonte.render(d1_3, True, branco)
    textoDist_2_3 = fonte.render(d2_3, True, branco)
    
    if posYCar1 == 340 and movXCar1 >= 908 and (movXCar1 > movXCar2 and movXCar3):
        tela.blit(textoVermelho, (270,70))
        acabou = True
        
        
    elif posYCar2 == 420 and movXCar2 >= 908 and (movXCar2 > movXCar1 and movXCar3):
        tela.blit(textoAmarelo, (270,180))
        acabou = True
        
        
    elif posYCar3 == 490 and movXCar3 >= 908 and (movXCar3 > movXCar1 and movXCar2):
        tela.blit(textoAzul, (270,180))
        acabou = True
        
    
    if acabou == True:
        tela.blit(fundo2, (0,0))
    
    if posYCar1 == 340 and movXCar1 >= 908 and (movXCar1 > movXCar2 and movXCar3):
        tela.blit(textoVermelho, (350,80))
        acabou = True
        #exibição das distancias:
        tela.blit(textoDist_1_2, (129,166))
        tela.blit(textoDist_1_3, (129,237))
        tela.blit(textoDist_2_3, (129,310))
        
        
    elif posYCar2 == 420 and movXCar2 >= 908 and (movXCar2 > movXCar1 and movXCar3):
        tela.blit(textoAmarelo, (350,80))
        acabou = True
        #exibição das distancias:
        tela.blit(textoDist_1_2, (129,166))
        tela.blit(textoDist_1_3, (129,237))
        tela.blit(textoDist_2_3, (129,310)) 
        
        
    elif posYCar3 == 490 and movXCar3 >= 908 and (movXCar3 > movXCar1 and movXCar2):
        tela.blit(textoAzul, (350,80))
        acabou = True
        #exibição das distancias:
        tela.blit(textoDist_1_2, (129,166))
        tela.blit(textoDist_1_3, (129,237))
        tela.blit(textoDist_2_3, (129,310))
    
    
        
    pygame.display.update()
    clock.tick(80)