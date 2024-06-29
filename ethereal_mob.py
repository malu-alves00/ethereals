import pygame
from ethereal_class import Ethereal
from battle import Battle

class WorldMob():
    def __init__(self,x,y,species,level):
        self.species = species
        self.level = level

        self.left = pygame.image.load("./imagens/sprites_mob/32bit/left_1.png")
        self.right = pygame.image.load("./imagens/sprites_mob/32bit/right_1.png")
        self.front = pygame.image.load("./imagens/sprites_mob/32bit/front_1.png")
        self.back = pygame.image.load("./imagens/sprites_mob/32bit/back_1.png")
        self.image = self.front
        self.facing = "front"

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x,y

    def update(self):
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
    
    def get_interacted(self,screen):
        print("start battle >:(")
        screen.fill("#000000")
        self.ethereal = Ethereal(self.level,self.species,self.species)
        self.battle = Battle([self.ethereal],"wild")
        return "battle"