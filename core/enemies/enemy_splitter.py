from core.enemies.enemy import Enemy
import pygame
from core.gameplay_configuration import ENEMY_HEALTH, ENEMY_SPEED
from utils.direction import Direction
from core.gameplay_configuration import ENEMY_GOLD_DROP


class SplitterEnemy(Enemy):
    def __init__(self, path, gold_manager):
        super().__init__(path, gold_manager)
        self.health = ENEMY_HEALTH * 1.5
        self.max_health = self.health
        self.speed = ENEMY_SPEED * 0.8
        self.sprite_sheet = pygame.image.load("assets/enemies/Splitter.png").convert_alpha()
        self.split_count = 2
        self.spread_distance = 30
        self.frames = {
            "walk":{
                Direction.DOWN: self.load_frames(row=3, count=8),
                Direction.UP: self.load_frames(row=4, count=8),
                Direction.LEFT: self.load_frames(row=5, count=8),
                Direction.RIGHT: self.load_frames(row=5, count=8),
            },
            "die":{
                Direction.DOWN: self.load_frames(row=6, count=8),
                Direction.UP: self.load_frames(row=7, count=8),
                Direction.LEFT: self.load_frames(row=8, count=8),
                Direction.RIGHT: self.load_frames(row=8, count=8),
            }
        }
    def die(self):
        if self.state != "die":
            small_enemy = SmallSplitEnemy(self.path[self.path_index:], self.gold_manger)
            small_enemy.position = self.position
            small_enemy.rect.center = self.position
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {"enemy": small_enemy}))
        super().die()

class SmallSplitEnemy(Enemy):
    def __init__(self, path, gold_manager):
        super().__init__(path, gold_manager)
        self.health = ENEMY_HEALTH * 0.5
        self.max_health = self.health
        self.speed = ENEMY_SPEED * 1.2
        self.gold_drop = self.gold_drop // 2
        self.sprite_sheet = pygame.image.load("assets/enemies/SplitterMini.png").convert_alpha()
        self.frames = {
            "walk":{
                Direction.DOWN: self.load_frames(row=3, count=8),
                Direction.UP: self.load_frames(row=4, count=8),
                Direction.LEFT: self.load_frames(row=5, count=8),
                Direction.RIGHT: self.load_frames(row=5, count=8),
            },
            "die":{
                Direction.DOWN: self.load_frames(row=6, count=8),
                Direction.UP: self.load_frames(row=7, count=8),
                Direction.LEFT: self.load_frames(row=8, count=8),
                Direction.RIGHT: self.load_frames(row=8, count=8),
            }
        }
