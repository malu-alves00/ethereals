import pygame
from player_class import Player
from ethereal_mob import WorldMob
from overworld import LevelTilemap
from ethereal_class import Ethereal
from battle import Battle

tiles_path = "./imagens/sprites_terrain/32bit/"

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('bahnschrift', 30)
clock = pygame.time.Clock()

player = Player("Lilium",32,32)

screenSize = [1216,800]
screen = pygame.display.set_mode(screenSize, pygame.SHOWN)

tilemap = LevelTilemap("starting_area")

def collision_checking():
    for rect_collision in tilemap.obstacles:
        if player.rect.colliderect(rect_collision[0]):
            if player.facing == "front":
                player.rect.y-=32
            elif player.facing == "back":
                player.rect.y+=32
            elif player.facing == "left":
                player.rect.x+=32
            elif player.facing == "right":
                player.rect.x-=32

gamemode = "overworld"

running = True
while running: # oh não, o tilemap atualiza a cada update da tela!! quem poderia prever?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and gamemode == "overworld":
                interacted=player.interact(tilemap.interactive)
                if interacted:
                    gamemode = interacted.get_interacted(screen)
            if event.key == pygame.K_ESCAPE and gamemode == "battle":
                gamemode = "overworld"
    
    if gamemode == "overworld":
        player.update()
        collision_checking()

        tilemap.blit_tiles(screen)
        tilemap.draw_mobs(screen)
        screen.blit(player.image, player.rect)

    if gamemode == "battle":
        #interacted.battle.draw_battle_screen(screen)
        interacted.battle.draw_enemy_sprites(screen)

    pygame.display.update()
    clock.tick(15)

pygame.quit()
