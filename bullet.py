import pygame
from consts import *

class Bullet:
    def __init__(self,x,y,speed):
        self.x = x + 13
        self.y = y
        self.speed = speed
        image_path = "assets/images/PNG/Lasers/laserBlue01.png"
        self.image = pygame.image.load(image_path).convert_alpha() 
        initial_rect = self.image.get_rect()
        initial_rect.centerx = SCREEN_WIDTH // 2
        initial_rect.bottom = SCREEN_HEIGHT - 20
        new_width = initial_rect.width // 2
        new_height = initial_rect.height // 6
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y

    
    def update(self):
        self.rect.centery += self.speed
        
    def is_off_screen(self):
        if self.speed > 0 and self.rect.centery > SCREEN_HEIGHT:
            return True
        if self.speed < 0 and self.rect.centery < 0:
            return True
        return False
        
    def draw(self,screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen,RED,self.rect,1)