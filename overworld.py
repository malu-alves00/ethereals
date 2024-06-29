import pygame
import glob
import json
from ethereal_mob import WorldMob
import os
import random
import copy

class LevelTilemap:
    def __init__(self,level_name):
        self.level_name = level_name
        self.tiles_path = "./imagens/sprites_terrain/32bit/"
        self.obstacles_list = [4,6,7,8]
        self.x_rects = int(1216/32)
        self.y_rects = int(800/32)
        self.max_amount = 5
        self.open_files()
        self.add_tiles()
        self.create_tiles_rect_matrix()
        self.create_obstacles_rects()
        self.create_free_tiles()
        self.initialize_mobs_and_interactive()
        
    def open_files(self):
        for folder in os.listdir("./levels_data/"):
            if folder == self.level_name:
                with open("./levels_data/{}/{}.json".format(folder,folder)) as infile:
                    self.area = json.load(infile)
                with open("./levels_data/{}/{}_ethereals.json".format(folder,folder)) as infile:
                    self.spawn_table=json.load(infile)

    def add_tiles(self):
        self.f={}
        i=1
        for file in glob.glob(self.tiles_path+"*.png"): 
            loaded_img = pygame.image.load(file).convert()
            self.f[i] = file, loaded_img, loaded_img.get_rect(), int(file.rpartition('\\')[-1][0])
            i+=1
        xl = pygame.image.load("./imagens/sprites_terrain/32bit/1_ground_1.png").convert()
        self.f[0] = "./imagens/sprites_terrain/32bit/1_ground_1.png",xl,xl.get_rect(), 1

    def create_tiles_rect_matrix(self):
        self.tiles_rect_matrix = [[pygame.Rect(left,top,32,32) for left in range(0,1216,32)] for top in range(0,800,32)]
        self.tiles_matrix = [[[self.tiles_rect_matrix[i][j], self.area[i][j]] for j in range(self.x_rects)] for i in range(self.y_rects)]

    def create_obstacles_rects(self):
        self.obstacles = [[self.tiles_rect_matrix[i][j], self.area[i][j]]for j in range(self.x_rects) for i in range(self.y_rects) if self.area[i][j] in self.obstacles_list ]

    def create_free_tiles(self):
        self.free_tiles =[[self.tiles_rect_matrix[i][j], self.area[i][j]]for j in range(self.x_rects) for i in range(self.y_rects) if self.area[i][j] not in self.obstacles_list]

    def initialize_mobs_and_interactive(self):
        mob_amount=random.choices([5,4,3,2,1],weights=[10,15,20,25,30],k=1)
        mob_list=random.choices(list(self.spawn_table.keys()),weights=[self.spawn_table[item][0] for item in self.spawn_table],k=mob_amount[0])
        mob_levels=[random.randint(self.spawn_table[mob_item][2]-self.spawn_table[mob_item][3], self.spawn_table[mob_item][2]+self.spawn_table[mob_item][3]) for mob_item in mob_list]
        mob_rects=[]
        mob_rects = [random.choice(self.free_tiles) for i in range(mob_amount[0]) if self.free_tiles not in mob_rects]
        self.mob_objs=[WorldMob(mob_rects[i][0].x,mob_rects[i][0].y,mob_list[i],mob_levels[i]) for i in range(mob_amount[0])]
        self.obstacles.extend([[self.mob_objs[i].rect,999] for i in range(len(mob_list))])
        self.interactive=[]
        self.interactive.extend(self.mob_objs)
        
    def draw_mobs(self,screen):
        for item in self.mob_objs:
            screen.blit(item.image,item.rect)
        
    def blit_tiles(self,screen):
        for x_line in self.tiles_matrix:
            for y_line in x_line:
                screen.blit(self.f[y_line[1]][1],(y_line[0]))
        