import pygame
pygame.init()

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load("enemysprite.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(74.4,98.4))
        self.image = pygame.transform.flip(self.image, False, False)
        self.rect= self.image.get_rect(topleft = (x,y-34))
        self.speed=7
        self.hit_points=10
        self.invincible=False
        self.damageCD=400

    def move(self):
        self.rect.x += self.speed

    def reverse(self):
        self.image = pygame.transform.flip(self.image, True, False)
        self.speed *= -1

    def checkDeath(self):
        if self.hit_points <= 0:
            self.kill()
            self.remove()

    def takeDamage(self):
        if not self.invincible:
            self.hit_points -= 1
            self.hurt_time = pygame.time.get_ticks()
            self.invincible = True

    def invincibleCD(self):
        if self.invincible:
            current_time = pygame.time.get_ticks()
            if current_time - self.hurt_time >= self.damageCD:
                self.invincible = False

    def update(self,shift):
        self.move()
        self.rect.x+=shift
        self.checkDeath()
        self.invincibleCD()
#enemyvar=pygame.sprite.Group()