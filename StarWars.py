import pygame
import random
import time

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
tieadvancedx1 = pygame.image.load("assets/TIEAdvancedX1.webp")




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
    millenniumX = 342
    millenniumY = 650
    movimentoMillenniumX = 0
    larguraMillennium = 125
    alturaMillennium = 125
    alturaMissile = 80
    larguraMissile = 17
    posicaoMissileX = 400
    posicaoMissileY = 610
    velocidadeMissile = 10
    lancaMissile = 0
    pontos = 0
    pygame.mixer.music.load("assets/starwarstheme.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(-1)

    missileSound = pygame.mixer.Sound("assets/missile.wav")
    missileSound.set_volume(1)
    pygame.mixer.Sound.play(missileSound)

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
                elif event.key == pygame.K_BACKSPACE:
                    lancaMissile = 1
                elif event.key == pygame.K_RETURN:
                    jogar()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    lancaMissile = 0
            movimentoMillenniumX = 0
                
                
            
        if jogando:
            if posicaoMissileY < 0 and lancaMissile == 1:
                posicaoMissileY = 610
                posicaoMissileX = millenniumX + 55
                pontos = pontos + 1
                pygame.mixer.Sound.play(missileSound)
            else:
                posicaoMissileY = posicaoMissileY - velocidadeMissile

            if millenniumX + movimentoMillenniumX >0 and millenniumX + movimentoMillenniumX < largura - larguraMillennium:
                millenniumX = millenniumX + movimentoMillenniumX
            gameDisplay.fill(branco)
            gameDisplay.blit(fundo,(0,0))
            gameDisplay.blit(millenniumfalcon, (millenniumX,millenniumY))
            
            gameDisplay.blit(missile, (posicaoMissileX,posicaoMissileY))
            escreverTexto("Pontos: "+str(pontos))

            pixelsXIron = list(range(millenniumX, millenniumX+larguraMillennium))
            pixelsYIron = list(range(millenniumY, millenniumY+alturaMillennium))

            pixelXMissile = list(range(posicaoMissileX, posicaoMissileX+larguraMissile))
            pixelYMissile = list(range(posicaoMissileY, posicaoMissileY+alturaMissile))

            colisaoY = len(list(set(pixelYMissile) & set(pixelsYIron) ))
            
            
            if colisaoY > 0:
                colisaoX = len(list(set(pixelXMissile) & set(pixelsXIron) ))
                print(colisaoX)
                if colisaoX > 45:
                    morreu()
                    jogando=False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(explosaoSound)


        pygameDisplay.update()
        clock.tick(60)

jogar()