import pygame
from core.towers.bullets.bullet import Bullet
from utils import vector2 as v2
from core.gameplay_configuration import BOMBER_EXPLOSION_RADIUS

class BomberBullet(Bullet):
    def __init__(self, pos, dir, dmg, speed, color, enemies):
        super().__init__(pos, dir, dmg, speed, color)
        self.enemies = enemies  # list of enemies to check for explosion
        self.image

    def on_hit(self, enemy_hit):
        for enemy in self.enemies:
            if v2.distance(enemy.position, self.pos) <= BOMBER_EXPLOSION_RADIUS:
                enemy.take_damage(self.damage)
        
        self.kill()
        return False  
