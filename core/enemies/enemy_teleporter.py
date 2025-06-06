from .enemy import Enemy
import pygame
import random
from core.gameplay_configuration import ENEMY_HEALTH, ENEMY_SPEED, ENEMY_DAMAGE
from utils.direction import Direction

class TeleporterEnemy(Enemy):
    def __init__(self, path, gold_manager, hp_multiplier):
        super().__init__(path, gold_manager, hp_multiplier)
        self.health = ENEMY_HEALTH * 0.8 * hp_multiplier
        self.max_health = self.health
        self.teleport_cooldown = 3000
        self.stun_duration = 1000
        self.last_teleport = pygame.time.get_ticks()
        self.is_stunned = False
        self.original_speed = ENEMY_SPEED * 0.8
        self.cooldown_progress = 0
        self.sprite_sheet = pygame.image.load("assets/enemies/Teleporter.png").convert_alpha()
        self.flip = True

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

    def update(self):
        current_time = pygame.time.get_ticks()
        
        if self.is_stunned:
            self.speed = 0
            if current_time - self.last_teleport > self.stun_duration:
                self.is_stunned = False
                self.speed = self.original_speed
        else:
            self.cooldown_progress = current_time - self.last_teleport
        
        if not self.is_stunned and self.cooldown_progress > self.teleport_cooldown:
            self.path_index = min(self.path_index + 2, len(self.path) - 1)
            self.last_teleport = current_time
            self.cooldown_progress = 0
            self.is_stunned = True
            self.speed = 0
        
        super().update()


