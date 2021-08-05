from pygame import *



class Counter(object):
    def __init__(self, bucks, rate, bucks_per,lives=3):
        #how many loops have we gone through
        self.loop_count = 0
        self.font = font.Font('img/pizza_font.ttf',30)
        #Starting $$$
        self.bucks = bucks
        #how many loops before we get more $$$
        self.rate = rate
        #how many bucks per rate
        self.bucks_per = bucks_per
        #where to draw bucks
        self.buck_rect = Rect(1030,540,50,50)
        #lives stats
        self.lives_lost = 0
        self.lives = lives
        #where to draw lives
        self.lives_rect = Rect(930,540,50,50)
        #timer
        self.time_left= 180
        self.timer_rect = Rect(830,540,50,50)
        
    def update(self,window,fps):
        self.loop_count += 1
        if self.loop_count % self.rate == 0:
            self.bucks += self.bucks_per
        if self.loop_count % fps == 0:
            self.time_left -= 1
        self.draw_counters(window)
        if self.lives_lost >= self.lives:
            quit()

    def draw_counters(self,window):
        bucks_surf = self.font.render(str(self.bucks),True,(255,255,255))
        window.blit(bucks_surf,self.buck_rect)
        lives_surf = self.font.render(f"{self.lives_lost} / {self.lives}",True,(255,0,0))
        window.blit(lives_surf,self.lives_rect)
        timer_surf = self.font.render(str(self.time_left),True,(255,255,255))
        window.blit(timer_surf,self.timer_rect)
