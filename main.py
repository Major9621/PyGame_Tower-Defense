import pygame
import sys
from core.screens.main_menu import mainMenu
from core.constants import init_tile_types, TILESET_PATH

running = True

def main():
    global running
    if running:
        mainMenu()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()