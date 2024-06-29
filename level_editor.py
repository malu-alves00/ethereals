import pygame
import math
import json
import glob

pygame.init()

# cria tela e a barra amarela para colocar os blocos e botão de salvar
screenSize = [1216,900] #800+100, pois 800 é o tamanho da tela do jogo e 100 é da barra
screen = pygame.display.set_mode(screenSize, pygame.SHOWN)
ui_rect = pygame.Rect(0,801,1216,100)
tiles_path = "./imagens/sprites_terrain/32bit/"

f={}
i=1

j=0
k=800

for file in glob.glob(tiles_path+"*.png"):
    loaded_img = pygame.image.load(file)
    f[i] = file, loaded_img, loaded_img.get_rect(), int(file.rpartition('\\')[-1][0])
    f[i][2].x, f[i][2].y = j, k
    i+=1
    j+=32

# criação da matriz que descreverá a fase, cheia de zeros
matrix_columns = int(1216/32)
matrix_lines = int(800/32)
rect_matrix = [[0 for x in range(matrix_columns)] for y in range(matrix_lines)]

# desenha grid para ficar mais fácil de se localizar
def draw_grid():
    grid_size = 32
    for x in range(0, 1216, grid_size):
        for y in range(0, 800, grid_size):
            rect_grid = pygame.Rect(x,y,grid_size,grid_size)
            pygame.draw.rect(screen, "#FFFFFF", rect_grid, 1)
draw_grid()

#with open("./levels_data/area1.json") as infile:
    #area1 = json.load(infile)

def create_grid(area1,f):
    j = 0
    k = 0

    grid_size = 32
    for x in range(0, 800, grid_size):
        for y in range(0, 1216, grid_size):
            for i in range(len(f)):
                if f[i+1][3] == area1[j][k]:
                    screen.blit(f[i+1][1],(y,x))
            k+=1
        k=0
        j+=1

#create_grid(area1,f)

# inicializa com tall_grass selecionado
selected = 1
selected_rect = f[1][1]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[1] < 800: # se a posição for na grid
                val0 = math.ceil(pos[0]/32) - 1 # val0 e val1 vão calcular qual a posição do tile na tela com relação à grid
                val1 = math.ceil(pos[1]/32) - 1

                blank_rect = pygame.Rect(val0*32,val1*32,32,32) # criar e desenhar retêngulo preto para apagar a imagem anterior
                pygame.draw.rect(screen, "#000000", blank_rect)

                screen.blit(selected_rect, (val0*32,val1*32)) # inserir na tela a imagem do tile
                rect_matrix[val1][val0] = selected # insere nas posições val0 e val1 da matriz o código selecionado
            
            else: # se a posição for na barra de tarefas
                for i in range(len(f)): # itera entre os itens da matriz
                    if f[i+1][2].collidepoint(pos): # caso haja colisão entre o retângulo e mouse, muda a tile selecionada
                        selected = f[i+1][3]
                        selected_rect = f[i+1][1]
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                json_array = json.dumps(rect_matrix)
                with open("./levels_data/testing_area/testing_area.json","w") as outfile:
                    outfile.write(json_array)

    pygame.draw.rect(screen, "#fcba03", ui_rect)

    for i in range(len(f)):
        pygame.draw.rect(screen,"#000000", f[i+1][2])
        screen.blit(f[i+1][1],f[i+1][2])
        
    pygame.display.flip()