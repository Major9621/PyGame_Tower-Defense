import pygame
from core.gameplay_configuration import BOMBER_BULLET_SPEED, BOMBER_EXPLOSION_DAMAGE, BOMBER_TOWER_RANGE, BOMBER_TOWER_FIRE_RATE, BOMBER_EXPLOSION_RADIUS, BOMBER_TOWER_COST
from core.towers.bullets.bullet import Bullet
from core.enemies.enemy import Enemy
from utils import vector2 as v2
from core.constants import RED
from core.towers.turret import Turret
from core.towers.bullets.bomber_bullet import BomberBullet
from core.towers.shop.shop_category import ShopUpgradeCategory

class BomberTurret(Turret):
    def __init__(self, position, bullets):
        super().__init__(position, bullets)
        self.image = pygame.image.load("assets/towers/Idle/bomber.png").convert_alpha()
        self.bullet_color = RED
        self.range = BOMBER_TOWER_RANGE

    bulletDamage = BOMBER_EXPLOSION_DAMAGE
    bulletSpeed = BOMBER_BULLET_SPEED
    shotsPerSecond = BOMBER_TOWER_FIRE_RATE
    shootInterval = 1000 / shotsPerSecond
    upgradeCategory = ShopUpgradeCategory.NONE
    
    
    def shoot(self, direction_to_enemy, enemies):
        bullet = BomberBullet(self.pos, direction_to_enemy, self.bulletDamage, self.bullet_speed, self.bullet_color, enemies)
        self.bullets.add(bullet)
    
    
    def update(self, enemies):
        current_time = pygame.time.get_ticks()
        
        
        #If is able to shoot
        if current_time - self.last_shot_time >= self.shootInterval: 
            
            #Looking for new enemy
            self.look_for_enemies(enemies)
                
            #If has enemy or just found it calculate shoot direction
            if self.current_enemy != None:
                direction_to_enemy = direction_to_enemy = self.predict_leading_direction(self.current_enemy)
                distance_to_enemy = v2.distance(self.current_enemy.position, self.pos)
                
                if self.current_enemy.reached_end or distance_to_enemy > self.range:
                    self.current_enemy = None
                
                #Shoot!
                self.shoot(direction_to_enemy, enemies)
                
                self.last_shot_time = current_time
            else:
                direction_to_enemy = None
                distance_to_enemy = None
        
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
    