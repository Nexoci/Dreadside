import pygame
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,image_to_use,speed):
        super().__init__() 
        self.image = pygame.image.load(image_to_use)
        self.image = pygame.transform.scale(self.image , (width, height)).convert_alpha() 
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        self.speed = speed
    def back(self):
        self.rect.x -= self.movex
        self.rect.y -= self.movey
    def move(self):
        key_input = pygame.key.get_pressed()
        self.movex = (key_input[pygame.K_a] * -self.speed) + (key_input[pygame.K_d] * self.speed)
        self.movey = (key_input[pygame.K_w] * -self.speed) + (key_input[pygame.K_s] * self.speed)
        self.rect.x += self.movex
        self.rect.y += self.movey

    def dead(self):
        self.kill()
        self.rect.x=10000
        
    def win(self):
        self.speed = 0
    def reset(self):
        # Reset the player's position to the initial coordinates
        self.rect.x = 350
        self.rect.y = 600
    def check_hit(self,group):
        if pygame.sprite.spritecollide(self,group, False, collided=pygame.sprite.collide_mask):
            return True
        else:
            return False
    def bullet_strike(self,group):
        if pygame.sprite.spritecollide(self,group, False, collided=pygame.sprite.collide_mask):
            return True
        
