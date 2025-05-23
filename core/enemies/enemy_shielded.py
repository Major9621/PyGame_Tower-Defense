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
        self.flip_sprite = True

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
