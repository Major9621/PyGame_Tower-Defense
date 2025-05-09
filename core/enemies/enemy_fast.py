from core.enemies.enemy import Enemy
import pygame
from utils.direction import Direction

class FastEnemy(Enemy):
    def __init__(self, path, gold_manger):
        super().__init__(path, gold_manger)
        self.speed = 2.0
        self.health = 50
        self.max_health = 50
        self.flip = True
        self.sprite_sheet = pygame.image.load("assets/enemies/Scorpion.png").convert_alpha()

        self.frames = {
            "walk": {
                Direction.DOWN: self.load_frames(row=3, count=8),
                Direction.UP: self.load_frames(row=4, count=8),
                Direction.LEFT: self.load_frames(row=5, count=8),
                Direction.RIGHT: self.load_frames(row=5, count=8),
            },
            "die": {
                Direction.DOWN: self.load_frames(row=6, count=8),
                Direction.UP: self.load_frames(row=7, count=8),
                Direction.LEFT: self.load_frames(row=8, count=8),
                Direction.RIGHT: self.load_frames(row=8, count=8),
            }
        }
