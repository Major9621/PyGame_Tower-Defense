from core.enemies.enemy import Enemy
import pygame
from core.gameplay_configuration import ENEMY_HEALTH
from utils.direction import Direction

class ShieldedEnemy(Enemy):
    def __init__(self, path, gold_manager):
        super().__init__(path, gold_manager)
        self.health = ENEMY_HEALTH * 2
        self.max_health = self.health
        self.shield_active = True
        self.shield_health = ENEMY_HEALTH
        self.sprite_sheet = pygame.image.load("assets/enemies/Shield.png").convert_alpha()
        self.flip = True
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

    def take_damage(self, damage):
        if self.shield_active:
            self.shield_health -= damage
            if self.shield_health <= 0:
                self.shield_active = False
        else:
            super().take_damage(damage)

    def draw(self, surface):
        super().draw(surface)
        if self.shield_active:
            pygame.draw.circle(surface, (0, 150, 255), self.position, self.rect.width//2 + 2, 2)
