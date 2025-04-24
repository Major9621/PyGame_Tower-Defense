from core.enemy import Enemy
from core.constants import PURPLE
from pygame import Color

class FastEnemy(Enemy):
    def __init__(self, path):
        super().__init__(path)
        self.speed = 2.0
        self.health = 50
        self.max_health = 50
        self.color = Color("aqua")
