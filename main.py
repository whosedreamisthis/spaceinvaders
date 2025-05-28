import pygame
from consts import *
from player import Player
from enemy_manager import EnemyManager

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
running = True
FPS = 60
player = Player()
enemy_manager = EnemyManager()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or \
                event.key == pygame.K_RIGHT:
                    player.speed = 0
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    elif keys[pygame.K_RIGHT]:
        player.move_right()
    if keys[pygame.K_SPACE]:
        player.shoot()
        
    enemy_manager.update()
    player.update()
    screen.fill(BLACK)
    enemy_manager.draw(screen)
    player.draw(screen)
    pygame.display.update()    
    clock.tick(FPS)

pygame.quit()