from .enemy import Enemy
from .enemy_fast import FastEnemy
from .enemy_tank import TankEnemy


ENEMY_TYPES = {
    "default": {"class": Enemy, "power": 1},
    "fast": {"class": FastEnemy, "power": 2},
    "tank": {"class": TankEnemy, "power": 5},
}
