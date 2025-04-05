import pygame
import math
from .constants import RED, GREEN, BLACK, ENEMY_RADIUS

class Enemy:
    def __init__(self, path):
        self.path = path
        self.path_index = 0
        self.progress = 0  # Progress along current path segment (0-1)
        self.speed = 1.0
        self.health = 100
        self.max_health = 100
        self.position = path[0]
        self.radius = ENEMY_RADIUS
        self.reached_end = False
        self.value = 10
        self.color = RED
        
    def update(self):
        if self.reached_end or self.path_index >= len(self.path) - 1:
            self.reached_end = True
            return
        
        # Get current and next path points
        start = self.path[self.path_index]
        end = self.path[self.path_index + 1]
        
        # Calculate distance between points
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        distance = math.sqrt(dx**2 + dy**2)
        
        # Move along the path
        move_amount = self.speed / distance
        self.progress += move_amount
        
        if self.progress >= 1:
            # Move to next segment
            self.progress = 0
            self.path_index += 1
            if self.path_index >= len(self.path) - 1:
                self.reached_end = True
                return
        
        # Update position
        self.position = (
            start[0] + dx * self.progress,
            start[1] + dy * self.progress
        )
    
    def draw(self, surface):
        # Draw enemy sprite (colored circle for now)
        pygame.draw.circle(surface, self.color, (int(self.position[0]), int(self.position[1])), self.radius)
        
        # Draw enemy healthbar
        bar_width = 30
        health_percent = self.health / self.max_health
        pygame.draw.rect(surface, BLACK, 
                        (self.position[0] - bar_width//2, self.position[1] - self.radius - 10, 
                         bar_width, 5))
        pygame.draw.rect(surface, GREEN, 
                        (self.position[0] - bar_width//2, self.position[1] - self.radius - 10, 
                         int(bar_width * health_percent), 5))
    
    def take_damage(self, damage):
        self.health -= damage
        return self.health <= 0
