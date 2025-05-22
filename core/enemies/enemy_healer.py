from core.enemies.enemy import Enemy
import pygame
from core.gameplay_configuration import ENEMY_HEALTH
from utils.direction import Direction

class HealerEnemy(Enemy):
    def __init__(self, path, gold_manager):
        super().__init__(path, gold_manager)
        self.health = ENEMY_HEALTH * 0.7
        self.max_health = self.health
        self.heal_range = 100
        self.heal_amount = 20
        self.heal_cooldown = 2000  # milliseconds
        self.last_heal = pygame.time.get_ticks()
        self.sprite_sheet = pygame.image.load("assets/enemies/Leafbug.png").convert_alpha()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_heal > self.heal_cooldown:
            # Heal nearby enemies
            for enemy in pygame.sprite.Group(self.groups()[0]).sprites():
                if enemy != self and not enemy.isDead():
                    distance = ((enemy.position[0] - self.position[0])**2 + 
                              (enemy.position[1] - self.position[1])**2)**0.5
                    if distance <= self.heal_range:
                        enemy.health = min(enemy.health + self.heal_amount, enemy.max_health)
            self.last_heal = current_time
        super().update()

    def draw(self, surface):
        super().draw(surface)
        if pygame.time.get_ticks() - self.last_heal < 500:  # Show heal effect for 500ms
            pygame.draw.circle(surface, (0, 255, 0), self.position, self.heal_range, 1)
