import pygame,sys
from assetsmenu import soundimg,nosoundimg
import time
from pygame import mixer
pygame.init()
clock=pygame.time.Clock()
size=width,height = 1280,720
screen=pygame.display.set_mode(size)

font=pygame.font.Font(None,200, bold=True)
text=font.render("VOCÊ MORREU",True,("white"),None)
textRect=text.get_rect()
textRect.center=width/2,100

font4= pygame.font.Font(None,85, bold=True)
text4=font4.render("SAIR",True,"white","orange")
textRect4=text4.get_rect()
textRect4.center=width/2,500
pauseflag=False

musica=pygame.mixer.Channel(0)
somdetiro=pygame.mixer.Channel(1)
somdepedra=pygame.mixer.Channel(2)
musicapause=pygame.mixer.Channel(3)

def telamorto():
    global pauseflag
    global screen,size,clock
    soundflag=True
    tempopause=0
    musica.pause()
    musicapause=mixer.Sound("game-over-sound.mp3")
    musicapause.play(0)
    while True:
        mousepos=pygame.mouse.get_pos()
        if not soundflag:
            musica.set_volume(0)
            somdetiro.set_volume(0)
            musicapause.set_volume(0)
        else:
            musica.set_volume(0.4)
            somdetiro.set_volume(0.15)
            musicapause.set_volume(0.4)
        for event in pygame.event.get():      
            if event.type==pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pygame.quit() 
                sys.exit()
            if event.type==pygame.KEYDOWN and event.key==pygame.K_m:
                if soundflag==True:
                    tempopause=time.time()
                    musicapause.set_volume(0)
                    soundflag=False
                else:
                    tempopause=time.time()
                    musicapause.set_volume(0.4)
                    soundflag=True
            if event.type==pygame.MOUSEBUTTONDOWN and textRect4.collidepoint(mousepos[0],mousepos[1])==1:
                pygame.quit()
                sys.exit()       
        screen.fill((181,27,27))
        screen.blit(text,textRect)
        screen.blit(text4,textRect4)      
        tempo2=time.time()
        if soundflag==True and tempo2-tempopause<2:
            screen.blit(soundimg,(100,50))
        elif soundflag==False and tempo2-tempopause<2:
            screen.blit(nosoundimg,(100,50)) 
        clock.tick(10)
        pygame.display.flip()