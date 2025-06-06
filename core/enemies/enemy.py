import pygame
import math
from core.constants import GREEN, BLACK, ENEMY_RADIUS, TILE_SIZE
from core.gameplay_configuration import ENEMY_GOLD_DROP, ENEMY_HEALTH, ENEMY_SPEED, ENEMY_DAMAGE
from utils.direction import Direction

class Enemy(pygame.sprite.Sprite):
    def __init__(self, path, gold_manger, hp_multiplier):
        super().__init__()
        self.path = path
        self.path_index = 0
        self.progress = 0
        self.damage = ENEMY_DAMAGE
        self.speed = ENEMY_SPEED
        self.health = ENEMY_HEALTH * hp_multiplier
        self.max_health = ENEMY_HEALTH
        self.reached_end = False
        self.value = 10
        self.direction = Direction.RIGHT
        self.flip = False
        self.gold_drop = ENEMY_GOLD_DROP
        self.gold_manger = gold_manger
        self.can_move = True

        # Load sprite sheet
        self.sprite_sheet = pygame.image.load("assets/enemies/Leafbug.png").convert_alpha()
        self.frame_width = self.sprite_sheet.get_width() // 8
        self.frame_height = self.sprite_sheet.get_height() // 9
        self.animation_timer = 0
        self.animation_speed = 0.15
        self.frame_index = 0
        self.state = "walk"

        self.frames = {
            "walk":{
                Direction.DOWN: self.load_frames(row=3, count=8),
                Direction.UP: self.load_frames(row=4, count=8),
                Direction.LEFT: self.load_frames(row=5, count=8),
                Direction.RIGHT: self.load_frames(row=5, count=8),
            },
            "die":{
                Direction.DOWN: self.load_frames(row=6, count=8),
                Direction.UP: self.load_frames(row=7, count=8),
                Direction.LEFT: self.load_frames(row=8, count=8),
                Direction.RIGHT: self.load_frames(row=8, count=8),
            }
        }

        self.image = self.frames[self.state][self.direction][0]
        self.rect = self.image.get_rect(center=self.tile_to_pixel(path[0]))
        self.position = self.rect.center

    def load_frames(self, row, count):
        frames = []
        for i in range(count):
            frame = self.sprite_sheet.subsurface(
                pygame.Rect(
                    i * self.frame_width,
                    row * self.frame_height,
                    self.frame_width,
                    self.frame_height
                )
            )
            frames.append(pygame.transform.scale(frame, (ENEMY_RADIUS * 2, ENEMY_RADIUS * 2)))
        return frames


    def tile_to_pixel(self, tile_pos):
        return (
            tile_pos[0] * TILE_SIZE * 2 + TILE_SIZE,
            tile_pos[1] * TILE_SIZE * 2 + TILE_SIZE
        )

    def update(self):
        self.animate()

        if self.state == "die":
            if self.frame_index >= len(self.frames["die"]) - 1:
                self.kill()
            return

        if self.reached_end or self.health <= 0 or not self.can_move:
            return

        if self.path_index >= len(self.path) - 1:
            self.reached_end = True
            return

        start = self.tile_to_pixel(self.path[self.path_index])
        end = self.tile_to_pixel(self.path[self.path_index + 1])

        dx = end[0] - start[0]
        dy = end[1] - start[1]

        if abs(dx) > abs(dy):
            self.direction = Direction.RIGHT if dx > 0 else Direction.LEFT
        else:
            self.direction = Direction.DOWN if dy > 0 else Direction.UP

        distance = math.sqrt(dx ** 2 + dy ** 2)

        move_amount = self.speed / distance
        self.progress += move_amount

        self.position = (
            start[0] + dx * self.progress,
            start[1] + dy * self.progress
        )

        self.rect.center = self.position

        if self.progress >= 1:
            self.progress = 0
            self.path_index += 1
            if self.path_index >= len(self.path) - 1:
                self.reached_end = True

    def animate(self):
        self.animation_timer += self.animation_speed
        current_frames = self.frames[self.state][self.direction]

        if self.animation_timer >= 1:
            self.animation_timer = 0
            if self.state == "die":
                if self.frame_index < len(current_frames) - 1:
                    self.frame_index += 1
            else:
                self.frame_index = (self.frame_index + 1) % len(current_frames)

        if self.direction == Direction.RIGHT and self.flip:
            self.image = pygame.transform.flip(current_frames[self.frame_index], True, False)
        else:
            self.image = current_frames[self.frame_index]

    def draw(self, surface):
        surface.blit(self.image, self.rect)

        # Health bar
        bar_width = 30
        health_percent = self.health / self.max_health
        pygame.draw.rect(surface, BLACK,
                         (self.position[0] - bar_width//2, self.position[1] - ENEMY_RADIUS - 10,
                          bar_width, 5))
        pygame.draw.rect(surface, GREEN,
                         (self.position[0] - bar_width//2, self.position[1] - ENEMY_RADIUS - 10,
                          int(bar_width * health_percent), 5))

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0 and self.state != "die":
            self.die()

    def die(self):
        self.health = 0
        self.state = "die"
        self.frame_index = 0
        self.animation_timer = 0
        self.gold_manger.add_gold(self.gold_drop)

    def isDead(self):
        return self.health <= 0
