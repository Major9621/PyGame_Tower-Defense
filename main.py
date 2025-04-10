import pygame
from core.map import Map
from core.enemy import Enemy
from core.constants import BLACK, SCREEN_WIDTH, SCREEN_HEIGHT, FPS

def main():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    game_map = Map()
    enemies = []

    spawn_interval = 2000
    last_spawn_time = 0

    # Game loop
    running = True
    while running:
        current_time = pygame.time.get_ticks()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #TODO Change to spawn enemies in waves curr spawns enemy every 2sec
        if current_time - last_spawn_time > spawn_interval:
            enemies.append(Enemy(game_map.path))
            last_spawn_time = current_time

        for enemy in enemies[:]:
            enemy.update()
            if enemy.reached_end:
                enemies.remove(enemy)
                # TODO player losing hp
            if enemy.health <= 0:
                enemy.die()
                enemies.remove(enemy)
        
        # Draw everything
        screen.fill(BLACK)
        game_map.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()