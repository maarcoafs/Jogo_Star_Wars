import pygame
import random
import time
from random import randint

pygame.init()
pygameDisplay = pygame.display
pygameDisplay.set_caption("Jogo Star Wars")
altura = 811
largura = 811
tamanho = (largura, altura)
gameDisplay = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
gameEvents = pygame.event
branco = (255,255,255)
fundo = pygame.image.load("assets/fundostarwars.png")
millenniumfalcon = pygame.image.load("assets/millenniumfalcon.png")
missile = pygame.image.load("assets/missile.png")
tieadvancedx1 = pygame.image.load("assets/TIEAdvancedX1.png")
lancaMissile = 0




def escreverTexto (texto):
    fonte  = pygame.font.Font("freesansbold.ttf",15)
    textoDisplay = fonte.render(texto,True,branco)
    gameDisplay.blit(textoDisplay, (880,80))
    pygameDisplay.update()

def morreu():
    fonte  = pygame.font.Font("freesansbold.ttf",95)
    fonte2  = pygame.font.Font("freesansbold.ttf",45)
    textoDisplay = fonte.render("MORREUU !!!!",True,branco)
    textoDisplay2 = fonte2.render("press enter to continue !!!!",True,branco)
    gameDisplay.blit(textoDisplay, (150,150))
    gameDisplay.blit(textoDisplay2, (150,350))
    pygameDisplay.update()

def jogar():
    jogando = True
    lancaMissile = 0
    millenniumX = 342
    millenniumY = 650
    tieadvancedX = 0
    tieadvancedY = 30
    movimentoMillenniumX = 0
    larguraMillennium = 125
    alturaMillennium = 125
    alturaMissile = 80
    larguraMissile = 17
    posicaoMissileX = 400
    posicaoMissileY = 610
    velocidadeMissile = 10
    pygame.mixer.music.load("assets/starwarstheme.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(-1)

    missileSound = pygame.mixer.Sound("assets/missile.mp3")
    missileSound.set_volume(1)

    explosaoSound = pygame.mixer.Sound("assets/explosao.wav")
    explosaoSound.set_volume(1)
    
    
    
    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoMillenniumX = -15
                elif event.key == pygame.K_RIGHT:
                    movimentoMillenniumX = 15
                elif event.key == pygame.K_m:
                    lancaMissile = 1
                elif event.key == pygame.K_RETURN:
                    jogar()
            elif event.type == pygame.KEYUP:
                movimentoMillenniumX = 0
                
                
            
        if jogando:
            if lancaMissile == 0:
                posicaoMissileX = millenniumX + 55
            else:
                pygame.mixer.Sound.play(missileSound)
                posicaoMissileY = posicaoMissileY - velocidadeMissile
                if posicaoMissileY <0:
                    posicaoMissileX = millenniumX + 55
                    lancaMissile = 0
                    posicaoMissileY = 610
                        
                

            if millenniumX + movimentoMillenniumX >0 and millenniumX + movimentoMillenniumX < largura - larguraMillennium:
                millenniumX = millenniumX + movimentoMillenniumX
                
            gameDisplay.fill(branco)
            gameDisplay.blit(fundo,(0,0))
            gameDisplay.blit(millenniumfalcon, (millenniumX,millenniumY))
            
            tieadvancedX = randint(70,640)          
            gameDisplay.blit(tieadvancedx1, (tieadvancedX,tieadvancedY))
        
            
            gameDisplay.blit(missile, (posicaoMissileX,posicaoMissileY))

            pixelsXMillennium = list(range(millenniumX, millenniumX+larguraMillennium))
            pixelsYMillenium = list(range(millenniumY, millenniumY+alturaMillennium))

            pixelXMissile = list(range(posicaoMissileX, posicaoMissileX+larguraMissile))
            pixelYMissile = list(range(posicaoMissileY, posicaoMissileY+alturaMissile))

            colisaoY = len(list(set(pixelYMissile) & set(pixelsYMillenium) ))
            
            
            if colisaoY > 0:
                colisaoX = len(list(set(pixelXMissile) & set(pixelsXMillennium) ))
                print(colisaoX)
                if colisaoX > 45:
                    morreu()
                    jogando=False
                    pygame.mixer.music.stop()


        pygameDisplay.update()
        clock.tick(60)

jogar()