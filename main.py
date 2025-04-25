import pygame
import sys
from core.screens.main_menu import mainMenu

running = True

def main():
    global running
    if running:
        mainMenu()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()