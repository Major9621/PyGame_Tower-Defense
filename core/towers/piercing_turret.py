import pygame
from core.gameplay_configuration import PIERCING_BULLET_SPEED, PIERCING_TOWER_DAMAGE, PIERCING_TOWER_FIRE_RATE, PIERCING_TOWER_RANGE
from core.towers.bullets.piercing_bullet import PiercingBullet
from core.enemies.enemy import Enemy
from utils import vector2 as v2
from core.constants import RED
from core.towers.turret import Turret
from core.towers.shop.shop_category import ShopUpgradeCategory

class PiercingTurret(Turret):
    def __init__(self, position, bullets):
        super().__init__(position, bullets)
        self.image = pygame.image.load("assets/towers/Idle/piercing.png").convert_alpha()
        self.bullet_color = RED
        self.range = PIERCING_TOWER_RANGE

    bullet_damage = PIERCING_TOWER_DAMAGE
    bullet_speed = PIERCING_BULLET_SPEED
    
    shotsPerSecond = PIERCING_TOWER_FIRE_RATE
    shootInterval = 1000 / shotsPerSecond
    upgradeCategory = ShopUpgradeCategory.NONE
    
    def look_for_enemies(self, enemies):
        if self.current_enemy is None or self.current_enemy.isDead():
            closest_enemy = None
            closest_distance = float('inf')

            for en in enemies:
                distance = v2.distance(en.position, self.pos)
                if distance <= self.range and not en.isDead():
                    if distance < closest_distance:
                        closest_distance = distance
                        closest_enemy = en

            self.current_enemy = closest_enemy

    
    def shoot(self, direction_to_enemy):
        bullet = PiercingBullet(self.pos, direction_to_enemy, self.bullet_damage, self.bullet_speed, self.bullet_color)
        self.bullets.add(bullet)