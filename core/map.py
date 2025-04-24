import pygame
import math
from .constants import GRAY, RED, PATH_WIDTH, BROWN

class Map:
    def __init__(self, path):
        self.path = path
        self.path_width = PATH_WIDTH
        
    def draw(self, surface):
        for i in range(len(self.path) - 1):
            start = self.path[i]
            end = self.path[i + 1]

            dx = end[0] - start[0]
            dy = end[1] - start[1]


            if dx == 0:
                rect = pygame.Rect(
                    start[0] - self.path_width // 2, 
                    min(start[1], end[1]), 
                    self.path_width, 
                    abs(dy)
                )
                pygame.draw.rect(surface, BROWN, rect)

            elif dy == 0:
                rect = pygame.Rect(
                    min(start[0], end[0]) - self.path_width // 2, 
                    start[1] - self.path_width // 2,
                    abs(dx) + self.path_width, 
                    self.path_width
                )
                pygame.draw.rect(surface, BROWN, rect)

            else:
                pygame.draw.line(surface, BROWN, start, end, self.path_width)
        
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
    