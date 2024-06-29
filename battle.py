import pygame

class Battle:
    def __init__(self,enemies_array,state):
        self.enemies_array = enemies_array
        self.curr_enemy = enemies_array[0]
        self.battle_buttons_ui = pygame.image.load("./imagens/sprites_ui/battle_box_1.png").convert()
        self.battle_buttons_ui_rect = self.battle_buttons_ui.get_rect()
        #self.allies = 

    def draw_battle_screen(self,screen):
        screen.blit(self.battle_buttons_ui,self.battle_buttons_ui_rect)

    def draw_enemy_sprites(self,screen):
        screen_location = [200,200]
        self.curr_enemy.get_sprite(screen,screen_location)

    def create_clickable_areas(self):
        pass