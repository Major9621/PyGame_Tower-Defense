import pygame
from core.towers.bullets.bullet import Bullet
from core.gameplay_configuration import PIERCING_BULLET_DESPAWN_TIME

class PiercingBullet(Bullet):
    def __init__(self, pos, dir, dmg, speed, color):
        super().__init__(pos, dir, dmg, speed, color)
        self.already_hit_enemies = set()

    despawn_time = PIERCING_BULLET_DESPAWN_TIME

    def on_hit(self, enemy):
        if enemy not in self.already_hit_enemies:
            self.already_hit_enemies.add(enemy)
            enemy.take_damage(self.damage)
        return True