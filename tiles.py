#pygame was already imported in main, so just import it into this class!
from pygame import *

#make the trap images
trap0_img = image.load('img/garlic.png')
trap0_surf = Surface.convert_alpha(trap0_img)
TRAP0 = transform.scale(trap0_surf, (100,100))

trap1_img = image.load('img/pizzacutter.png')
trap1_surf = Surface.convert_alpha(trap1_img)
TRAP1 = transform.scale(trap1_surf, (100,100))

trap2_img = image.load('img/pepperoni1.png')
trap2_surf = Surface.convert_alpha(trap2_img)
TRAP2 = transform.scale(trap2_surf, (100,100))

trapf_img = image.load('img/pizza-box.png')
trapf_surf = Surface.convert_alpha(trapf_img)
FREE_TRAP = transform.scale(trapf_surf,(100,100))

select_img = image.load('img/gem1Red.png')
select_surf = Surface.convert_alpha(select_img)
SELECT = transform.scale(select_surf,(100,100))

traps=[TRAP0, TRAP1, TRAP2, FREE_TRAP]

trap_cost = [5, 15, 20,0]

class Tile(sprite.Sprite):
    
    def __init__(self,rect):
        super().__init__()
        self.trap = -1
        self.rect = rect
        self.image=None
        self.button = -1
        self.buck_parts = 0
        self.buck_rate = 5
        
    def update(self,window,trap_type):
        if self.button == trap_type:
            window.blit(SELECT,(self.rect.x, self.rect.y))
        if self.trap>=0:
            self.image=traps[self.trap]
            window.blit(self.image,(self.rect.x, self.rect.y))
        

    def buy_trap(self, counter, trap_type):
        if counter.bucks >= trap_cost[trap_type]:
            counter.bucks -= trap_cost[trap_type]
            #if there is already a trap refund it's cost
            if self.trap >= 0:
                counter.bucks += trap_cost[self.trap]  
            self.trap = trap_type

    def increment_bucks(self,counter):
        self.buck_parts += 1
        if self.buck_parts % self.buck_rate == 0:
            counter.bucks += 1
        
