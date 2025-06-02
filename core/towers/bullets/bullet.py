import pygame
from core.gameplay_configuration import BULLET_DESPAWN_TIME

def load_bullet_frames(sheet, start_x, start_y, frame_width, frame_height, frame_count):
    frames = []
    for i in range(frame_count):
        rect = pygame.Rect(start_x + i * frame_width, start_y, frame_width, frame_height)
        frame = sheet.subsurface(rect).copy()
        frame = pygame.transform.scale(frame, (frame_width * 2, frame_height * 2))
        frames.append(frame)
    return frames


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, dir, dmg, speed, color):
        super().__init__()
        self.pos = pos
        self.dir = dir
        self.damage = dmg
        self.speed = speed
        self.color = color
        self.spawnTime = pygame.time.get_ticks()

        # Load the sprite sheet and extract animation frames
        sheet = pygame.image.load("assets/bullets/OrangeBullet.png").convert_alpha()
        self.frames = load_bullet_frames(sheet, start_x=0, start_y=208, frame_width=16, frame_height=16, frame_count=4)

        self.current_frame = 0
        self.animation_speed = 100  # ms per frame
        self.last_frame_time = pygame.time.get_ticks()

        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=self.pos)
    
    despawn_time = BULLET_DESPAWN_TIME  # seconds before the bullet despawns

    def update(self, bullets):
        # Move the bullet
        if self.dir is None:
            self.kill()
            return


        self.pos = (
            self.pos[0] + self.dir[0] * self.speed,
            self.pos[1] + self.dir[1] * self.speed
        )
        self.rect.center = self.pos

        # Animate the bullet
        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_time >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_frame_time = current_time

        if current_time - self.spawnTime >= 1000 * self.despawn_time:
            #print("Bullet despawned")
            self.kill()
        
    def on_hit(self, enemy):
        self.kill()
        enemy.take_damage(self.damage)
        return False # Should be removed

    def draw(self, surface):
        rect = self.image.get_rect(center=self.pos)
        surface.blit(self.image, rect)
