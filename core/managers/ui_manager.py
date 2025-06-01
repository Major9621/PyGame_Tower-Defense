import pygame
from core.constants import BLACK, GREEN, YELLOW, WHITE
from core.towers.shop.turret_shop import TurretShop

class UI_Manager:
    def __init__(self, screen, healthBarPosition, health_default_value, gold_default_value, turret_shop : TurretShop):
        self.screen = screen
        self.health_bar_position = healthBarPosition
        self.health_amount_text_position = (self.health_bar_position[0], self.health_bar_position[1] - 20)
        self.wave_number_text_position = (self.health_bar_position[0] + 300, self.health_bar_position[1] - 50)
        self.smaller_font = pygame.font.SysFont("Arial-Bold", 30)
        self.bigger_font = pygame.font.SysFont("Arial-Bold", 50)
        self.healthBarWidth = 300 
        self.gold_amount = gold_default_value
        self.radius = 50
        self.wave_number = 0
        self.healthBarValue = health_default_value
        self.shop_position = (self.health_bar_position[0] - 400, self.health_bar_position[1] + 330)
        self.turret_shop = turret_shop
        self.turret_shop.pos = self.shop_position
    
    
    def draw_shop(self):
        # Draw the shop background
        pygame.draw.rect(self.screen, WHITE, (self.shop_position[0], self.shop_position[1], 300, 80))
        
        # Draw the shop title
        title_text = self.smaller_font.render("Turret Shop", True, YELLOW)
        title_rect = title_text.get_rect(center=(self.shop_position[0] + 150, self.shop_position[1] - 10))
        self.screen.blit(title_text, title_rect)
        
        # Draw the shop items
        self.turret_shop.draw_shop_menu(self.screen)
        
        
    
    def draw_health_bar(self):
        health_percent = self.healthBarValue
        pygame.draw.rect(self.screen, BLACK, 
                        (self.health_bar_position[0] - self.healthBarWidth//2, self.health_bar_position[1] - self.radius - 10, 
                        self.healthBarWidth, 5))
        pygame.draw.rect(self.screen, GREEN, 
                        (self.health_bar_position[0] - self.healthBarWidth//2, self.health_bar_position[1] - self.radius - 10, 
                        int(self.healthBarWidth * health_percent), 5))
    
    def draw_text(self):
        #Health amount
        text = f"Health: {int(self.healthBarValue * 100)}%"
        text_surface = self.smaller_font.render(text, True, GREEN)
        
        text_rect = text_surface.get_rect(center=self.health_amount_text_position)
        self.screen.blit(text_surface, text_rect)
        
        
        #Wave info
        text = f"Wave: {self.wave_number}"
        text_surface = self.bigger_font.render(text, True, BLACK)
        
        text_rect = text_surface.get_rect(center=self.wave_number_text_position)
        self.screen.blit(text_surface, text_rect)
        
        
        #Gold
        text = f"Gold: {self.gold_amount}"
        text_surface = self.smaller_font.render(text, True, YELLOW)
        text_rect = text_surface.get_rect(center=(self.health_bar_position[0] - 350, self.health_bar_position[1] - 60))
        self.screen.blit(text_surface, text_rect)
    
    def update_health_bar_and_text(self, value):
        self.healthBarValue = value
        
    def update_wave_number(self, wave_number):
        self.wave_number = wave_number
    
    def update_gold_amount(self, gold_amount):
        self.gold_amount = gold_amount