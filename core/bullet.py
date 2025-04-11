import pygame
from .constants import YELLOW

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, dir, dmg, speed):
        super().__init__()
        self.pos = pos
        self.dir = dir 
        self.damage = dmg
        self.speed = speed
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect(center=(pos[0], pos[1]))
        self.spawnTime = pygame.time.get_ticks()
        
    def update(self, bullets):
        self.pos = (self.pos[0] + (self.dir[0] * self.speed), self.pos[1] + (self.dir[1] * self.speed))
        self.rect.center = self.pos
        
        #Remove itself after 10 seconds
        if(pygame.time.get_ticks() - self.spawnTime >= 10000):
            bullets.remove(self)
    
    def draw(self, surface):
        pygame.draw.circle(surface, YELLOW, self.pos, 10)
    