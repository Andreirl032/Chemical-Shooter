import pygame
from tiles import *
from configsnivel import tamanho_tile
from player import Player
from enemy import Enemy

class Level():
    def __init__(self,level_data,surface):
        #setup do nivel
        self.display_surface=surface
        self.setuplevel(level_data)
        self.world_shift=0 
        self.world_shift_y=0

        self.imagemvida=pygame.image.load("vida.png").convert_alpha()
        self.imagemvida=pygame.transform.scale(self.imagemvida,(115.5,35))
        self.imagemvidarect=self.imagemvida.get_rect()
        self.imagemvidarect.topleft=30,15

        self.outlinevida=pygame.image.load("empty-lifebar.png").convert_alpha()
        self.outlinevida=pygame.transform.scale(self.outlinevida,(144,30))
        self.outlinevidarect=self.outlinevida.get_rect()
        self.outlinevidarect.topleft=20,55

        self.barravida=None #pygame.Surface((140,26))
        #self.barravida.fill((0,255,0))
        self.barravidarect=None #self.barravida.get_rect()
        #self.barravidarect.topleft=22,57

    def diminuir_barravida(self,x,y):
        self.barravida=pygame.Surface((x,y))
        self.barravida.fill((0,255,0))
        self.barravidarect=self.barravida.get_rect()
        self.barravidarect.topleft=22,57


    def setuplevel(self, layout):
        self.tiles=pygame.sprite.Group()
        self.tiles2=pygame.sprite.Group()
        self.player=pygame.sprite.GroupSingle()
        self.enemy=pygame.sprite.Group()
        self.test=pygame.sprite.Group()
        self.bandeira=pygame.sprite.Group()
        self.tiobaca=pygame.sprite.Group()
        #self.bullett=pygame.sprite.Group()
        for fileira_index,fileira in enumerate(layout):
            for coluna_index,coluna in enumerate(fileira):
                x=coluna_index*tamanho_tile
                y=fileira_index*tamanho_tile
                if coluna=='X':
                    tile=Tile((x,y),tamanho_tile)
                    self.tiles.add(tile)
                if coluna=='P':
                    player_sprite=Player((x,y))
                    self.player.add(player_sprite)
                if coluna=='I':
                    teste=Tiletest((x,y),tamanho_tile)
                    self.tiles2.add(teste)
                if coluna=='R':
                    tile2=Tilered((x,y),tamanho_tile)
                    self.tiles.add(tile2)
                if coluna=='E':
                    enemy2=Enemy(x,y)
                    self.enemy.add(enemy2)
                if coluna=='B':
                    tile3=Tilewin((x,y),tamanho_tile)
                    self.tiles.add(tile3)
                if coluna=='T':
                    tile4=Tiobaca(x,y,tamanho_tile)
                    self.tiobaca.add(tile4)
                if coluna=='Q':
                    tile5=Bacatext(x,y,tamanho_tile)
                    self.tiobaca.add(tile5)

    def enemy_collision_reverse(self):
        for enemy in self.enemy.sprites():
            if pygame.sprite.spritecollide(enemy, self.tiles2, False):
                enemy.reverse()
            #if pygame.sprite.spritecollide(enemy, bulletgroup,False):
                #bulletgroup.remove()
                #bulletgroup.kill()

    def playerlife(self):
        for coisa in self.player.sprites():
            if pygame.sprite.spritecollide(coisa, self.enemy, False):
                coisa.takeDamage()
                coisa.invincibleCD()
            vidajogador=coisa.lifebar()
        self.diminuir_barravida(140*vidajogador,26)

    def scroll_x(self):
        player=self.player.sprite
        playerx=player.rect.centerx
        directionx=player.direction.x  
        if playerx<640 and directionx<0:
            self.world_shift=8
            player.speed=0
        elif playerx>640 and directionx>0:   
            self.world_shift=-8
            player.speed=0
        else:
            self.world_shift=0
            player.speed=4
    '''def scroll_y(self):
        player=self.player.sprite
        playery=player.rect.centery
        directiony=player.direction.y 
        if playery<360 and directiony<0:
            self.world_shift_y=8
            player.speedy=0
        elif playery>360 and directiony>0:   
            self.world_shift_y=-8
            player.speedy=1
        else:
            self.world_shift_y=0
            player.speedy=1'''        
            
    '''def colisaobullet(self):
        bala=False
        for balas in bulletgroup.sprites():
            bala=balas
        if bala:
            colisaoentresprites=pygame.sprite.spritecollide(bala,self.tiles,False)
            if colisaoentresprites:
                bala.kill()'''

    def colisao_mov_horizontal(self):
        player=self.player.sprite
        player.rect.x+=player.direction.x*player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x<0:
                    player.rect.left=sprite.rect.right
                    player.direction.x=0
                elif player.direction.x>0:   
                    player.rect.right=sprite.rect.left
                    player.direction.x=0
        for sprite in self.tiles2.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x<0:
                    player.rect.left=sprite.rect.right
                    player.direction.x=0
                elif player.direction.x>0:   
                    player.rect.right=sprite.rect.left
                    player.direction.x=0

    def colisao_mov_vertical(self):
        player=self.player.sprite
        player.gravityfunc()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y<0:
                    player.rect.top=sprite.rect.bottom
                    player.direction.y=0 
                elif player.direction.y>0:
                    player.jumpstate=False
                    player.rect.bottom=sprite.rect.top
                    player.direction.y=0 
        for sprite in self.tiles2.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y<0:
                    player.rect.top=sprite.rect.bottom
                    player.direction.y=0 
                elif player.direction.y>0:
                    player.jumpstate=False
                    player.rect.bottom=sprite.rect.top
                    player.direction.y=0             
        '''if player.jumpstate==True and player.direction.y>0:
            player.jumpstate=False       '''   


    def run(self):
        #nivel
      self.tiles2.update(self.world_shift)
      self.tiles2.update(self.world_shift_y)
      self.tiles2.draw(self.display_surface)

      self.tiobaca.update(self.world_shift)
      self.tiobaca.update(self.world_shift_y)
      self.tiobaca.draw(self.display_surface)

      self.tiles.update(self.world_shift)
      self.tiles.draw(self.display_surface)  
      self.scroll_x()
      #self.scroll_y()

      self.enemy.update(self.world_shift)
      self.enemy_collision_reverse()
      self.enemy.draw(self.display_surface)

      self.playerlife()

      self.display_surface.blit(self.imagemvida,self.imagemvidarect)
      self.display_surface.blit(self.outlinevida,self.outlinevidarect)
      self.display_surface.blit(self.barravida,self.barravidarect)

        #jogador
      self.player.update()
      self.colisao_mov_horizontal() 
      self.colisao_mov_vertical()
      self.player.draw(self.display_surface)
      #self.colisaobullet()

      self.player.sprite.bulletgroup.update(self.enemy)
      