import pygame
import math
from core.constants import BLUE, YELLOW, TILE_SIZE, GRAY, WHITE
from core.gameplay_configuration import TOWER_RANGE, TOWER_DAMAGE, TOWER_FIRE_RATE, BULLET_SPEED
from core.towers.bullets.bullet import Bullet
from core.enemies.enemy import Enemy
from utils import vector2 as v2
from core.towers.shop.shop_category import ShopUpgradeCategory

class Turret:
    def __init__(self, pos, bullets, sound_manager):
        self.pos = self.snap_to_grid(pos)
        self.last_shot_time = pygame.time.get_ticks()
        self.range = TOWER_RANGE
        self.current_enemy = None
        self.bullets = bullets
        self.bullet_color = YELLOW
        self.image = pygame.image.load("assets/towers/Idle/basic.png").convert_alpha()
        self.rect = self.image.get_rect(center=(self.pos[0], self.pos[1] + 32), size=(70, 70))
        self.sound_manager = sound_manager

    bulletDamage = TOWER_DAMAGE
    bullet_speed = BULLET_SPEED
    shotsPerSecond = TOWER_FIRE_RATE
    shootInterval = 1000 / shotsPerSecond
    upgradeCategory = ShopUpgradeCategory.BASIC
    
    @staticmethod
    def snap_to_grid(pos):
        cell_size = TILE_SIZE * 2
        x = (pos[0] // cell_size) * cell_size + cell_size // 2
        y = (pos[1] // cell_size) * cell_size + cell_size // 2
        return (x, y)

    @staticmethod
    def can_place_turret(pos, existing_turrets, grid_path):
        snapped_pos = Turret.snap_to_grid(pos)
        
        cell_size = TILE_SIZE * 2
        grid_x = snapped_pos[0] // cell_size
        grid_y = snapped_pos[1] // cell_size
        
        for i in range(0, len(grid_path) - 1):
            x1, y1 = grid_path[i]
            x2, y2 = grid_path[i + 1]
            
            if y1 == y2 and y1 == grid_y:
                if min(x1, x2) <= grid_x <= max(x1, x2):
                    return False
                    
            if x1 == x2 and x1 == grid_x:
                if min(y1, y2) <= grid_y <= max(y1, y2):
                    return False
        
        for turret in existing_turrets:
            if turret.pos == snapped_pos:
                return False
                
        return True
    
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def look_for_enemies(self, enemies):
    
        if self.current_enemy == None or (self.current_enemy != None and self.current_enemy.isDead()):
                lowest_hp_enemy = None
                for en in enemies:
                    en: Enemy
                    if(v2.distance(en.position, self.pos) <= self.range):
                        if lowest_hp_enemy != None:
                            if lowest_hp_enemy.health > lowest_hp_enemy.health:
                                lowest_hp_enemy = en
                        else:
                            lowest_hp_enemy = en
                    
                self.current_enemy = lowest_hp_enemy



    def predict_leading_direction(self, enemy):
        shooter_pos = pygame.math.Vector2(self.pos)
        enemy_pos = pygame.math.Vector2(enemy.position)

        # If enemy is frozen then aim directly at it
        if not enemy.can_move:
            return (enemy_pos - shooter_pos).normalize()

        # Predict enemy's position based on its path and speed
        if enemy.path_index < len(enemy.path) - 1:
            start = pygame.math.Vector2(enemy.tile_to_pixel(enemy.path[enemy.path_index]))
            end = pygame.math.Vector2(enemy.tile_to_pixel(enemy.path[enemy.path_index + 1]))
            enemy_velocity = (end - start).normalize() * enemy.speed
        else:
            return None


        # crazyyy math
        relative_pos = enemy_pos - shooter_pos
        a = enemy_velocity.dot(enemy_velocity) - self.bullet_speed ** 2
        b = 2 * relative_pos.dot(enemy_velocity)
        c = relative_pos.dot(relative_pos)

        delta = b ** 2 - 4 * a * c

        if delta < 0 or abs(a) < 1e-6:
            return (enemy_pos - shooter_pos).normalize()

        sqrt_delta = math.sqrt(delta)
        t1 = (-b + sqrt_delta) / (2 * a)
        t2 = (-b - sqrt_delta) / (2 * a)

        t = min(t for t in [t1, t2] if t > 0) if any(t > 0 for t in [t1, t2]) else None

        if t is None:
            return (enemy_pos - shooter_pos).normalize()

        future_enemy_pos = enemy_pos + enemy_velocity * t
        return (future_enemy_pos - shooter_pos).normalize()



    def shoot(self, direction_to_enemy):
        bullet = Bullet(self.pos, direction_to_enemy, self.bulletDamage, self.bullet_speed, self.bullet_color)
        self.bullets.add(bullet)
        self.sound_manager.play_random_shot()

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
                self.shoot(direction_to_enemy)
                
                self.last_shot_time = current_time
            else:
                direction_to_enemy = None
                distance_to_enemy = None
            
    
    def draw(self, surface):
        rect = self.image.get_rect(center=(self.pos[0], self.pos[1] - 32))
        surface.blit(self.image, rect)
        
    
    def draw_targeting_radius(self, surface):
        pygame.draw.circle(surface, WHITE, self.pos, self.range, 1)

