import pygame
from pygame import *
from random import randint

pygame.init()
#set up clock
clock = time.Clock()
#Set display properties
window_width = 1100
window_height = 600
GAME_WINDOW = display.set_mode((window_width, window_height))
display.set_caption("Attack of the Vampire Pizzas")

#Background Image
background_img = image.load('img/restaurant.jpg')
background_surf = Surface.convert_alpha(background_img)
BACKGROUND = transform.scale(background_surf, (window_width,window_height))

#Gameplay Variables
spawn_rate=160
fps = 60
#slow : 0, hurt : 1, $$$ : 2 
trap_type = 0

#import all the classes!
from vampires import *
from tiles import *
from counters import *

#make the groups
vampire_group=sprite.Group()


#Make the Tile Grid
tile_grid=[]
for row in range(6):
    tile_row=[]
    for column in range(11):
        tile_rect=Rect(100*column, 100*row, 100, 100)
        new_tile=Tile(tile_rect)
        if column == 2:
            new_tile.trap = 3
        tile_row.append(new_tile)
    tile_grid.append(tile_row)
#add the button images
for i in range(3):
    tile_grid[5][2+i].trap = i
    tile_grid[5][2+i].button = i
#make the counter!
counter = Counter(20,60,1)

#Main Gameplay Loop!
game_running = True
while game_running:

    #Check if an event happened!
    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False
        elif event.type == MOUSEBUTTONDOWN:
            coordinates = mouse.get_pos()
            tile_x = coordinates[0] // 100
            tile_y = coordinates[1] // 100
            if tile_y < 5 and tile_x > 1:
                tile_grid[tile_y][tile_x].buy_trap(counter,trap_type)
            #check if they click on buttons!
            elif tile_y ==5 and 5 > tile_x > 1:
                trap_type = tile_x - 2

    
    #Display The Background!
    GAME_WINDOW.blit(BACKGROUND, (0,0))


    #spawn vampires randomly
    if randint(1,spawn_rate)==1:
        Vampire(vampire_group)
        
    for vamp in vampire_group:
        vamp.update(GAME_WINDOW,counter,tile_grid)
        
        

    for row in tile_grid:
        for tile in row:
            tile.update(GAME_WINDOW,trap_type)


    counter.update(GAME_WINDOW,fps)
    
    display.update()
    
    #use clock to manage fps
    clock.tick(fps)

#If not looping, quit the game
pygame.quit()
