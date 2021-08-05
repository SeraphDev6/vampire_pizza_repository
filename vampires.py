#pygame was already imported in main, so just import it into this class!
from pygame import *
from random import randint

pizza_img = image.load('img/vampire.png')
pizza_surf = Surface.convert_alpha(pizza_img)
VAMPIRE = transform.scale(pizza_surf, (100,100))

normal_speed = 2
max_health=300
hurt_damage = 1


class Vampire(sprite.Sprite):
    def __init__(self,group):
        super().__init__()
        #Set the Vampire's speed!
        self.speed = normal_speed
        #Set the vampire health
        self.health = max_health
        #Which lane is the vampire in?
        self.lane = randint(0,4)
        #add the vampire to the group
        group.add(self)
        self.image = VAMPIRE.copy()
        #set the y position based on lane
        y = 50 + 100 * self.lane
        self.rect = self.image.get_rect(center=(1100,y))

    def update(self,window,counter,tile_grid):
        self.rect.x -= self.speed
        self.speed = normal_speed
        window.blit(self.image,(self.rect.x, self.rect.y))
        self.left= self.rect.x // 100
        self.right=(self.rect.x + self.rect.width) // 100
        #check Collision
        if self.left > 1:
            if tile_grid[self.lane][self.left].trap >= 0:
                self.Collide(tile_grid[self.lane][self.left],counter)
            if self.right < 10 and tile_grid[self.lane][self.right].trap >= 0:
                self.Collide(tile_grid[self.lane][self.right],counter)
        else:
            self.kill()
            counter.lives_lost+=1
        #draw health bar
        if self.health < max_health:
            draw.rect(self.image,(200,200,200),(0,90,100,10))
            draw.rect(self.image,(255,0,0),(0,91,100*self.health/max_health,8))
        if self.health <= 0:
             self.kill()
             
    def Collide(self,tile,counter):
        if tile.trap == 0: #slow
            self.speed = normal_speed//2
        elif tile.trap == 1: #hurt
            self.health -= hurt_damage
        elif tile.trap == 2:
            tile.increment_bucks(counter)
        elif tile.trap == 3:
            self.kill()
            tile.trap = -1
            
