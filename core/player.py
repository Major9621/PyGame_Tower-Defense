import pygame
from .constants import BLACK, GREEN

class Player:
    def __init__(self, maxHP, ui_manager):
        self.ui_manager = ui_manager
        self.max_health = maxHP
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
            
            self.ui_manager.update_health_bar_and_text(self.health / self.max_health)
                
    def is_dead(self):
        return self.health == 0

    def heal(self, amount):
        if self.is_alive:
            self.health += amount
            if self.health > self.max_health:
                self.health = self.max_health
            
            self.ui_manager.update_health_bar(self.health / self.max_health)
    
    
