import pygame
from core.gameplay_configuration import BETTER_TWIN_TOWER_DAMAGE, BETTER_TWIN_TOWER_RANGE, BETTER_TWIN_TOWER_FIRE_RATE, BULLET_SPEED
from core.towers.twin_turret import TwinTurret
from core.constants import BLUE, DARKGREEN
from utils import vector2 as v2
from core.towers.shop.shop_category import ShopUpgradeCategory

class BetterTwinTurret(TwinTurret):
    def __init__(self, position, bullets, sound_manager):
        super().__init__(position, bullets, sound_manager)
        self.bullet_color = BLUE
        self.image = pygame.image.load("assets/towers/Idle/better_twin.png").convert_alpha()
        self.fire_side = 0  # 0 for left, 1 for right
        self.range = BETTER_TWIN_TOWER_RANGE

    bulletDamage = BETTER_TWIN_TOWER_DAMAGE
    bulletSpeed = BULLET_SPEED
    shotsPerSecond = BETTER_TWIN_TOWER_FIRE_RATE
    shootInterval = 1000 / shotsPerSecond
    upgradeCategory = ShopUpgradeCategory.NONE
    

    def draw_targeting_radius(self, surface):
        pygame.draw.circle(surface, DARKGREEN, self.pos, self.range, 1)