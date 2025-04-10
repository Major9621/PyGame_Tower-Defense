import pygame
import math
from .constants import GRAY, RED, PATH_WIDTH

class Map:
    def __init__(self):
        self.path = [
            (0, 300),
            (200, 300),
            (200, 150),
            (400, 150),
            (400, 450),
            (600, 450),
            (600, 300),
            (800, 300)
        ]
        self.path_width = PATH_WIDTH
        
    def draw(self, surface):
        for i in range(len(self.path) - 1):
            start = self.path[i]
            end = self.path[i + 1]
            
            if start[0] == end[0]:
                rect = pygame.Rect(
                    start[0] - self.path_width // 2, 
                    min(start[1], end[1]), 
                    self.path_width, 
                    abs(end[1] - start[1])
                )
            else:
                rect = pygame.Rect(
                    min(start[0], end[0]) - self.path_width // 2, 
                    start[1] - self.path_width // 2,
                    abs(end[0] - start[0]) + self.path_width, 
                    self.path_width
                )
            
            pygame.draw.rect(surface, GRAY, rect)
        
        # Draw path points (for debugging)
        for point in self.path:
            pygame.draw.circle(surface, RED, point, 5)
    
    def get_path_length(self):
        length = 0
        for i in range(len(self.path) - 1):
            x1, y1 = self.path[i]
            x2, y2 = self.path[i + 1]
            length += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return length
    