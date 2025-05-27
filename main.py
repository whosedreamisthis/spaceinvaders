import pygame
from consts import *
from player import Player

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
running = True
FPS = 60
player = Player()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    elif keys[pygame.K_RIGHT]:
        player.move_right()
    screen.fill(BLACK)
    player.draw(screen)
    pygame.display.update()    
    clock.tick(FPS)

pygame.quit()