import pygame
from core.gameplay_configuration import SNIPER_TOWER_DAMAGE, SNIPER_TOWER_RANGE, SNIPER_TOWER_FIRE_RATE, SNIPER_TOWER_BULLET_SPEED
from core.towers.bullets.bullet import Bullet
from core.enemies.enemy import Enemy
from utils import vector2 as v2
from core.constants import RED, ORANGE, YELLOW
from core.towers.turret import Turret
from core.towers.shop.shop_category import ShopUpgradeCategory

class SniperTurret(Turret):
    def __init__(self, position, bullets, sound_manager):
        super().__init__(position, bullets, sound_manager)
        self.image = pygame.image.load("assets/towers/Idle/sniper.png").convert_alpha()
        self.bullet_color = RED
        self.range = SNIPER_TOWER_RANGE
        self.radius_color = YELLOW

    bulletDamage = SNIPER_TOWER_DAMAGE
    bulletSpeed = SNIPER_TOWER_BULLET_SPEED
    shotsPerSecond = SNIPER_TOWER_FIRE_RATE
    shootInterval = 1000 / shotsPerSecond
    upgradeCategory = ShopUpgradeCategory.SNIPER
    
        
    def look_for_enemies(self, enemies):
        if self.current_enemy == None or (self.current_enemy != None and self.current_enemy.isDead()):
                max_hp_enemy = None
                for en in enemies:
                    en: Enemy
                    if(v2.distance(en.position, self.pos) <= self.range):
                        if max_hp_enemy != None:
                            if max_hp_enemy.health < max_hp_enemy.health:
                                max_hp_enemy = en
                        else:
                            max_hp_enemy = en
                    
                self.current_enemy = max_hp_enemy
    

    def draw_targeting_radius(self, surface):
        pygame.draw.circle(surface, YELLOW, self.pos, self.range, 1)