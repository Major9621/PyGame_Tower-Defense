import pygame
from .constants import BLACK, GREEN

class Player:
    def __init__(self, maxHP, healthBarPosition):
        self.max_health = maxHP
        self.position = healthBarPosition
        self.health = self.max_health
        self.radius = 50
        self.is_alive = True

    def take_damage(self, amount):
        if self.is_alive:
            self.health -= amount
            if self.health <= 0:
                self.health = 0
                self.is_alive = False
                print("Player dead!")
                
    def is_dead(self):
        return self.health == 0

    def heal(self, amount):
        if self.is_alive:
            self.health += amount
            if self.health > self.max_health:
                self.health = self.max_health
    
    
    def draw_health_bar(self, screen):
        bar_width = 300
        health_percent = self.health / self.max_health
        pygame.draw.rect(screen, BLACK, 
                        (self.position[0] - bar_width//2, self.position[1] - self.radius - 10, 
                        bar_width, 5))
        pygame.draw.rect(screen, GREEN, 
                        (self.position[0] - bar_width//2, self.position[1] - self.radius - 10, 
                         int(bar_width * health_percent), 5))