from core.enemy import Enemy
from pygame import Color

class TankEnemy(Enemy):
    def __init__(self, path):
        super().__init__(path)
        self.speed = 0.5
        self.health = 300
        self.max_health = 300
        self.color = Color("darkslateblue")