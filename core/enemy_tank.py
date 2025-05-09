from core.enemy import Enemy
from pygame import Color
import pygame
from .direction import Direction

class TankEnemy(Enemy):
    def __init__(self, path):
        super().__init__(path)
        self.speed = 0.5
        self.health = 300
        self.max_health = 300
        self.flip = True
        self.sprite_sheet =  pygame.image.load("assets/enemies/Magmacrab.png").convert_alpha()
        self.frame_width = self.sprite_sheet.get_width() // 10
        self.frame_height = self.sprite_sheet.get_height() // 9

        self.frames = {
            "walk": {
                Direction.DOWN: self.load_frames(row=3, count=8),
                Direction.UP: self.load_frames(row=4, count=8),
                Direction.LEFT: self.load_frames(row=5, count=8),
                Direction.RIGHT: self.load_frames(row=5, count=8),
            },
            "die": {
                Direction.DOWN: self.load_frames(row=6, count=10),
                Direction.UP: self.load_frames(row=7, count=10),
                Direction.LEFT: self.load_frames(row=8, count=10),
                Direction.RIGHT: self.load_frames(row=8, count=10),
            }
        }