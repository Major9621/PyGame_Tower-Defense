import pygame
from core.constants import DARKGREEN

class GoldManager:
    def __init__(self, initial_currency, ui_manager):
        self.ui_manager = ui_manager
        self.gold_amount = initial_currency
        
    def enough_gold(self, amount):
        return self.gold_amount >= amount

    def add_gold(self, amount):
        self.gold_amount += amount
        self.ui_manager.update_gold_amount(self.gold_amount)
        
    def spend_gold(self, amount):
        if self.gold_amount >= amount:
            self.gold_amount -= amount
            self.ui_manager.update_gold_amount(self.gold_amount)
            return True
        else:
            return False