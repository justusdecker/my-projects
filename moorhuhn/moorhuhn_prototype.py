
import pygame as pg
from random import randint
from time import time
pg.mixer.init()
pg.font.init()
__version__ = "1.1"
FOLDER = "bin\\"
"""
(c)2025 Justus Decker - The Moorhuhn Project

All sprites are created in Krita with my mouse
The music was created in LMMS
"""
"""
Method to functions
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
        self.highscores = []
        self.WINDOW = pg.display.set_mode((self.WIDTH,self.HEIGHT))
        self.CLOCK = pg.Clock()
        self.delta_time = 0
        self.is_running = True
        self.state = 0
        self.load_graphics()
        pg.mixer.music.load(FOLDER + "bgm.mp3")
        pg.mouse.set_visible(False)
        
    def load_graphics(self):
        self.text = pg.image.load(FOLDER + "nums.png")
        self.text = pg.transform.scale(self.text, (int(self.WIDTH / self.HEIGHT)*600,int(self.WIDTH / self.HEIGHT)*60))
        self.little_chicken_left = pg.transform.scale(pg.image.load(FOLDER + "flip.png"),(self.HEIGHT * .125,self.HEIGHT * .125)) , pg.transform.scale(pg.image.load(FOLDER + "flap.png"),(self.HEIGHT * .125,self.HEIGHT * .125))
        self.medium_chicken_left = pg.transform.scale(pg.image.load(FOLDER + "flip.png"),(self.HEIGHT * .25,self.HEIGHT * .25)) , pg.transform.scale(pg.image.load(FOLDER + "flap.png"),(self.HEIGHT * .25,self.HEIGHT * .25))
        self.little_chicken_right = pg.transform.flip(pg.transform.scale(pg.image.load(FOLDER + "flip.png"),(self.HEIGHT * .125,self.HEIGHT * .125)),True,False) ,pg.transform.flip(pg.transform.scale(pg.image.load(FOLDER + "flap.png"),(self.HEIGHT * .125,self.HEIGHT * .125)),True,False)
        self.medium_chicken_right = pg.transform.flip(pg.transform.scale(pg.image.load(FOLDER + "flip.png"),(self.HEIGHT * .25,self.HEIGHT * .25)),True,False) ,pg.transform.flip(pg.transform.scale(pg.image.load(FOLDER + "flap.png"),(self.HEIGHT * .25,self.HEIGHT * .25)),True,False)
        self.combo_surface = pg.transform.scale(pg.image.load(FOLDER + "combo.png"),(self.HEIGHT * .125,self.HEIGHT * .125))
        self.ammo_surface = pg.transform.scale(pg.image.load(FOLDER + "round.png"),(int(self.WIDTH / self.HEIGHT)*60,int(self.WIDTH / self.HEIGHT)*60))
        self.dead_chicken_surface = pg.image.load(FOLDER + "yummy.png")
        background = pg.transform.scale(pg.image.load(FOLDER + "background.png"),(self.WIDTH,self.HEIGHT))
        self.background = pg.Surface(background.get_size())
        self.background.blit(background,(0,0))
        self.cross = pg.transform.scale(pg.image.load(FOLDER + "cross.png"),(int(self.WIDTH / self.HEIGHT)*100,int(self.WIDTH / self.HEIGHT)*100))
    
    def render_numbers(self,text:str,position: list | tuple):
        char_size = self.text.get_width() // 10

        for idx,i in enumerate(text):
            if i not in "0123456789": continue
            draw_pos = (idx*char_size) + position[0],position[1]
            rect = (
            (char_size)*int(i),
            0,
            char_size,
            self.text.get_height()
            )
            self.WINDOW.blit(self.text,draw_pos,rect)
    def get_highscore_zeros(self,text:str) -> str:
        text = str(text)
        return ("0"*(8-len(text))) + text
    def get_double_zero(self,text:str) -> str:
        text = str(text)
        return text if len(text) == 2 else "0" + text
    def convert_time(self):
        return f"{self.get_double_zero(int(self.timer//60))}:{self.get_double_zero(int(self.timer%60))}"
    def set_default_game_vars(self):
        self.player = Player()
        self.chicken = [Chicken(self) for i in range(30)]
        self.dead_chickens = []
        self.last_frame_mouse_press = pg.mouse.get_pressed()[0]
        self.last_frame_mouse_r_press = pg.mouse.get_pressed()[2]
        self.last_chicken_hit = False
        self.last_actual_press = False
        self.combo = 1
        self.timer = 70
        pg.mixer.music.play()
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                self.is_running = False
            
    def run(self):
        while self.is_running:
            t1 = time()
            pg.display.set_caption(f"DT: {int(self.delta_time*1000)}ms")
            self.CLOCK.tick(60)
            
            match self.state:
                case 0:
                    self.update_menu()
                case 1:
                    self.update_game()
            pg.display.update()
            self.check_events()
            self.delta_time = time() - t1
            
            
    def update_menu(self):
        self.WINDOW.fill(pg.Color("#242424"))
        for idx,score in enumerate(self.highscores):
            self.render_numbers(f"{self.get_highscore_zeros(score)}",((self.WIDTH//2) - (int(self.WIDTH / self.HEIGHT)*60*4),(int(self.WIDTH / self.HEIGHT)*60)*idx))
        if pg.mouse.get_pressed()[0]:
            self.set_default_game_vars()
            self.state = 1
    
    def update_game(self):
        self.WINDOW.blit(self.background,(0,0))
        
        self.chicken = bubble_sort([chicken.size for chicken in self.chicken],self.chicken)
        
        mouse_pos = pg.mouse.get_pos()
        mouse_press = pg.mouse.get_pressed()[0]
        mouse_r_press = pg.mouse.get_pressed()[2]
        
        failed_press = not self.last_frame_mouse_press and mouse_press and self.player.current_ammo == 0
        actual_press = not self.last_frame_mouse_press and mouse_press and self.player.current_ammo > 0

        chicken_hit = self.draw_chicken_alive(actual_press,mouse_pos)
        
        self.combo += chicken_hit
        
        if not actual_press and not self.last_frame_mouse_r_press and mouse_r_press and self.player.max_ammo != self.player.current_ammo:
            #$Player reloading
            pg.mixer.Sound(FOLDER + "reload.mp3").play()
            self.player.current_ammo = self.player.max_ammo
        
        if actual_press:
            #$Player shoot
            self.player.current_ammo -= 1
            pg.mixer.Sound(FOLDER + "shot.mp3").play()
        elif not self.last_frame_mouse_press and mouse_press and self.player.current_ammo == 0:
            #$Player shoot but no ammo
            pg.mixer.Sound(FOLDER + "no_ammo.mp3").play()
        
        if chicken_hit:
            pg.mixer.Sound(FOLDER + f"chicken_hit_{randint(0,3)}.mp3").play()
        if chicken_hit > 1:
            pg.mixer.Sound(FOLDER + "row.mp3").play()
        
        self.draw_chicken_dead()
        
        self.draw_ammo()
        #UI
        self.render_numbers(f"{self.player.points}",(0,0))
        self.render_numbers(f"{self.convert_time()}",(self.WIDTH-((self.text.get_width()//10)*5),0))
        self.WINDOW.blit(self.cross,(mouse_pos[0]-(self.cross.get_width()//2),mouse_pos[1]-(self.cross.get_height()//2)))
        
        #COMBO Stuff
        if self.last_actual_press and chicken_hit: 
            self.last_chicken_hit = chicken_hit
        elif self.last_actual_press and not chicken_hit:
            self.last_chicken_hit = 0
            self.combo = 0
        elif failed_press:
            self.combo = 0
            self.last_chicken_hit = 0
        
        if self.combo > 2 and self.last_actual_press and chicken_hit:
            pg.mixer.Sound(FOLDER + "combo.mp3").play()
        
        
        self.last_actual_press = actual_press
        self.last_frame_mouse_press = mouse_press
        self.last_frame_mouse_r_press = mouse_r_press
        #If the timer reaches 0 return to menu and save new highscore
        self.timer -= self.delta_time
        if self.timer <= 0:
            self.highscores.append(self.player.points)
            self.state = 0
    def draw_chicken_dead(self):
        self.dead_chickens = [chicken for chicken in self.dead_chickens if chicken[1][1] < self.HEIGHT + chicken[0]]
        
        for dead_chicken in self.dead_chickens:
            dead_chicken[1][1] += self.delta_time * (self.HEIGHT//2)          
            self.WINDOW.blit(pg.transform.flip(pg.transform.scale(self.dead_chicken_surface,(dead_chicken[0],dead_chicken[0])),True if dead_chicken[2] == "fly_by_right" else False,False),dead_chicken[1])

            dead_chicken[3][1] -= self.delta_time * (self.HEIGHT//2)
            self.render_numbers(f"{dead_chicken[5]}",dead_chicken[3])
            
    def draw_chicken_alive(self,actual_press,mouse_pos):
        chicken_hit = 0
        for idx,chicken in enumerate(self.chicken):
            if not chicken.is_alive:
                points = (self.combo * (10 if chicken.destination == 2 else 5)) if self.combo > 0 else (10 if chicken.destination == 2 else 5)
                self.player.points += points
                chicken_hit += 1
                self.dead_chickens.append([chicken.size,chicken.position,chicken.animation_type,chicken.position.copy(),self.last_chicken_hit,points])
                
            if not chicken.is_alive or chicken.out_of_bounce: self.chicken[idx].reset()
            
            chicken.update(actual_press,*mouse_pos)
            self.WINDOW.blit(chicken.surface,chicken.position)
        return chicken_hit
    
    def draw_ammo(self):
        for i in range(self.player.current_ammo):
            self.WINDOW.blit(self.ammo_surface,(i*self.ammo_surface.get_width(),self.HEIGHT-self.ammo_surface.get_height()))
        

class Chicken:
    def __init__(self,app:Moorhuhn) -> None:
        self.app = app
        self.reset()
        
    def reset(self):
        self.image_toggle = False
        self.destination = randint(2,3)
        self.is_alive = True
        self.out_of_bounce = False
        match self.destination:
            
            case 2:
                fly_by = ["fly_by_left","fly_by_right"][randint(0,1)]
                size = int(self.app.HEIGHT * .125)
                self.set_type(size,[randint(self.app.WIDTH,self.app.WIDTH+(size*2)) if fly_by == "fly_by_left" else -randint(size,size*5),randint(0,self.app.HEIGHT-size)],fly_by)

            case 3:
                fly_by = ["fly_by_left","fly_by_right"][randint(0,1)]
                size = int(self.app.HEIGHT * .25)
                self.set_type(size,[randint(self.app.WIDTH,self.app.WIDTH+(size*2)) if fly_by == "fly_by_left" else -randint(size,size*5),randint(0,self.app.HEIGHT-size)],fly_by)
        self.get_image()

        self.fly_by_speed = self.size * 1.2
        
        self.last_switch = time() + .5
    def get_image(self):
        if self.destination == 2 and self.animation_type == "fly_by_left":
            self.surface = self.app.little_chicken_left[self.image_toggle]
        elif self.destination == 2 and self.animation_type == "fly_by_right":
            self.surface = self.app.little_chicken_right[self.image_toggle]
        elif self.destination == 3 and self.animation_type == "fly_by_left":
            self.surface = self.app.medium_chicken_left[self.image_toggle]
        elif self.destination == 3 and self.animation_type == "fly_by_right":
            self.surface = self.app.medium_chicken_right[self.image_toggle]
    def set_type(self,size:int,position:list[int],animation_type:str):
        self.size = size
        self.position = position
        self.animation_type = animation_type
    def get_chicken_hit(self,press,x,y):
        if x > self.position[0] and y > self.position[1] and x < self.position[0] + self.size and y < self.position[1] + self.size and press:
            mouse = pg.mask.from_surface(pg.Surface((1,1)))
            me = pg.mask.from_surface(self.surface)
            if me.overlap(mouse,(x-self.position[0],y-self.position[1])):
                self.is_alive = False
        
    def update(self,press,x,y):
        self.get_chicken_hit(press,x,y)
        if self.last_switch < time():
            self.last_switch = time() + .5
            self.image_toggle = not self.image_toggle
            self.get_image()
        match self.animation_type:
            case "fly_by_left":
                self.position[0] -= self.app.delta_time * self.fly_by_speed
                self.out_of_bounce = self.position[0] < -self.size
            case "fly_by_right":
                self.position[0] += self.app.delta_time * self.fly_by_speed
                self.out_of_bounce = self.position[0] > self.app.WIDTH
if __name__ == "__main__":
    APP = Moorhuhn()
    APP.run()