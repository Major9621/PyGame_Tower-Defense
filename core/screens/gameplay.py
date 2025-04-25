import pygame
import sys
from core import inputSystem
from core.waveManger import WaveManager
from core.map import Map
from core.enemy import Enemy
from core.player import Player
from core.turret import Turret
from core.constants import DARKGREEN,BLACK, WHITE, GRAY, SCREEN_WIDTH, SCREEN_HEIGHT, FPS
import levels.maps as maps

running = True
exit_gameplay = False

def play():
    pygame.init()
    global running
    global exit_gameplay
    exit_gameplay = False
    pygame.display.set_caption("Play")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial-Bold", 50)
    
    game_map = Map(maps.path6)
    #Drawing Buttons
    def draw_button(text, center_pos):
        text_render = font.render(text, True, WHITE)
        rect = text_render.get_rect(center=center_pos)
        pygame.draw.rect(screen, GRAY, rect.inflate(20, 10))  #button background
        screen.blit(text_render, rect)
        return rect
    
    #Pause 
    def pause():
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
            resume_button = draw_button("Resume", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
            main_menu_button = draw_button("Main Menu", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
            exit_button = draw_button("Exit", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

            #Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if resume_button.collidepoint(MENU_MOUSE_POS):
                        print("Resume")
                        return

                    elif main_menu_button.collidepoint(MENU_MOUSE_POS):
                        print("Main Menu")
                        exit_gameplay = True    #mainMenu()
                        return

                    elif exit_button.collidepoint(MENU_MOUSE_POS):
                        print("Exiting")
                        running = False
                        return
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            
            pygame.display.update()
    
    #Game over
    def game_over():
        global running
        global exit_gameplay
        while running:
            if exit_gameplay:
                return
            
            screen.fill("black")

            MENU_MOUSE_POS = pygame.mouse.get_pos()
            title_font = pygame.font.SysFont("Arial-Bold", 70)
            MENU_TEXT = title_font.render("GAME OVER!", True, WHITE)
            MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
            screen.blit(MENU_TEXT, MENU_RECT)

            #Buttons
            main_menu_button = draw_button("Main Menu", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
            exit_button = draw_button("Exit", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

            #Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    
                    if main_menu_button.collidepoint(MENU_MOUSE_POS):
                        print("Main Menu")
                        exit_gameplay = True #mainMenu()
                        return

                    elif exit_button.collidepoint(MENU_MOUSE_POS):
                        print("Exiting")
                        running = False
                        return
            
            pygame.display.update()
    
    game_map = Map(maps.path6)
    turrets = []
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    wave_system = WaveManager(lambda cls: enemies.add(cls(game_map.path)))

    # Game loop
    player = Player(1000, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5))
    
    while running:
        current_time = pygame.time.get_ticks()

        if player.is_dead():
            print("Game over")
            game_over()
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            #Mouse Click
            if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                inputSystem.leftMouseClickInteraction(event.pos)
                turrets.append(Turret(event.pos, bullets))
            
            #Pause game
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()
        
        if exit_gameplay:   #Exit to main menu
            return True

        wave_system.update(current_time)
        wave_system.check_wave_complete(enemies, current_time)
        for enemy in enemies:
            enemy.update()
            if enemy.reached_end:
                player.take_damage(50)   #Taking damage if enemy reaches end
                enemies.remove(enemy)
            if enemy.health <= 0:
                enemies.remove(enemy)
                
        for turret in turrets:
            turret.update(enemies)
        
        for b in bullets:
            b.update(bullets)
        
        
        for bullet in bullets:
            enemies_hit = pygame.sprite.spritecollide(bullet, enemies, False)
            for enemy in enemies_hit:
                
                enemy.take_damage(bullet.damage)
                bullets.remove(bullet)
        
        
        # Draw everything
        screen.fill(DARKGREEN)
        game_map.draw(screen)
        player.draw_health_bar(screen)
        for enemy in enemies:
            enemy.draw(screen)
            
        for turret in turrets:
            turret.draw(screen)
            
        for b in bullets:
            b.draw(screen)
                
        pygame.display.flip()
        clock.tick(FPS)
    
    return False    #EXIT game