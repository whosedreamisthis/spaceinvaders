import pygame
from consts import *

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
        self.speed = 3

    def move_left(self):
        self.rect.centerx -= self.speed 
        if self.rect.centerx < self.rect.width/2:
            self.rect.centerx = self.rect.width/2
                
    def move_right(self):
        self.rect.centerx += self.speed 
        if self.rect.centerx > SCREEN_WIDTH:
            self.rect.centerx = SCREEN_WIDTH
    
    def draw(self,screen):
        screen.blit(self.image, self.rect)