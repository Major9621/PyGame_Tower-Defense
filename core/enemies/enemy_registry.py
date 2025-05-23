from .enemy import Enemy
from .enemy_fast import FastEnemy
from .enemy_tank import TankEnemy
from .enemy_splitter import SplitterEnemy
from .enemy_teleporter import TeleporterEnemy
from .enemy_shielded import ShieldedEnemy
from .enemy_healer import HealerEnemy

ENEMY_TYPES = {
    # "default": {"class": Enemy, "power": 1},
    # "fast": {"class": FastEnemy, "power": 2},
    # "tank": {"class": TankEnemy, "power": 5},
    "splitter" : {"class": SplitterEnemy, "power": 5},
    "teleporter": {"class": TeleporterEnemy, "power": 5},
    "shielded": {"class": ShieldedEnemy, "power": 5},
    "healer": {"class": HealerEnemy, "power": 7},
}
