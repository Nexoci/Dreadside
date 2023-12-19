import pygame
import sys
#custom object for copys of walls
class Background(pygame.sprite.Sprite):
    def __init__(self, width,height,image_to_use):
        super().__init__()
        self.image = pygame.image.load(image_to_use) 
        self.image = pygame.transform.scale(self.image, (width, height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(0,0))
       