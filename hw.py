import pygame
import time
import random
pygame.init()

screen = pygame.display.set_mode((1250,690))

bee = pygame.image.load("lesson 6/image/bee.png")
flower = pygame.image.load("lesson 6/image/flower.png")
bg = pygame.image.load("lesson 6/image/grass.png")
bg = pygame.transform.scale(bg,(1250,690))

beex = 625
beey = 345


font = pygame.font.SysFont("Times New Roman",36)

class Bee(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = bee
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def handel_movement(self,keys):  
      if keys[pygame.K_UP]:
           self.rect.y -= 2
      if keys[pygame.K_DOWN]:
           self.rect.y += 2
      if keys[pygame.K_LEFT]:
           self.rect.x -= 2
      if keys[pygame.K_RIGHT]:
           self.rect.x += 2

class Flower(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = flower
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

bee = Bee(beex,beey)
Bee = pygame.sprite.Group()
Bee.add(bee)

flower = Flower(1000,345)
Flower = pygame.sprite.Group()
Flower.add(flower)

while beey<600:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if bee.rect.colliderect(flower.rect):
      flower.rect.x = random.randint(50,1200)
      flower.rect.y = random.randint(50,640)

         
    screen.fill("black")
    screen.blit(bg,(0,0))
    Bee.draw(screen)
    Flower.draw(screen)
    keys = pygame.key.get_pressed()
    bee.handel_movement(keys)
    pygame.display.update()