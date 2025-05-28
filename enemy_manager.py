import pygame
from consts import *
from enemy import Enemy
from player import Player


class EnemyManager:
    def __init__(self):
        self.num_rows = 5
        self.num_cols = 4
        self.enemies = []
        self.init_enemies()
        
    def init_enemies(self):
        dummy_enemy = Enemy(0,0,0,0,3,False)
        y = ENEMY_GRID_OFFSET_Y
        for i in range(self.num_rows):
            x = ENEMY_GRID_OFFSET_X
            for j in range(self.num_cols):
                enemy = Enemy(x,y,i,j,3, i == self.num_rows - 1)
                x += dummy_enemy.rect.width + 20
                self.enemies.append(enemy)
            y += dummy_enemy.rect.height + 20
        
        del dummy_enemy
        
    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)
            
    def update(self,player):
        for enemy in self.enemies[:]:
            enemy.update()
            if len(player.bullets) > 0 and \
            enemy.rect.colliderect(player.bullets[0].rect):
                print("enemy Collision detected!")
                row = enemy.row
                col = enemy.col
                row_above = row - 1
                for next_enemy in self.enemies:
                    if next_enemy.row == row_above and next_enemy.col == col:
                        next_enemy.shooting_enabled = True
                        next_enemy.shoot()
                    
                self.enemies.remove(enemy)
                
                player.bullets.pop(0)
            if len(enemy.bullets) > 0 and \
            player.rect.colliderect(enemy.bullets[0].rect):
                print(" player Collision detected!")
                enemy.bullets.pop(0)