import pygame
from consts import *

class Bullet:
    def __init__(self,x,y,speed):
        self.x = x + 2
        self.y = y
        self.speed = speed
        image_path = "assets/images/PNG/Lasers/laserBlue01.png"
        self.image = pygame.image.load(image_path).convert_alpha() 

        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        new_width = self.rect.width // 2
        new_height = self.rect.height // 6
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
    
    def update(self):
        self.rect.centery += self.speed
        
    def draw(self,screen):
        screen.blit(self.image, self.rect)