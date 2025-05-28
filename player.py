import pygame
from consts import *
from bullet import Bullet

class Player:
    def __init__(self):
        # self.x = x
        # self.y = y
        image_path = "assets/images/PNG/playerShip1_blue.png"
        self.image = pygame.image.load(image_path).convert_alpha() 

        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20
        new_width = self.rect.width // 2
        new_height = self.rect.height // 2
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        self.speed = 0
        self.bullets = []
        self.time_since_last_bullet = 0

    def shoot(self):
        if self.time_since_last_bullet <= 0:
            self.bullets.append(Bullet(self.rect.centerx - self.rect.width/4,self.rect.centery - self.rect.height/6, -3))
            self.time_since_last_bullet = 10
    
    def move_left(self):
        self.speed = -3
        
                
    def move_right(self):
        self.speed = 3
    
    def update(self):
        if self.time_since_last_bullet > 0:
            self.time_since_last_bullet -= 1
        self.rect.centerx += self.speed 
        if self.rect.centerx < self.rect.width/2:
            self.rect.centerx = self.rect.width/2
            
        if self.rect.centerx > SCREEN_WIDTH:
            self.rect.centerx = SCREEN_WIDTH
            
        for bullet in self.bullets:
            bullet.update()
    
    def draw(self,screen):
        screen.blit(self.image, self.rect)
        for bullet in self.bullets:
            bullet.draw(screen)