import pygame
from core import inputSystem
from core.map import Map
from core.enemy import Enemy
from core.turret import Turret
from core.constants import BLACK, SCREEN_WIDTH, SCREEN_HEIGHT, FPS

def main():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    game_map = Map()
    turrets = []
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

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
            
            #Mouse Click
            if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                inputSystem.leftMouseClickInteraction(event.pos)
                turrets.append(Turret(event.pos, bullets))
        
        #TODO Change to spawn enemies in waves curr spawns enemy every 2sec
        if current_time - last_spawn_time > spawn_interval:
            enemy = Enemy(game_map.path)
            enemies.add(enemy)
            last_spawn_time = current_time
            

        for enemy in enemies:
            enemy.update()
            if enemy.reached_end:
                enemies.remove(enemy)
                # TODO player losing hp
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
        screen.fill(BLACK)
        game_map.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
            
        for turret in turrets:
            turret.draw(screen)
            
        for b in bullets:
            b.draw(screen)
                
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()