import pygame
from utils.draw_button import draw_button
from core.constants import WHITE, SCREEN_WIDTH, SCREEN_HEIGHT

running = True
exit_gameplay = False

def pause(screen, font):
        global running
        global exit_gameplay
        while running:
            
            if exit_gameplay == True:
                return
            
            screen.fill("black")

            MENU_MOUSE_POS = pygame.mouse.get_pos()
            title_font = pygame.font.SysFont("Arial-Bold", 70)
            MENU_TEXT = title_font.render("Pause Menu", True, WHITE)
            MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
            screen.blit(MENU_TEXT, MENU_RECT)

            #Buttons
            resume_button = draw_button("Resume", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50), font, screen)
            main_menu_button = draw_button("Main Menu", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30), font, screen)
            exit_button = draw_button("Exit", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110), font, screen)

            #Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if resume_button.collidepoint(MENU_MOUSE_POS):
                        print("Resume")
                        return (True, True)

                    elif main_menu_button.collidepoint(MENU_MOUSE_POS):
                        print("Main Menu")
                        exit_gameplay = True    #mainMenu()
                        return (True, False)

                    elif exit_button.collidepoint(MENU_MOUSE_POS):
                        print("Exiting")
                        running = False
                        return (False, False)
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return (True, True)
            
            pygame.display.update()