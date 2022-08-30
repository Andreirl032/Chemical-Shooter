import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image=pygame.image.load("testblock.png").convert()
        self.rect=self.image.get_rect(topleft=position)
    def update(self,trocar_x):
        self.rect.x+=trocar_x

class Tilered(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image=pygame.image.load("testblock2.png").convert()
        self.rect=self.image.get_rect(topleft=position)
    def update(self,trocar_x):
        self.rect.x+=trocar_x  
        

class Tiletest(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image=pygame.image.load("blokito.png").convert()
        self.rect=self.image.get_rect(topleft=position)
    def update(self,trocar_x):
        self.rect.x+=trocar_x

class Tilewin(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image=pygame.image.load("bandeira.png").convert_alpha()
        self.rect=self.image.get_rect(topleft=position)
    def update(self,trocar_x):
        self.rect.x+=trocar_x
        
class Tiobaca(pygame.sprite.Sprite):
    def __init__(self, x,y, size):
        super().__init__()
        self.image=pygame.image.load("tio-baca.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(90,128))
        self.image=pygame.transform.flip(self.image,True,False)
        self.rect=self.image.get_rect(topleft=(x,y-64))
    def update(self,trocar_x):
        self.rect.x+=trocar_x     
class Bacatext(pygame.sprite.Sprite):
    def __init__(self, x,y, size):
        super().__init__()
        self.image=pygame.image.load("tiobacaimg.png").convert_alpha()
        self.rect=self.image.get_rect(topleft=(x+20,y))
    def update(self,trocar_x):
        self.rect.x+=trocar_x             
'''class Enemytile(pygame.sprite.Sprite):
    def __init__(self, positionx,positiony, size):
        super().__init__()
        self.image=pygame.image.load("enemysprite.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(79.2,98.4))
        self.rect=self.image.get_rect()
        self.rect.topleft=positionx,positiony-34
    def update(self,trocar_x):
        self.rect.x+=trocar_x   '''             