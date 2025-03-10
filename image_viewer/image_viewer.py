from tkinter.filedialog import askdirectory
import pygame as pg
from os import listdir,mkdir,path,remove
from json import load,dumps
from ctypes import windll
__version__ = "1.3"

class App:
    FPS = 20
    WIDTH = 1280
    HEIGHT = 720
    def __init__(self) -> None:
        self.WINDOW = pg.display.set_mode((self.WIDTH,self.HEIGHT))
        self.CLK = pg.Clock()
        
        self.image_pointer = 0
        
        self.load_config()
        
        self.move_pointer(0)
        self.is_running = True
        
        self.fav_image = pg.transform.scale_by(pg.image.load('fav.png'),0.25)
        self.trash_image = pg.transform.scale_by(pg.image.load('trash.png'),0.25)
    def load_config(self):
        if path.isfile("config.json"):
            with open("config.json") as fIn:
                data = load(fIn)
                self.files = data['files']
                self.favfiles = data['favfiles']
                self.deletefiles = data['deletefiles']
                self.folder_structure = data['folder_structure']
        else:
            self.folder_structure = askdirectory()
            self.files = [i for i in listdir(self.folder_structure) if i.lower().endswith('jpg') or i.lower().endswith('png')]
            self.deletefiles = []
            self.favfiles = []
    def save_config(self):
        with open("config.json","w") as fOut:
            data = {}
            data['files'] = self.files
            data['favfiles'] = self.favfiles
            data['deletefiles'] = self.deletefiles
            data['folder_structure'] = self.folder_structure
            fOut.write(dumps(data))
    def get_file_path_original(self):
        return f"{self.folder_structure}\\{self.files[self.image_pointer]}"
    def move_pointer(self,direction:int):
        
        self.image_pointer += direction
        if self.image_pointer < 0:
            self.image_pointer = 0
        if self.image_pointer > len(self.files) - 1:
            self.image_pointer = len(self.files) - 1
        pg.display.set_caption(f'[{self.image_pointer+1}/{len(self.files)}] - [{self.get_file_path_original()}]')    
        if self.files:
            try:
                img = pg.image.load(self.get_file_path_original())
            except FileNotFoundError as FNFE:
                print(FNFE)
                img = pg.Surface((1,1))
            old_image_x, old_image_y = img.get_size()
            x , y = 1 , 1
            if old_image_x > self.WIDTH or old_image_x < self.WIDTH:
                x = self.WIDTH / old_image_x

            if old_image_y > self.HEIGHT or old_image_y < self.HEIGHT:
                y = self.HEIGHT / old_image_y

            self.current_image = pg.transform.scale_by(img,x if x < y else y)
            print(old_image_x,old_image_y,x if x < y else y)
        else:
            self.current_image = pg.Surface((1,1))
    def msg_box(self):
        msg_result = windll.user32.MessageBoxW(0, "Do you want to save your config?", __name__, 35) #6,7,2 YES, NO ,CANCEL
        if msg_result == 6:
            self.save_config()
        return msg_result == 2
    def get_trash_or_fav(self):
        return (self.files[self.image_pointer] in self.deletefiles) - (self.files[self.image_pointer] in self.favfiles)
    
    def remove_from(self,data:list):
        "Add current Image shortpath to {data} - deletefiles or favfiles"
        if self.files[self.image_pointer] in data:
            data.remove(self.files[self.image_pointer])
            
    def add_to(self,data:list):
        "Add current Image shortpath to {data} - deletefiles or favfiles"
        if self.files[self.image_pointer] not in data:
            data.append(self.files[self.image_pointer])
            
    def copy_paste(self,filepath_copy:str,filepath_paste:str):
        try:
            with open(filepath_copy,"rb") as fIn:
                with open(filepath_paste,"wb") as fOut:
                    fOut.write(fIn.read())
        except FileNotFoundError as FNFE:
            print(FNFE)
            return
        try:
            remove(filepath_copy)
        except WindowsError as WE:
            print(WE)

    def create_folder(self,filepath:str):
        if not path.isdir(filepath):
            mkdir(filepath)
    def run(self):
        while self.is_running:
            self.WINDOW.fill((0,0,0))
            self.WINDOW.blit(self.current_image,(640-(self.current_image.get_width()//2),0))
            
            
            if self.get_trash_or_fav() == 1:
                self.WINDOW.blit(self.trash_image,(0,0))
            elif self.get_trash_or_fav() == -1:
                self.WINDOW.blit(self.fav_image,(0,0))
            self.CLK.tick(20)
            pg.display.update()
            
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.move_pointer(-1)
                        
                    if event.key == pg.K_RIGHT:
                        self.move_pointer(1)
                        
                    if event.key == pg.K_RETURN:
                        
                        self.create_folder(f'{self.folder_structure}\\deleted\\')
                        self.create_folder(f'{self.folder_structure}\\fav\\')
                            
                        for file in self.deletefiles:
                            self.copy_paste(f'{self.folder_structure}\\{file}',f'{self.folder_structure}\\deleted\\{file}')
 
                        for file in self.favfiles:
                            self.copy_paste(f'{self.folder_structure}\\{file}',f'{self.folder_structure}\\fav\\{file}')
                            
                        self.is_running = False
                        
                    if event.key == pg.K_ESCAPE:
                        self.remove_from(self.deletefiles)
                        self.remove_from(self.favfiles)
                        
                    if event.key == pg.K_SPACE:
                        self.remove_from(self.deletefiles)
                        self.add_to(self.favfiles)
                        
                    if event.key == pg.K_BACKSPACE:
                        self.remove_from(self.favfiles)
                        self.add_to(self.deletefiles)
                    if self.is_running:
                        if event.key == pg.K_s and pg.key.get_pressed()[pg.K_LCTRL]:
                            self.save_config()
                        if event.key == pg.K_o and pg.key.get_pressed()[pg.K_LCTRL]:
                            if not self.msg_box():
                                self.load_config()
                            
                        if event.key == pg.K_n and pg.key.get_pressed()[pg.K_LCTRL]:
                            if not self.msg_box():
                                self = App()
                if event.type == pg.QUIT:
                    pg.quit()
                    self.is_running = False

APP = App()
APP.run()