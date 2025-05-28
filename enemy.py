import pygame, random
from consts import *
from bullet import Bullet

class Enemy:
    def __init__(self,x,y,row,col,image_index,shooting_enabled):
        self.row = row
        self.col = col
        image_path = self.set_image_path(image_index)
        self.image = pygame.image.load(image_path).convert_alpha() 

        # # self.rect = self.image.get_rect()
        # # self.rect.centerx = SCREEN_WIDTH // 2
        # # self.rect.bottom = SCREEN_HEIGHT // 2
        # # new_width = self.rect.width // 2
        # # new_height = self.rect.height // 2
        # self.image = pygame.transform.scale(self.image, (new_width, new_height))
        # self.shooting_enabled = shooting_enabled
        self.speed = 0
        self.yspeed = 0
        self.bullets = []
        self.time_since_last_bullet = random.randint(200,500)
        self.shooting_enabled = shooting_enabled
        if self.shooting_enabled:
            self.shoot()
        
        initial_rect = self.image.get_rect()
        initial_rect.centerx = x#SCREEN_WIDTH // 2
        initial_rect.bottom = y#SCREEN_HEIGHT//2
        new_width = initial_rect.width // 2
        new_height = initial_rect.height // 2
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        self.image = pygame.transform.rotate(self.image,180)
        self.rect = self.image.get_rect()

        self.rect.centerx = initial_rect.centerx
        self.rect.bottom = initial_rect.bottom

    def set_image_path(self,image_index):
        image_path = ""
        if image_index == 1:
            image_path = "assets/images/PNG/Enemies/enemyBlack1.png"
        elif image_index == 2:
            image_path = "assets/images/PNG/Enemies/enemyGreen2.png"
        elif image_index == 3:
            image_path = "assets/images/PNG/Enemies/enemyRed3.png"
        
        return image_path

    def shoot(self):
        if self.time_since_last_bullet <= 0:
            self.bullets.append(Bullet(self.rect.centerx - self.rect.width/4,self.rect.centery - self.rect.height/6, 3))
            self.time_since_last_bullet = random.randint(200,500)
            
            
    
    def move_left(self):
        self.speed = -3
        
                
    def move_right(self):
        self.speed = 3
        
    def move_down(self):
        self.yspeed = 1
        
        
    
    def update(self):
        if self.time_since_last_bullet > 0:
            self.time_since_last_bullet -= 1
        
        if self.time_since_last_bullet <= 0:
            #if random.randint(1, 500) == 1: # 1% chance each frame to shoot
            if self.shooting_enabled:
                self.shoot()
        self.rect.centerx += self.speed 
        if self.rect.centerx < self.rect.width/2:
            self.rect.centerx = self.rect.width/2
            
        if self.rect.centerx > SCREEN_WIDTH:
            self.rect.centerx = SCREEN_WIDTH
            
        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.is_off_screen():
                self.bullets.remove(bullet)
        
    def draw(self,screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen,RED,self.rect,1)
        for bullet in self.bullets:
            bullet.draw(screen)