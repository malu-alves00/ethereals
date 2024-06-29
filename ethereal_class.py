import pygame
import json
import copy

class Ethereal():
    def __init__(self,level,name, nick):
        self.ethereals_path = "./ethereals_data/ethereals.json"
        self.ethereals_moves = "./ethereals_data/moves.json"
        self.ethereals_sprite = pygame.image.load("./imagens/ethereals/" + name + ".png")
        self.level = level
        self.species = name
        self.nickname = nick
        self.retrieve_ethereal()
        self.add_stats_to_current_level()
        self.determine_moves()
        print(level, name, nick)

    def retrieve_ethereal(self):
        with open(self.ethereals_path) as infile:
            ethereals_list = json.load(infile)
        for item in ethereals_list:
            if item == self.species:
                self.base_stats = ethereals_list[item]["base_stats"]
                self.up_stats = ethereals_list[item]["stats_levelup"]
        del ethereals_list
    
    def get_sprite(self,screen,location):
        screen.blit(self.ethereals_sprite,location)

    def add_stats_to_current_level(self):
        self.dict_copy = copy.copy(self.up_stats)
        self.stats={item:self.base_stats[item]+self.dict_copy[item]*(self.level-1) for item in self.up_stats}

    def determine_moves(self):
        pass

    def add_level(self):
        self.stats={item:self.stats[item]+self.dict_copy[item] for item in self.up_stats}

    def add_to_player_party(self):
        return self