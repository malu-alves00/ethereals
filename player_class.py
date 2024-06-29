import pygame
import copy
from ethereal_class import Ethereal

class Player():
    def __init__(self,name, x, y): # quantos selfs! 
        self.name = name
        self.left = pygame.image.load("./imagens/sprites_player/32bit/left.png")
        self.right = pygame.image.load("./imagens/sprites_player/32bit/right.png")
        self.front = pygame.image.load("./imagens/sprites_player/32bit/front.png")
        self.back = pygame.image.load("./imagens/sprites_player/32bit/back.png")
        self.image = self.front
        self.height = 32
        self.width = 32
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x,y
        self.facing="front"
        self.interacting_area_rects = {
            "upper_rect": "upper",
            "under_rect": "under",
            "left_rect": "left",
            "right_rect": "right"
        }
        
        self.update_interacting_areas_rect()
        self.interact_rect = self.interacting_area_rects["under_rect"]

        self.party = {}

    def update(self): # isso não deveria estar se atualizando constantemente, mas quem sou eu contra a gambiarra?
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and key[pygame.K_a] == False and key[pygame.K_s] == False:
            self.rect.y -= 32
            self.image = self.back
            self.facing="back"
        if key[pygame.K_s] and key[pygame.K_a] == False and key[pygame.K_d] == False:
            self.rect.y += 32
            self.image = self.front
            self.facing="front"
        if key[pygame.K_a] and key[pygame.K_w] == False and key[pygame.K_s]==False:
            self.rect.x -= 32
            self.image = self.left
            self.facing="left"
        if key[pygame.K_d] and key[pygame.K_w] == False and key[pygame.K_s]==False:
            self.rect.x += 32
            self.image = self.right
            self.facing="right"
        
        self.update_interacting_areas_rect()
        self.update_interact_rect()
        
    def update_interact_rect(self):
        if self.facing == "front":
            self.interact_rect = self.interacting_area_rects["under_rect"]
        elif self.facing == "back":
            self.interact_rect = self.interacting_area_rects["upper_rect"]
        elif self.facing == "left":
            self.interact_rect = self.interacting_area_rects["left_rect"]
        elif self.facing == "right":
            self.interact_rect = self.interacting_area_rects["right_rect"]

    def update_interacting_areas_rect(self): # achou que aqui teriam mais ifs? pois é né, todos têm seus momentos de clareza
        for item in self.interacting_area_rects:
            self.interacting_area_rects[item] = copy.copy(self.rect)
        
        self.interacting_area_rects["upper_rect"].y -= 32
        self.interacting_area_rects["under_rect"].y += 32
        self.interacting_area_rects["left_rect"].x -= 32
        self.interacting_area_rects["right_rect"].x += 32

    def interact(self,interactive):
        for item in interactive:
            if self.interact_rect.colliderect(item.rect):
                return item
        return False
    
    def add_ethereal_to_party(self,ethereal):
        temp = ethereal.add_to_player_party()
        print(temp)