import pygame

class WaveManager:
    def __init__(self, spawn_enemy_callback):
        self.wave_number = -1
        self.enemies_left_to_spawn = 0
        self.spawn_enemy = spawn_enemy_callback
        self.wave_in_progress = False
        self.ready_for_next_wave = True

        self.spawn_interval = 1000
        self.last_spawn_time = 0

        self.auto_wave_delay = 5000
        self.time_wave_finished = None

    def start_next_wave(self):
        self.wave_number += 1
        self.enemies_left_to_spawn = 5 + self.wave_number * 2
        self.wave_in_progress = True
        self.ready_for_next_wave = False
        self.last_spawn_time = pygame.time.get_ticks()
        self.time_wave_finished = None
        print(f"[WaveManager] Starting wave {self.wave_number}")

    def update(self, current_time):
        if self.wave_number == -1:
            self.start_next_wave()

        if self.wave_in_progress and self.enemies_left_to_spawn > 0:
            if current_time - self.last_spawn_time >= self.spawn_interval:
                self.spawn_enemy()
                self.enemies_left_to_spawn -= 1
                self.last_spawn_time = current_time

        # auto start the wave after auto_wave_delay (curr. 5secs)
        if self.ready_for_next_wave and self.time_wave_finished is not None:
            if current_time - self.time_wave_finished >= self.auto_wave_delay:
                self.start_next_wave()

    def check_wave_complete(self, active_enemies, current_time):
        if self.enemies_left_to_spawn == 0 and len(active_enemies) == 0 and not self.ready_for_next_wave:
            self.wave_in_progress = False
            self.ready_for_next_wave = True
            self.time_wave_finished = current_time
            print(f"[WaveManager] Wave {self.wave_number} finished. Waiting to start next wave...")
