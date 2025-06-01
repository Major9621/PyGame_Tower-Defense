import pygame
from core.gameplay_configuration import TWIN_TOWER_COST, TWIN_TOWER_RANGE, TWIN_TOWER_DAMAGE, TWIN_TOWER_FIRE_RATE, BULLET_SPEED
from core.towers.turret import Turret
from core.towers.bullets.bullet import Bullet
from core.constants import BLUE
from utils import vector2 as v2
from core.towers.shop.shop_category import ShopUpgradeCategory

class TwinTurret(Turret):
    def __init__(self, position, bullets):
        super().__init__(position, bullets)
        self.bullet_color = BLUE
        self.image = pygame.image.load("assets/towers/Idle/twin.png").convert_alpha()
        self.fire_side = 0  # 0 for left, 1 for right

    bulletDamage = TWIN_TOWER_DAMAGE
    bulletSpeed = BULLET_SPEED
    shotsPerSecond = TWIN_TOWER_FIRE_RATE
    shootInterval = 1000 / shotsPerSecond
    upgradeCategory = ShopUpgradeCategory.TWIN
    
    def update(self, enemies):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_shot_time >= self.shootInterval:
            self.look_for_enemies(enemies)

            if self.current_enemy is not None:
                direction_to_enemy = self.predict_leading_direction(self.current_enemy)
                distance_to_enemy = v2.distance(self.current_enemy.position, self.pos)

                if self.current_enemy.reached_end or distance_to_enemy > self.range:
                    self.current_enemy = None
                    return

                # Bullet offset
                perpendicular = (-direction_to_enemy[1], direction_to_enemy[0])
                offset_amount = 10 

                if self.fire_side == 0:
                    fire_pos = (
                        self.pos[0] + perpendicular[0] * offset_amount,
                        self.pos[1] + perpendicular[1] * offset_amount
                    )
                    self.fire_side = 1
                else:
                    fire_pos = (
                        self.pos[0] - perpendicular[0] * offset_amount,
                        self.pos[1] - perpendicular[1] * offset_amount
                    )
                    self.fire_side = 0

                # Fire
                self.shoot(direction_to_enemy)

                self.last_shot_time = current_time