import pygame
from consts import *
from enemy import Enemy
from player import Player
class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.init_enemies()
        
    def init_enemies(self):
        enemy = Enemy(3)
        self.enemies.append(enemy)
        
    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)
            
    def update(self,player):
        for enemy in self.enemies[:]:
            enemy.update()
            if len(player.bullets) > 0 and \
            enemy.rect.colliderect(player.bullets[0].rect):
                print("enemy Collision detected!")
                self.enemies.remove(enemy)
                player.bullets.pop(0)
            if len(enemy.bullets) > 0 and \
            player.rect.colliderect(enemy.bullets[0].rect):
                print(" player Collision detected!")
                enemy.bullets.pop(0)