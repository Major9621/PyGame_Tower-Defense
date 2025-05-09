import pygame
import random

from core.enemies.enemy_registry import ENEMY_TYPES

class WaveManager:
    def __init__(self, spawn_enemy_callback, ui_manager):
        self.ui_manager = ui_manager
        self.wave_number = -1
        self.spawn_enemy = spawn_enemy_callback
        self.wave_in_progress = False
        self.ready_for_next_wave = True

        self.spawn_interval = 1000
        self.last_spawn_time = 0

        self.auto_wave_delay = 5000
        self.time_wave_finished = None

        self.enemy_unlock_interval = 2
        self.unlocked_enemy_types = []
        self.spawn_queue = []

    def start_next_wave(self):
            self.wave_number += 1
            self.ui_manager.update_wave_number(self.wave_number)

            # Unlock new enemy type every 5 waves
            type_keys = list(ENEMY_TYPES.keys())
            if self.wave_number % self.enemy_unlock_interval == 0 and len(self.unlocked_enemy_types) < len(type_keys):
                new_type = type_keys[len(self.unlocked_enemy_types)]
                self.unlocked_enemy_types.append(new_type)
                print(f"[WaveManager] Unlocked enemy type: {new_type}")

            # Power budget scales with wave
            power_budget = int(10 * (self.wave_number ** 1.2)) + 5
            self.spawn_queue = self.generate_wave_enemies(power_budget)
            self.wave_in_progress = True
            self.ready_for_next_wave = False
            self.last_spawn_time = pygame.time.get_ticks()
            self.time_wave_finished = None

            print(f"[WaveManager] Starting wave {self.wave_number} with {len(self.spawn_queue)} enemies (power {power_budget})")

    def update(self, current_time):
        if self.wave_number == -1:
            self.start_next_wave()

        if self.wave_in_progress and self.spawn_queue:
            if current_time - self.last_spawn_time >= self.spawn_interval:
                enemy_type = self.spawn_queue.pop(0)
                enemy_class = ENEMY_TYPES[enemy_type]["class"]
                self.spawn_enemy(enemy_class)
                self.last_spawn_time = current_time

        # auto start the wave after auto_wave_delay (curr. 5secs)
        if self.ready_for_next_wave and self.time_wave_finished is not None:
            if current_time - self.time_wave_finished >= self.auto_wave_delay:
                self.start_next_wave()


    def check_wave_complete(self, active_enemies, current_time):
        if not self.spawn_queue and len(active_enemies) == 0 and not self.ready_for_next_wave:
            self.wave_in_progress = False
            self.ready_for_next_wave = True
            self.time_wave_finished = current_time
            print(f"[WaveManager] Wave {self.wave_number} finished. Waiting to start next wave...")


    def generate_wave_enemies(self, total_power):
        enemies = []
        types = self.unlocked_enemy_types

        while total_power > 0:
            valid_choices = [t for t in types if ENEMY_TYPES[t]["power"] <= total_power]
            if not valid_choices:
                break
            chosen = random.choice(valid_choices)
            enemies.append(chosen)
            total_power -= ENEMY_TYPES[chosen]["power"]

        return enemies
