import pygame
from consts import *
from enemy import Enemy
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
            
    def update(self):
        for enemy in self.enemies:
            enemy.update()