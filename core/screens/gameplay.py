import pygame
from core.managers.waveManger import WaveManager
from core.map import Map
from core.player import Player
from core.towers.turret import Turret
from core.managers.ui_manager import UI_Manager
from core.managers.gold_manager import GoldManager
from core.towers.turret_shop import TurretShop

from utils.draw_button import draw_button
from core.screens.pause_menu import pause
from core.constants import DARKGREEN, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT, FPS, init_tile_types, \
    TILESET_PATH
from core.gameplay_configuration import STARTING_GOLD, TOWER_COST, PLAYER_HP
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
    init_tile_types(TILESET_PATH)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial-Bold", 50)
    
    #Drawing Buttons

    
    #Pause 
    
    
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
            main_menu_button = draw_button("Main Menu", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30), font, screen)
            exit_button = draw_button("Exit", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

            #Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    
                    if main_menu_button.collidepoint(MENU_MOUSE_POS):
                        print("Main Menu")
                        exit_gameplay = True #mainMenu()
                        return True

                    elif exit_button.collidepoint(MENU_MOUSE_POS):
                        print("Exiting")
                        running = False
                        return False
                    
            
            pygame.display.update()
    
    def try_place_turret(pos):
        snapped_pos = Turret.snap_to_grid(pos)
        if Turret.can_place_turret(snapped_pos, turrets, game_map.grid_path) and turret_shop.selected_item != None:
            if gold_manager.spend_gold(turret_shop.selected_item.price):
                new_turret = turret_shop.selected_item.prefab(snapped_pos, bullets)
                turrets.append(new_turret)
                turret_shop.deselect_all_items()  
                return True
        return False


    game_map = Map(maps.grid_path2)
    turrets = []
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    turret_shop = TurretShop(None)

    ui_manager = UI_Manager(screen, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5), 1, STARTING_GOLD, turret_shop)
    turret_shop = ui_manager.turret_shop
    gold_manager = GoldManager(STARTING_GOLD, ui_manager)
    wave_system = WaveManager(lambda cls: enemies.add(cls(game_map.grid_path, gold_manager)), ui_manager)
    player = Player(PLAYER_HP, ui_manager)
    show_turret_range = False
    
    # Game loop 
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
                if turret_shop.handle_click(event.pos):
                    pass
                else:
                    try_place_turret(event.pos)
            
            #Pause game
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    result = pause(screen, font)
                    if result[0] == False:
                        running = False
                        return False
                    elif result[1] == False:
                        exit_gameplay = True
                        return True
                elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    show_turret_range = True
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    show_turret_range = False

            if event.type == pygame.USEREVENT:
                if hasattr(event, 'enemy'):
                    enemies.add(event.enemy)
                    
        if exit_gameplay:   #Exit to main menu
            return True

        wave_system.update(current_time)
        wave_system.check_wave_complete(enemies, current_time)
        for enemy in enemies:
            enemy.update()
            if enemy.reached_end:
                player.take_damage(enemy.damage)   #Taking damage if enemy reaches end
                enemies.remove(enemy)
                continue
                
        for turret in turrets:
            turret.update([e for e in enemies if e.state != "die"])
        
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

        
        for enemy in enemies:
            enemy.draw(screen)
            
        for turret in turrets:
            turret.draw(screen)
            if show_turret_range:
                turret.draw_targeting_radius(screen)
            
        for b in bullets:
            b.draw(screen)
            

        ui_manager.draw_shop()
        ui_manager.draw_health_bar()
        ui_manager.draw_text()

        pygame.display.flip()
        clock.tick(FPS)
        
        

    
    return False    #EXIT game