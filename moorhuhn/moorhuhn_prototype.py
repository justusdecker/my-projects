
import pygame as pg
from random import randint
from time import time
pg.mixer.init()
pg.font.init()

"""

TEXT:
    Time left
    Score from chicken fly
swipe to right and left: viewport
Fix collision
music
"""
class Player:
    def __init__(self) -> None:
        self.max_ammo = 5
        self.current_ammo = self.max_ammo
        self.points = 0
    def reload(self):
        return self.max_ammo
    def shoot(self):
        self.current_ammo = (self.current_ammo - 1) if self.current_ammo > 0 else 0

def bubble_sort(array1,array2):
    
    n = len(array1)

    for i in range(n):
        for j in range(0, n - i - 1):

            if array1[j] > array1[j + 1]:
                array1[j], array1[j + 1] = array1[j + 1], array1[j]
                array2[j], array2[j + 1] = array2[j + 1], array2[j]
    return array2

class Moorhuhn:
    WIDTH = 1280
    HEIGHT = 720
    def __init__(self) -> None:
        self.WINDOW = pg.display.set_mode((self.WIDTH,self.HEIGHT))
        self.font = pg.font.Font(pg.font.get_default_font(),self.HEIGHT//10)
        self.delta_time = 0.00000000000001
        self.chicken = [Chicken(self) for i in range(30)]
        self.dead_chickens = []
        self.is_running = True
        self.player = Player()
        self.ammo_surface = pg.transform.scale(pg.image.load("round.png"),(int(self.WIDTH / self.HEIGHT)*60,int(self.WIDTH / self.HEIGHT)*60))
        self.dead_chicken_surface = pg.image.load("yummy.png")
        self.background = pg.transform.scale(pg.image.load("background.png"),(self.WIDTH,self.HEIGHT))
        pg.mouse.set_visible(False)
        self.cross = pg.transform.scale(pg.image.load("cross.png"),(int(self.WIDTH / self.HEIGHT)*100,int(self.WIDTH / self.HEIGHT)*100))
    def update(self):
        last_frame_mouse_press = pg.mouse.get_pressed()[0]
        last_frame_mouse_r_press = pg.mouse.get_pressed()[2]
        while self.is_running:
            t1 = time()
            pg.display.set_caption(f"Points: {self.player.points} DT: {int(self.delta_time*1000)}ms")
            self.WINDOW.blit(self.background,(0,0))
            self.chicken = bubble_sort([chicken.size for chicken in self.chicken],self.chicken)
            mouse_pos = pg.mouse.get_pos()
            mouse_press = pg.mouse.get_pressed()[0]
            mouse_r_press = pg.mouse.get_pressed()[2]
            if not last_frame_mouse_r_press and mouse_r_press:
                pg.mixer.Sound("reload.mp3").play()
                self.player.current_ammo = self.player.max_ammo
            actual_press = not last_frame_mouse_press and mouse_press and self.player.current_ammo > 0
            if actual_press:
                self.player.current_ammo -= 1
                pg.mixer.Sound("shot.mp3").play()
            elif not last_frame_mouse_press and mouse_press and self.player.current_ammo == 0:
                pg.mixer.Sound("no_ammo.mp3").play()
            chicken_hit = False
            for idx,chicken in enumerate(self.chicken):
                if not chicken.is_alive:
                    self.dead_chickens.append([chicken.size,chicken.position,chicken.animation_type]) 
                    self.player.points += int((1 / chicken.size) * 0xff)
                    chicken_hit = True
                if not chicken.is_alive or chicken.out_of_bounce:
                    self.chicken[idx] = Chicken(self)
                chicken.update(actual_press,*mouse_pos)
                self.WINDOW.blit(chicken.surface,chicken.position)
            if chicken_hit:
                pg.mixer.Sound(f"chicken_hit_{randint(0,3)}.mp3").play()
            self.dead_chickens = [chicken for chicken in self.dead_chickens if chicken[1][1] < self.HEIGHT + chicken[0] ]
            for dead_chicken in self.dead_chickens:
                dead_chicken[1][1] += self.delta_time * (self.HEIGHT//2)
                
                self.WINDOW.blit(pg.transform.flip(pg.transform.scale(self.dead_chicken_surface,(dead_chicken[0],dead_chicken[0])),True if dead_chicken[2] == "fly_by_right" else False,False),dead_chicken[1])
                
            for i in range(self.player.current_ammo):
                self.WINDOW.blit(self.ammo_surface,(i*self.ammo_surface.get_width(),self.HEIGHT-self.ammo_surface.get_height()))
            self.WINDOW.blit(self.font.render(f"{self.player.points}",True,(255,255,255)),(0,0))
            self.WINDOW.blit(self.cross,(mouse_pos[0]-(self.cross.get_width()//2),mouse_pos[1]-(self.cross.get_height()//2)))
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    self.is_running = False
            last_frame_mouse_press = mouse_press
            last_frame_mouse_r_press = mouse_r_press
            self.delta_time = time() - t1
        
class Chicken:
    def __init__(self,app:Moorhuhn) -> None:
        destination = randint(2,3)
        self.app = app
        self.is_alive = True
        self.out_of_bounce = False
        
        """
        case 1:
                size = int(app.HEIGHT * .25)
                self.set_type(size,[randint(0,app.WIDTH-size),app.HEIGHT],"peak")
        """
        match destination:
            
            case 2:
                fly_by = ["fly_by_left","fly_by_right"][randint(0,1)]
                size = randint(int(app.HEIGHT * .125),int(app.HEIGHT * .25))
                self.set_type(size,[app.WIDTH if fly_by == "fly_by_left" else -size,randint(0,app.HEIGHT-size)],fly_by)
            case 3:
                fly_by = ["fly_by_left","fly_by_right"][randint(0,1)]
                size = randint(int(app.HEIGHT * .0675),int(app.HEIGHT * .125))
                self.set_type(size,[app.WIDTH if fly_by == "fly_by_left" else -size,randint(0,app.HEIGHT-size)],fly_by)
        self.fly_by_speed = self.size * 1.2
        self.animation_peak_wait = randint(5,10)
        match fly_by:
            case "fly_by_left":
                self.surfaces = pg.transform.scale(pg.image.load("flip.png"),(self.size,self.size)) , pg.transform.scale(pg.image.load("flap.png"),(self.size,self.size))
            case "fly_by_right":
                self.surfaces = pg.transform.flip(pg.transform.scale(pg.image.load("flip.png"),(self.size,self.size)),True,False) ,pg.transform.flip(pg.transform.scale(pg.image.load("flap.png"),(self.size,self.size)),True,False)
        self.surface = self.surfaces[0]
        self.image_toggle = False
        self.last_switch = time() + .5
    def set_type(self,size:int,position:list[int],animation_type:str):
        self.size = size
        self.position = position
        self.animation_type = animation_type
    def get_chicken_hit(self,press,x,y):
        if x > self.position[0] and y > self.position[1] and x < self.position[0] + self.size and y < self.position[1] + self.size and press:
            self.is_alive = False
        
    def update(self,press,x,y):
        self.get_chicken_hit(press,x,y)
        if self.last_switch < time():
            self.last_switch = time() + .5
            self.image_toggle = not self.image_toggle
            self.surface = self.surfaces[self.image_toggle]
        match self.animation_type:
            case "fly_by_left":
                self.position[0] -= self.app.delta_time * self.fly_by_speed
                self.out_of_bounce = self.position[0] < -self.size
            case "fly_by_right":
                self.position[0] += self.app.delta_time * self.fly_by_speed
                self.out_of_bounce = self.position[0] > self.app.WIDTH
if __name__ == "__main__":
    APP = Moorhuhn()
    APP.update()