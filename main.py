import pygame
import sys
from core import inputSystem
from core.waveManger import WaveManager
from core.map import Map
from core.enemy import Enemy
from core.player import Player
from core.turret import Turret
from screens.gameplay import play
from core.constants import DARKGREEN,BLACK, WHITE, GRAY, SCREEN_WIDTH, SCREEN_HEIGHT, FPS
import levels.maps as maps

running = True

def mainMenu():
    pygame.init()
    pygame.display.set_caption("MainMenu")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    font = pygame.font.SysFont("Arial-Bold", 50)

    #Drawing buttons
    def draw_button(text, center_pos):
        text_render = font.render(text, True, WHITE)
        rect = text_render.get_rect(center=center_pos)
        pygame.draw.rect(screen, GRAY, rect.inflate(20, 10))  #button background
        screen.blit(text_render, rect)
        return rect

    global running
    while running:
        screen.fill("black")

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        title_font = pygame.font.SysFont("Arial-Bold", 70)
        MENU_TEXT = title_font.render("Main Menu", True, WHITE)
        MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(MENU_TEXT, MENU_RECT)

        #Buttons
        start_button = draw_button("Start", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        settings_button = draw_button("Settings", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
        exit_button = draw_button("Exit", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start_button.collidepoint(MENU_MOUSE_POS):
                    print("Start Game")
                    if not play():
                        running = False

                elif settings_button.collidepoint(MENU_MOUSE_POS):
                    print("Settings")

                elif exit_button.collidepoint(MENU_MOUSE_POS):
                    print("Exiting")
                    running = False

        if running:
            pygame.display.update()

    pygame.quit()
    sys.exit()

def options():
    pass


if __name__ == "__main__":
    mainMenu()