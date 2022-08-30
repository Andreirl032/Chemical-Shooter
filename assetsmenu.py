import pygame
pygame.init()
size=width,height = 1280,720
screen=pygame.display.set_mode(size)
clock=pygame.time.Clock()

font= pygame.font.Font(None,100, bold=True)
text=font.render("INICIAR",True,("white"),("blue"))
textRect=text.get_rect()
textRect.center=640,450

fontquit2= pygame.font.Font(None,100, bold=True)
text2=fontquit2.render("CONTROLES",True,("white"),("blue"))
textRect2=text2.get_rect()
textRect2.center=640,550

fontquit3= pygame.font.Font(None,100, bold=True)
text3=fontquit3.render("SAIR",True,("white"),("blue"))
textRect3=text3.get_rect()
textRect3.center=640,650

menuimage=pygame.image.load("chemical-plant.jpg").convert()
menuimagerect=menuimage.get_rect()

controlsimage=pygame.image.load("white-chemical-plant.jpeg").convert()
controlsimage=pygame.transform.scale(controlsimage,(1279,1855))
controlsimagerect=menuimage.get_rect()

title=pygame.image.load("chemical title piskel1.png").convert_alpha()
title=pygame.transform.scale(title,(640,360))
titlerect=menuimage.get_rect()

black=pygame.image.load("blackjpg.jpg").convert()
blackrect=black.get_rect()

soundimg=pygame.image.load("soundpng.png").convert_alpha()
soundimg=pygame.transform.scale(soundimg,(150,80))

nosoundimg=pygame.image.load("nosoundpng.png").convert_alpha()
nosoundimg=pygame.transform.scale(nosoundimg,(150,80))

def textoopcoes(texto,posicaoa,posicaob):
    fontopcao= pygame.font.Font(None,80, bold=True)
    textopcao=fontopcao.render(texto,True,("black"))
    textRectopcao=textopcao.get_rect()
    textRectopcao.center=posicaoa,posicaob
    blit=screen.blit(textopcao,textRectopcao)
    return blit

def imagensopcoes(nomeimagem,posicaoa,posicaob):    
  imagem=pygame.image.load("%s.png"%nomeimagem).convert_alpha()
  blit=screen.blit(imagem,(posicaoa,posicaob))
  return blit

fontvoltar= pygame.font.Font(None,100, bold=True)
voltar=fontvoltar.render("VOLTAR",True,("white"),("blue"))
voltarrect=voltar.get_rect()
voltarrect.center=1100,80

nosecrets=pygame.font.Font(None,100, bold=True)
textnosecrets=nosecrets.render("JÁ CHEGA DE SEGREDOS, NÃO?",True,("white"))
textRectnosecrets=textnosecrets.get_rect()
textRectnosecrets.center=640,360