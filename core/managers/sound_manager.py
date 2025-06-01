import pygame
import random

class SoundManager:

    def __init__(self):
        pygame.mixer.init()
        self.music_path = "assets/sounds/music.wav"
        self.shot_sounds_paths = [
            "assets/sounds/shot1.wav",
            "assets/sounds/shot2.wav",
            "assets/sounds/shot3.wav",
            "assets/sounds/shot4.wav",
            "assets/sounds/shot5.wav",
            "assets/sounds/shot6.wav",
        ]

        self.sounds = {}
        self.shot_sounds = []

        self._load_shot_sounds()

    def _load_shot_sounds(self):
        """Preload all shot sounds into memory."""
        self.shot_sounds = [pygame.mixer.Sound(path) for path in self.shot_sounds_paths]

    def load_sound(self, name, file_path):
        """Load a sound file and store it by name."""
        self.sounds[name] = pygame.mixer.Sound(file_path)

    def play_sound(self, name):
        """Play a named sound."""
        if name in self.sounds:
            self.sounds[name].play()

    def stop_sound(self, name):
        """Stop a named sound."""
        if name in self.sounds:
            self.sounds[name].stop()

    def set_volume(self, name, volume):
        """Set volume for a named sound."""
        if name in self.sounds:
            self.sounds[name].set_volume(volume)

    def play_random_shot(self):
        """Play a random gunshot sound."""
        if self.shot_sounds:
            random.choice(self.shot_sounds).play()

    def play_music(self, loop=True):
        """Start background music."""
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play(-1 if loop else 0)

    def stop_music(self):
        """Stop background music."""
        pygame.mixer.music.stop()

    def set_music_volume(self, volume):
        """Set background music volume (0.0 to 1.0)."""
        pygame.mixer.music.set_volume(volume)
