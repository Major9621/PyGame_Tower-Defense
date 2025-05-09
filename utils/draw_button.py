import pygame
from core.constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, GRAY

def draw_button(text, center_pos, font, screen):
    text_render = font.render(text, True, WHITE)
    rect = text_render.get_rect(center=center_pos)
    pygame.draw.rect(screen, GRAY, rect.inflate(20, 10))  #button background
    screen.blit(text_render, rect)
    return rect