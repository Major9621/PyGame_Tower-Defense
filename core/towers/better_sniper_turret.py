import pygame
from core.gameplay_configuration import BETTER_SNIPER_TOWER_DAMAGE, BETTER_SNIPER_TOWER_RANGE, BETTER_SNIPER_TOWER_FIRE_RATE, BETTER_SNIPER_TURRET_BULLET_SPEED
from core.towers.bullets.bullet import Bullet
from core.constants import RED, ORANGE
from core.towers.sniper_turret import SniperTurret
from core.towers.shop.shop_category import ShopUpgradeCategory
from utils import vector2 as v2
from core.enemies.enemy import Enemy

class BetterSniperTurret(SniperTurret):
    def __init__(self, position, bullets, sound_manager):
        super().__init__(position, bullets, sound_manager)
        self.image = pygame.image.load("assets/towers/Idle/better_sniper.png").convert_alpha()
        self.bullet_color = RED
        self.range = BETTER_SNIPER_TOWER_RANGE
    
    bulletDamage = BETTER_SNIPER_TOWER_DAMAGE
    bulletSpeed = BETTER_SNIPER_TURRET_BULLET_SPEED
    shotsPerSecond = BETTER_SNIPER_TOWER_FIRE_RATE
    shootInterval = 1000 / shotsPerSecond
    upgradeCategory = ShopUpgradeCategory.SNIPER
    
    def draw_targeting_radius(self, surface):
        pygame.draw.circle(surface, ORANGE, self.pos, self.range, 1)
