import pygame
from enum import Enum
from core.towers.shop.shop_item import ShopItem
from core.towers.turret import Turret
from core.towers.twin_turret import TwinTurret
from core.towers.sniper_turret import SniperTurret
from core.towers.better_twin_turret import BetterTwinTurret
from core.towers.shop.shop_category import ShopUpgradeCategory
from core.towers.better_sniper_turret import BetterSniperTurret
from core.towers.piercing_turret import PiercingTurret
from core.towers.freeze_turret import FreezeTurret
from core.towers.bomber_turret import BomberTurret
from core.gameplay_configuration import (
    TOWER_COST,
    TWIN_TOWER_COST, BETTER_TWIN_TOWER_COST,
    SNIPER_TOWER_COST, BETTER_SNIPER_TOWER_COST,
    FREEZE_TOWER_COST, PIERCING_TOWER_COST, BOMBER_TOWER_COST
)

class TurretShop:
    def __init__(self, pos):
        self.pos = pos
        self.shop_category = ShopUpgradeCategory.NONE
        self.selected_item = None


        # All shop items for every level
        self.items_by_category = {
            0: [  # NONE
                ShopItem(TOWER_COST, "assets/towers/Idle/basic.png", Turret),
            ],
            1: [  # BASIC upgrades
                ShopItem(TWIN_TOWER_COST, "assets/towers/Idle/twin.png", TwinTurret),
                ShopItem(SNIPER_TOWER_COST, "assets/towers/Idle/sniper.png", SniperTurret),
                ShopItem(FREEZE_TOWER_COST, "assets/towers/Idle/freeze.png", FreezeTurret),
            ],
            2: [  # TWIN upgrades
                ShopItem(BETTER_TWIN_TOWER_COST, "assets/towers/Idle/better_twin.png", BetterTwinTurret),
            ],
            3: [  # SNIPER upgrades
                ShopItem(BETTER_SNIPER_TOWER_COST, "assets/towers/Idle/better_sniper.png", BetterSniperTurret),
            ],
            4: [  # FREEZE upgrades
                ShopItem(PIERCING_TOWER_COST, "assets/towers/Idle/piercing.png", PiercingTurret),
                ShopItem(BOMBER_TOWER_COST, "assets/towers/Idle/bomber.png", BomberTurret),
            ],
        }

        self.item_slots = []
        

    def draw_shop_menu(self, screen):
        self.item_slots.clear()
        items = self.items_by_category.get(self.shop_category.value, [])
        spacing = 10
        slot_width = 60
        start_x = self.pos[0] + 10
        y = self.pos[1]

        for idx, item in enumerate(items):
            x = start_x + idx * (slot_width + spacing)
            slot_rect = item.draw(screen, (x, y))
            self.item_slots.append((slot_rect, item))

    def deselect_all_items(self):
        for _, item in self.item_slots:
            item.selected = False
        self.selected_item = None


    def handle_click(self, mouse_pos):
        for rect, item in self.item_slots:
            if rect.collidepoint(mouse_pos):
                self.deselect_all_items()
                item.selected = True
                self.selected_item = item
                return True  # click in shop

        return False  # click outside the shop
