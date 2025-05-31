import pygame
from core.constants import BLUE, YELLOW, TILE_SIZE
from core.gameplay_configuration import TOWER_RANGE, TOWER_DAMAGE, TOWER_FIRE_RATE, BULLET_SPEED
from core.towers.bullets.bullet import Bullet
from core.enemies.enemy import Enemy
from utils import vector2 as v2

#TODO: Add grid snapping and disable turret stacking
class Turret:
    def __init__(self, pos, bullets):
        self.pos = self.snap_to_grid(pos)
        self.lastShotTime = pygame.time.get_ticks()
        self.range = TOWER_RANGE
        self.currentEnemy = None
        self.bullets = bullets
        self.image = pygame.image.load("assets/towers/Idle/1.png").convert_alpha()

    bulletDamage = TOWER_DAMAGE
    bulletSpeed = BULLET_SPEED
    shotsPerSecond = TOWER_FIRE_RATE
    shootInterval = 1000 / shotsPerSecond
    
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


    def update(self, enemies):
        currentTime = pygame.time.get_ticks()
        
        
        #If is able to shoot
        if currentTime - self.lastShotTime >= self.shootInterval: 
            
            #Looking for new (closest) enemy
            if self.currentEnemy == None or (self.currentEnemy != None and self.currentEnemy.isDead()):
                closestEnemy = None
                for en in enemies:
                    en: Enemy
                    if(v2.distance(en.position, self.pos) <= self.range):
                        if closestEnemy != None:
                            if v2.distance(closestEnemy.position, self.pos) > v2.distance(en.position, self.pos):
                                closestEnemy = en
                        else:
                            closestEnemy = en
                    
                self.currentEnemy = closestEnemy
                
            #If has enemy or just found it calculate shoot direction
            if self.currentEnemy != None:
                directionToEnemy = v2.normalized(v2.subtract(self.currentEnemy.position, self.pos))
                distanceToEnemy = v2.distance(self.currentEnemy.position, self.pos)
                
                if self.currentEnemy.reached_end or distanceToEnemy > self.range:
                    self.currentEnemy = None
                
                #Shoot!
                bullet = Bullet(self.pos, directionToEnemy, self.bulletDamage, self.bulletSpeed, YELLOW)
                self.bullets.add(bullet)
                
                self.lastShotTime = currentTime
            else:
                directionToEnemy = None
                distanceToEnemy = None
            
            

    
    def draw(self, surface):
        rect = self.image.get_rect(center=(self.pos[0], self.pos[1] - 32))
        surface.blit(self.image, rect)
        pygame.draw.circle(surface, BLUE, self.pos, self.range, 1)

