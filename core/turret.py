import pygame
from .constants import BLUE, YELLOW
from .bullet import Bullet
from .enemy import Enemy
from . import vector2 as v2

class Turret:
    def __init__(self, pos, bullets):
        self.pos = pos
        self.lastShotTime = pygame.time.get_ticks()
        self.range = 150
        self.hp = 100
        self.currentEnemy = None
        self.bullets = bullets
    
    bulletDamage = 10
    bulletSpeed = 10
    shotsPerSecond = 3
    shootInterval = 1000 / shotsPerSecond
    
    
    def update(self, enemies):
        currentTime = pygame.time.get_ticks()
        
        
        #If is able to shoot
        if currentTime - self.lastShotTime >= self.shootInterval: 
            
            #Looking for new (closest) enemy
            if self.currentEnemy == None or (self.currentEnemy != None and self.currentEnemy.isDead()):
                closestEnemy = None
                for en in enemies:
                    en: Enemy
                    if(v2.distance(en.position, self.pos) <= self.range):
                        if closestEnemy != None:
                            if v2.distance(closestEnemy.position, self.pos) > v2.distance(en.position, self.pos):
                                closestEnemy = en
                        else:
                            closestEnemy = en
                    
                self.currentEnemy = closestEnemy
                
            #If has enemy or just found it calculate shoot direction
            if self.currentEnemy != None:
                directionToEnemy = v2.normalized(v2.subtract(self.currentEnemy.position, self.pos))
                distanceToEnemy = v2.distance(self.currentEnemy.position, self.pos)
                
                if self.currentEnemy.reached_end or distanceToEnemy > self.range:
                    self.currentEnemy = None
                
                #Shoot!
                bullet = Bullet(self.pos, directionToEnemy, self.bulletDamage, self.bulletSpeed, YELLOW)
                self.bullets.add(bullet)
                
                self.lastShotTime = currentTime
            else:
                directionToEnemy = None
                distanceToEnemy = None
            
            

    
    def draw(self, surface):
        size = 35
        rect = pygame.Rect(self.pos[0] - size//2, self.pos[1] - size//2, size, size)
        pygame.draw.rect(surface, BLUE, rect)
        pygame.draw.circle(surface, BLUE, self.pos, self.range, 1)

