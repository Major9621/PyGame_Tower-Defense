import pygame
from core.towers.shop_item import ShopItem
from core.towers.turret import Turret

class TurretShop:
    def __init__(self, pos):
        self.pos = pos
        self.current_level = 1
        self.selected_item = None


        # All shop items for every level
        self.items_for_every_level = {
            1: [
                ShopItem(100, "assets/towers/Idle/1.png", Turret),
                ShopItem(200, "assets/towers/Idle/2.png", Turret),
            ],
            2: [
                ShopItem(150, "assets/towers/Idle/3.png", Turret),
                ShopItem(250, "assets/towers/Idle/4.png", Turret),
            ],
        }

        self.item_slots = []
        

    def draw_shop_menu(self, screen):
        self.item_slots.clear()
        items = self.items_for_every_level.get(self.current_level, [])
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
