#IMPORTS
import sys
import pygame
import time
import cv2
from pygame import mixer
from assetsmenu import *
from level import Level
from tiles import Tile
from configsnivel import mapafase
from player import Player
from pause import pausestate,pauseflag,musicapause

#time.sleep(12)

#VARIAVEIS GLOBAIS
pygame.init()

levelbg=pygame.image.load("background.png").convert()
levelbg=pygame.transform.scale(levelbg,(1344,995.4))

icon=pygame.image.load("icon.png").convert_alpha()
pygame.display.set_icon(icon)
pygame.display.set_caption("Chemical Shooter")
size=width,height = 1280,720
screen=pygame.display.set_mode(size)
clock=pygame.time.Clock()
i=0
flagvideo=True
flagmenu=True
flagtroll=True
flagtroll2=True
flagnivel=0
soundflag=True
tempomenu=0
tempocontroles=0
flagnivel=True
flagnivel2=True
temponivel=0
lista=[]
codigo=["cima","cima","baixo","baixo","esquerda","direita","esquerda","direita","b","a","start"]
trollnumber=0
musica=pygame.mixer.Channel(0)
somdetiro=pygame.mixer.Channel(1)
somdepedra=pygame.mixer.Channel(2)
tempomusica=0

cap = cv2.VideoCapture('startup.mp4')
success, img = cap.read()
wn = pygame.display.set_mode(size)

captroll = cv2.VideoCapture('secret-compressed.mp4')
successtroll, imgtroll = captroll.read()
wntroll = pygame.display.set_mode(size)

captroll2 = cv2.VideoCapture('secret2-compressed.mp4')
successtroll2, imgtroll2 = captroll2.read()
wntroll2 = pygame.display.set_mode(size)

maintile=pygame.sprite.Group(Tile((100,100),200))
level=Level(mapafase,screen)

#CLASSE COM FUNÇÕES DE FASES
class Fases():
  def __init__(self):
     self.state="video"

  def video(self):
    global flagvideo
    if flagvideo:
      pygame.init()
      mixer.init()
      startupaudio=mixer.Sound("startupaudio.mp3")
      musica.set_volume(1)
      musica.play(startupaudio,0)
      flagvideo=False
    tempo=time.time()
    success=True
    while success:
        tempo2=time.time()
        if tempo2-tempo>18:
            break
        clock.tick(30)
        success, img = cap.read()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key==pygame.K_SPACE:
                mixer.music.stop()
                success = False
            if event.type==pygame.QUIT: 
              pygame.quit()
              sys.exit()
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pygame.quit() 
                sys.exit()    
        wn.blit(pygame.image.frombuffer(img.tobytes(), size, "BGR"), (0, 0))
        pygame.display.update()  
    self.state="menu"   

  def menu(self):    
    global i
    global flagmenu
    global soundflag
    global tempomenu
    #soundmenu=False
    if flagmenu:
      titlemusic=mixer.Sound("title-music.mp3")
      musica.play(titlemusic,-1)
      musica.set_volume(0.4)
      flagmenu=False
      global textRect
      global textRect2  
      global textRect3
      global lista
      global codigo
      global trollnumber
    mousepos=pygame.mouse.get_pos() 
    for event in pygame.event.get():      
      if event.type==pygame.QUIT: 
        pygame.quit()
        sys.exit()
      if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
          pygame.quit() 
          sys.exit()              
      if event.type==pygame.KEYDOWN and event.key==pygame.K_m and i>=720:
           if soundflag==True:
               tempomenu=time.time()
               musica.set_volume(0)
               somdetiro.set_volume(0)
               soundflag=False
           else:
                tempomenu=time.time()
                musica.set_volume(0.4)
                somdetiro.set_volume(0.15)
                soundflag=True
      if lista!=codigo:
            if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
                lista.append("cima")
                for j in range(len(lista)):
                    if lista[j]!=codigo[j]:
                        lista=[]
            if event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:
                lista.append("baixo")
                for j in range(len(lista)):
                    if lista[j]!=codigo[j]:
                        lista=[]
            if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
                lista.append("esquerda")
                for j in range(len(lista)):
                    if lista[j]!=codigo[j]:
                        lista=[]
            if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
                lista.append("direita")
                for j in range(len(lista)):
                    if lista[j]!=codigo[j]:
                        lista=[] 
            if event.type==pygame.KEYDOWN and event.key==pygame.K_a:
                lista.append("a")
                for j in range(len(lista)):
                    if lista[j]!=codigo[j]:
                        lista=[]
            if event.type==pygame.KEYDOWN and event.key==pygame.K_b:
                lista.append("b")
                for j in range(len(lista)):
                    if lista[j]!=codigo[j]:
                        lista=[]
            if event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN:
                lista.append("start")
                for j in range(len(lista)):
                    if lista[j]!=codigo[j]:
                        lista=[]
      if event.type==pygame.MOUSEBUTTONDOWN and textRect.collidepoint(mousepos[0],mousepos[1])==1 and i>=720:
        musica.stop()
        self.state="nivel"  
      if event.type==pygame.MOUSEBUTTONDOWN and textRect2.collidepoint(mousepos[0],mousepos[1])==1 and i>=720:
        self.state="controles"  
      if event.type==pygame.MOUSEBUTTONDOWN and textRect3.collidepoint(mousepos[0],mousepos[1])==1 and i>=720:
        pygame.quit()
        sys.exit()   
    clock.tick(60)
    screen.blit(menuimage,menuimagerect)
    screen.blit(title, (320,20))
    screen.blit(text,textRect)
    screen.blit(text2,textRect2)
    screen.blit(text3,textRect3)
    tempo2=time.time()
    if soundflag==True and tempo2-tempomenu<2:
      screen.blit(soundimg,(100,50))
    elif soundflag==False and tempo2-tempomenu<2:
      screen.blit(nosoundimg,(100,50))  
    if i<721:
      screen.blit(black,(0,i)) 
      i+=10
    if lista==codigo and trollnumber==0:
      lista=[]
      i=0
      flagmenu=True
      self.state="troll"
    elif lista==codigo and trollnumber==1:
      lista=[]
      i=0
      flagmenu=True
      self.state="troll2"
    if lista==codigo and trollnumber==2:
      screen.blit(textnosecrets,textRectnosecrets)           
    pygame.display.flip()


  def troll(self):  
    global flagtroll
    global trollnumber
    if flagtroll:
      musica.stop()
      audiotroll=mixer.Sound("secret-compressed-audiofile.mp3")
      musica.set_volume(1)
      musica.play(audiotroll,0)
      flagtroll=False
    tempo=time.time()
    success=True
    while success:
        tempo2=time.time()
        if tempo2-tempo>=77:
            break
        clock.tick(30)
        successtroll, imgtroll = captroll.read()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key==pygame.K_SPACE:
                mixer.music.stop()
                success=False
            if event.type==pygame.QUIT: 
              pygame.quit()
              sys.exit()
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pygame.quit() 
                sys.exit()    
        wntroll.blit(pygame.image.frombuffer(imgtroll.tobytes(), size, "BGR"), (0, 0))
        pygame.display.update()
    trollnumber=1
    self.state="menu"

  def troll2(self):  
    global flagtroll2
    global trollnumber
    if flagtroll2:
      musica.stop()
      audiotroll2=mixer.Sound("secret2-compressed-audiofile.mp3")
      musica.set_volume(1)
      musica.play(audiotroll2,0)
      flagtroll2=False
    tempo=time.time()
    success=True
    while success:
        tempo2=time.time()
        if tempo2-tempo>=25:
            success=False
        clock.tick(30)
        successtroll2, imgtroll2 = captroll2.read()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key==pygame.K_SPACE:
                mixer.music.stop()
                success=False
            if event.type==pygame.QUIT: 
              pygame.quit()
              sys.exit()
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pygame.quit() 
                sys.exit()    
        wntroll2.blit(pygame.image.frombuffer(imgtroll2.tobytes(), size, "BGR"), (0, 0))
        pygame.display.update()
    trollnumber=2
    self.state="menu"  
  

  def controles(self):
    global soundflag
    global tempocontroles
    global i
    mousepos=pygame.mouse.get_pos()
    for event in pygame.event.get():      
      if event.type==pygame.QUIT: 
        pygame.quit()
        sys.exit()
      if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
          pygame.quit() 
          sys.exit()      
      if event.type==pygame.KEYDOWN and event.key==pygame.K_m:
           if soundflag==True:
               tempocontroles=time.time()
               mixer.music.set_volume(0)
               soundflag=False
           else:
                tempocontroles=time.time()
                mixer.music.set_volume(0.4)
                soundflag=True
      if event.type==pygame.MOUSEBUTTONDOWN and voltarrect.collidepoint(mousepos)==1:
        self.state="menu"   
    clock.tick(60)            
    screen.blit(controlsimage,controlsimagerect)
    screen.blit(voltar,voltarrect)
    imagensopcoes("wasd",100,60)
    textoopcoes("ANDAR",640,125)
    imagensopcoes("m",97,205)
    textoopcoes("DESATIVAR/ATIVAR SOM",565,255)
    imagensopcoes("esc",97,320)
    textoopcoes("SAIR DO JOGO",430,370)
    tempo2=time.time()
    if soundflag==True and tempo2-tempocontroles<2:
      screen.blit(soundimg,(100,50))
    elif soundflag==False and tempo2-tempocontroles<2:
      screen.blit(nosoundimg,(100,50))  
    pygame.display.flip()



  def nivel(self):
    global flagnivel
    global flagnivel2
    global soundflag
    global temponivel
    global tempomusica
    global flagvivo
    tempomusica2=time.time()
    if flagnivel:
      tempomusica=time.time()
      levelmusic=mixer.Sound("cpz2-pt1.mp3")
      musica.play(levelmusic,0)
      if soundflag:
        somdetiro.set_volume(0.15)
        musica.set_volume(0.4)
        musicapause.set_volume(0.4)
      else: 
        musica.set_volume(0)
        somdetiro.set_volume(0)
        musicapause.set_volume(0)
      flagnivel=False
    if flagnivel2==True and tempomusica2-tempomusica>=61.5:
      levelmusic2=mixer.Sound("cpz2-pt2.mp3")
      musica.play(levelmusic2,-1)
      flagnivel2=False
        
    for event in pygame.event.get():      
      if event.type==pygame.QUIT: 
          pygame.quit()
          sys.exit()
      if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
          pygame.quit() 
          sys.exit()   
      if event.type==pygame.KEYDOWN and event.key==pygame.K_m:
           if soundflag==True:
               temponivel=time.time()
               somdetiro.set_volume(0)
               musica.set_volume(0)
               musicapause.set_volume(0)
               soundflag=False
           else:
                temponivel=time.time()
                somdetiro.set_volume(0.15)
                musica.set_volume(0.4)
                musicapause.set_volume(0.4)
                soundflag=True    
    screen.blit(levelbg,(0,0))
    level.run()
    level.player.sprite.bulletgroup.draw(screen)
    level.player.sprite.bulletgroup.update(level.enemy)
    tempo2=time.time()
    if soundflag==True and tempo2-temponivel<2:
      screen.blit(soundimg,(100,50))
    elif soundflag==False and tempo2-temponivel<2:
      screen.blit(nosoundimg,(100,50))
    clock.tick(60)
    pygame.display.flip()

  def morto(self):
      global soundflag
      global flagvivo
      font=pygame.font.Font(None,200, bold=True)
      text=font.render("VOCÊ MORREU",True,("white"),None)
      textRect=text.get_rect()
      textRect.center=width/2,100

      font1= pygame.font.Font(None,85, bold=True)
      text1=font1.render("CONTINUAR",True,"white","red")
      textRect1=text1.get_rect()
      textRect1.center=width/2,400

      font4= pygame.font.Font(None,85, bold=True)
      text4=font4.render("SAIR",True,"white","red")
      textRect4=text4.get_rect()
      textRect4.center=width/2,500  

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
          if event.type==pygame.MOUSEBUTTONDOWN and textRect1.collidepoint(mousepos[0],mousepos[1])==1:
                  flagvivo=True
                  self.state="nivel"
          if event.type==pygame.MOUSEBUTTONDOWN and textRect4.collidepoint(mousepos[0],mousepos[1])==1:
                  pygame.quit()
                  sys.exit()       
      screen.fill((181,27,27))
      screen.blit(text,textRect)
      screen.blit(text1,textRect1)
      screen.blit(text4,textRect4)      
      tempo2=time.time()
      if soundflag==True and tempo2-tempopause<2:
          screen.blit(soundimg,(100,50))
      elif soundflag==False and tempo2-tempopause<2:
          screen.blit(nosoundimg,(100,50)) 
      clock.tick(10)
      pygame.display.flip()


  def manager_fases(self):
    if self.state=="video":
      self.video()
    if self.state=="troll":
      self.troll()    
    if self.state=="troll2":
      self.troll2()  
    if self.state=="menu":
      self.menu()  
    if self.state=="nivel":
      self.nivel()
    if self.state=="controles":
      self.controles()
    if self.state=="morto":
      self.morto()  





fasesobj=Fases()
#LOOP INFINITO DO JOGO
while True:
    fasesobj.manager_fases()