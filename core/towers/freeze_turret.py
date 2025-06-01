import pygame
from core.towers.turret import Turret
from core.towers.shop.shop_category import ShopUpgradeCategory
from core.constants import BLUE
from utils import vector2 as v2
from core.gameplay_configuration import FREEZE_TOWER_RANGE, FREEZE_DURATION, FREEZE_FIRE_RATE, FREEZE_MIN_ENEMIES_IN_RANGE

class FreezeTurret(Turret):
    def __init__(self, position, bullets, sound_manager):
        super().__init__(position, bullets, sound_manager)
        self.image = pygame.image.load("assets/towers/Idle/freeze.png").convert_alpha()
        self.range = FREEZE_TOWER_RANGE
        self.freeze_duration = FREEZE_DURATION * 1000
        self.last_shot_time = pygame.time.get_ticks()
        self.shootInterval = 1000 / FREEZE_FIRE_RATE
        self.frozen_enemies = {}
        self.minimum_enemies_in_range = FREEZE_MIN_ENEMIES_IN_RANGE

    upgradeCategory = ShopUpgradeCategory.FREEZE

    def update(self, enemies):
        current_time = pygame.time.get_ticks()

        # Unfreeze after duration
        to_unfreeze = [
            enemy for enemy, freeze_time in self.frozen_enemies.items()
            if current_time - freeze_time >= self.freeze_duration
        ]
        for enemy in to_unfreeze:
            enemy.can_move = True
            del self.frozen_enemies[enemy]

        # Check if enough time has passed
        if current_time - self.last_shot_time >= self.shootInterval:
            enemies_in_range = [
                enemy for enemy in enemies
                if v2.distance(enemy.position, self.pos) <= self.range and enemy not in self.frozen_enemies
            ]

            if len(enemies_in_range) >= self.minimum_enemies_in_range:
                self.freeze_enemies(enemies_in_range)
                self.last_shot_time = current_time

    def freeze_enemies(self, enemies_to_freeze):
        current_time = pygame.time.get_ticks()
        for enemy in enemies_to_freeze:
            enemy.can_move = False
            self.frozen_enemies[enemy] = current_time
    
    def draw_targeting_radius(self, surface):
        pygame.draw.circle(surface, BLUE, self.pos, self.range, 1)
