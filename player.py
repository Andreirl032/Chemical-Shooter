import pygame
from pygame import mixer
import time
from suporte import importfolder
pygame.init()
from pause import pause
from telamorto import telamorto
#from telawin import telawin

musica=pygame.mixer.Channel(0)
somdetiro=pygame.mixer.Channel(1)
somdepedra=pygame.mixer.Channel(2)

class Player(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()
        self.importplayerassets()
        self.frameindex=0
        self.animationspeed=0.15
        self.image=self.animations["idle"][self.frameindex]
        self.image=pygame.transform.scale(self.image,(56,108))
        self.rect=self.image.get_rect(topleft=position)
        self.bulletgroup=pygame.sprite.Group()


        #movimento do jogador
        self.direction=pygame.math.Vector2(0,0)
        self.speed=40
        self.gravity=0.8
        self.jumpspeed=-16
        self.jumpstate=False
        self.podepular=True
        self.isfacing=True #true é pra direita e false é pra a esquerda
        self.status="idle"
        self.atirano=False

        self.invincible=False
        self.damageCD=750
        self.vida=5

    '''def collisionflag(self,bandeiragroup):
        variavel=pygame.sprite.spritecollide(self,bandeiragroup,False)
        if variavel:
            telawin()'''

    def falldamage(self):
        if self.rect.y>=1300:
            self.vida=0    

    def vivomorto(self):
        if self.vida<=0:
            telamorto()


    def lifebar(self):
        lifebarvar=(0.2)*self.vida
        return lifebarvar

    def takeDamage(self):
        if not self.invincible:
            self.vida -= 1
            self.hurt_time = pygame.time.get_ticks()
            self.invincible = True

    def invincibleCD(self):
        if self.invincible:
            current_time = pygame.time.get_ticks()
            if current_time - self.hurt_time >= self.damageCD:
                self.invincible = False    

    #def life_UI(self):


    def create_bullet(self):
        if self.isfacing:
            bulletspeed=30
            return Bullet(self.rect.x+85,self.rect.y+35,bulletspeed)
        else:
            bulletspeed=-30     
            return Bullet(self.rect.x-5,self.rect.y+35,bulletspeed)

    def importplayerassets(self):
         playerpath = "C:/Users/andre/Downloads/Chemical Shooter/playerassets/"
         self.animations={"idle":[],"run":[],"jump":[],"shoot":[],"jumpshoot":[],"runshoot":[]}
         for animation in self.animations.keys():
             fullpath=playerpath+animation
             self.animations[animation]=importfolder(fullpath)

    def animate(self):
        animation=self.animations[self.status]

        #loop pelo frame index
        self.frameindex+=self.animationspeed
        if self.frameindex>=len(animation):     
            self.frameindex=0
        self.image=animation[int(self.frameindex)]   
        if self.status=='idle':
            self.image=pygame.transform.scale(self.image,(56,108))     
        elif self.status=='jump' or self.status=='run':
            self.image=pygame.transform.scale(self.image,(64.8,108)) 
        elif self.status=='shoot':
            self.image=pygame.transform.scale(self.image,(82.72,108))    
        elif self.status=='jumpshoot' or self.status=='runshoot':
            self.image=pygame.transform.scale(self.image,(84.64,108))   
        if not self.isfacing:
            self.image=pygame.transform.flip(self.image,True,False)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: 
            self.isfacing=True
            self.direction.x=6
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.isfacing=False
            self.direction.x=-6
        else:    
            self.direction.x=0
        if not keys[pygame.K_SPACE] and not self.jumpstate:
            self.podepular=True
        if not keys[pygame.K_SPACE] and self.jumpstate:
            self.direction.y+=self.gravity
        if keys[pygame.K_SPACE] and not self.jumpstate and self.podepular:
            self.jump()
            self.jumpstate=True
            self.podepular=False    
        if keys[pygame.K_RETURN]:   
            pause() 
  
    def pegarstatus(self):
        keys = pygame.key.get_pressed()
        global shot
        if self.direction.y<0:
            self.animationspeed=0
            self.status='jump'
        elif self.direction.y==0 and self.direction.x==0:   
            self.animationspeed=0
            self.status='idle'
        elif self.direction.x!=0 and self.direction.y==0:
            self.animationspeed=0.04
            self.status='run'
        if keys[pygame.K_q]:
            if self.direction.x!=0 and self.direction.y==0:
                self.animationspeed=0.04
                self.status="runshoot"
            elif self.direction.y<0:
                self.animationspeed=0
                self.status="jumpshoot"
            elif self.direction.x==0 and self.direction.y==0:
                self.animationspeed=0
                self.status="shoot"
            if not keys[pygame.K_e]:
                self.atirano=False         
            if keys[pygame.K_e] and not self.atirano:  
                shot=pygame.mixer.Sound("shot.mp3")
                somdetiro.play(shot)
                self.bulletgroup.add(self.create_bullet())
                self.atirano=True

    def gravityfunc(self):    
        self.direction.y+=self.gravity
        self.rect.y+=self.direction.y
        self.rect.y=self.rect.y

    def jump(self):
        self.direction.y=self.jumpspeed

    def update(self):
        self.falldamage()
        self.vivomorto()
        self.input()
        self.pegarstatus()
        self.animate()


class Bullet(pygame.sprite.Sprite):
    def __init__(self,posx,posy,bulletspeed):
        super().__init__()
        global bulletrect
        self.bulletspeed=bulletspeed
        self.image=pygame.image.load("bullet.png").convert_alpha()
        if self.bulletspeed<0:
            self.image=pygame.transform.flip(self.image,True,False)  
        self.image=pygame.transform.scale(self.image,(12,16))       
        self.rect=self.image.get_rect(center=(posx,posy))

    def collisionbullet(self,enemygroup):
        variavel=pygame.sprite.spritecollide(self,enemygroup,False)
        if variavel:
            for inimigo in variavel:
                inimigo.hit_points-=1
                self.kill()
    def update(self,enemygroup):
        self.collisionbullet(enemygroup)
        self.rect.x+= self.bulletspeed
        if self.rect.x>=1580 or self.rect.x<=-400:
            self.kill()

    #'''def bulletsprite(self):
        #bulletgroup=pygame.sprite.Group()
        #bulletspritevar=Bullet(posx,posy,bulletspeed)
       # bulletgroup.add(bulletspritevar)'''
