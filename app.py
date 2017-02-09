import pygame
from pygame.locals import *
from sys import exit
import random
import time
import math

pygame.init()
screenWidth = 400
screenHeight = 600
screenSize = (screenWidth, screenHeight)
screen = pygame.display.set_mode(screenSize, 0, 32)
clock = pygame.time.Clock()
TURQOISE = (46, 64, 83)
# player = pygame.image.load('./assets/player.png').convert_alpha()
# playerWidth = player.get_width()
# playerHeight = player.get_height()
# playerX = 0.5 * screenWidth - 0.5 * playerWidth
# playerY = screenHeight - playerHeight - 20
currentLevel = 1
previousTime = 0
enemies = []
enemySpritesList = pygame.sprite.Group()
pixelGroup = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    # player = pygame.image.load('./assets/player.png').convert_alpha()
    # playerWidth = player.get_width()
    # playerHeight = player.get_height()
    # playerWidth = 40
    # playerHeight = 48
    # playerX = 0.5 * screenWidth - 0.5 * playerWidth
    # playerY = screenHeight - playerHeight - 20

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./assets/player.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.playerWidth = self.image.get_width()
        self.playerHeight = self.image.get_height()
        self.rect.x = 0.5 * screenWidth - 0.5 * self.playerWidth
        self.rect.y = screenHeight - self.playerHeight - 20
            

player = Player()
playerGroup = pygame.sprite.Group()
playerGroup.add(player)        

class Enemy(pygame.sprite.Sprite):
    countCurrent = 0
    countMax = 5
    # enemyTemplate = pygame.image.load('./assets/enemy1.png').convert_alpha()
    # enemyWidth = enemyTemplate.get_width()
    # enemyHeight = enemyTemplate.get_height()
    frame1 = pygame.image.load('./assets/enemy1.png').convert_alpha()
    frame2 = pygame.image.load('./assets/enemy2.png').convert_alpha()
    # animationCheckpoint = 0
    # animationCounter = 0

    def __init__(self):
        super().__init__()
        self.life = 5
        # self.frame1 = pygame.image.load('./assets/enemy1.png').convert_alpha()
        # self.frame2 = pygame.image.load('./assets/enemy2.png').convert_alpha()
        self.animationCheckpoint = 0
        self.animationCounter = 0
        self.image = Enemy.frame1
        self.rect = self.image.get_rect()
        self.enemyWidth = self.image.get_width()
        self.enemyHeight = self.image.get_height()
        self.x = random.randint(self.enemyWidth, screenWidth) - self.enemyWidth
        self.y = 0 - self.enemyHeight
        enemySpritesList.add(self)

    
    def spawn(self):
        if Enemy.countCurrent < Enemy.countMax:
            self.rect.x = self.x
            self.rect.y = self.y
            # screen.blit(Enemy.enemyTemplate, (self.x, self.y))
            Enemy.countCurrent += 1         

    def update(self):
        if ((time.time() - self.animationCheckpoint) > 0.5):
            if (self.animationCounter / 2):
                self.image = Enemy.frame2
                self.animationCounter += 1
            else:
                self.image = Enemy.frame1
                self.animationCounter -= 1

            self.animationCheckpoint = time.time()

    def fall(self):
        # self.y += 1
        # screen.blit(Enemy.enemyTemplate, (self.x, self.y))
        self.rect.x = self.x
        self.rect.y += 1
        # if ((time.time() - Enemy.animationCheckpoint) > 0.5):
        #     if (Enemy.animationCounter / 2):
        #         self.image = pygame.image.load('./assets/enemy2.png').convert_alpha()
        #         Enemy.animationCounter += 1
        #         print('2')
        #     else:
        #         self.image = pygame.image.load('./assets/enemy1.png').convert_alpha()
        #         Enemy.animationCounter -= 1
        #         print('1')

        #     Enemy.animationCheckpoint = time.time()
        
        if self.rect.y > screenHeight:
            self.dead()
    
    # def deathAnimation(self, posX, posY):
        
            
            
            

    def dead(self):
        if Enemy.countCurrent != 0:
            Enemy.countCurrent -= 1
            # enemies.remove(self)
            # enemySpritesList.remove(self)




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pressed = pygame.key.get_pressed()

    if pressed[K_LEFT]:
        if player.rect.x > 0:
            player.rect.x -= 3.5
        else:
            player.rect.x = 0

    if pressed[K_RIGHT]:
        if (player.rect.x < (screenWidth - player.playerWidth)): 
            player.rect.x += 3.5
        else:
            player.rect.x = screenWidth - player.playerWidth

    # Spawning enemies on level 1
    if ((time.time() - previousTime) > 3) and (currentLevel == 1):
        previousTime = time.time()
        if Enemy.countCurrent < Enemy.countMax:
            enemy = Enemy()
            enemy.spawn()
            # enemies.append(enemy)
    
    for enemy in enemySpritesList.sprites():
        enemy.fall()
        # screen.blit(enemy.image, (enemy.rect.x, enemy.rect.y)) 

        # if enemy.rect.x > screenHeight:
        #     enemy.dead() 
    
    collisionList = pygame.sprite.spritecollide(player, enemySpritesList, True)
    for sprite in collisionList:
        sprite.dead()
        
        
    enemySpritesList.update()    
    # player.rect.x = player.playerX
    # player.rect.y = Player.playerY 
    screen.fill(TURQOISE)
    playerGroup.draw(screen)
    enemySpritesList.draw(screen)
    # screen.blit(player, (player.rect.x, player.rect.y))
    clock.tick(60)
    pygame.display.update()