from tkinter import filedialog
import pygame as pg
from os import listdir,mkdir,path,remove

class App:
    def __init__(self) -> None:
        self.WINDOW = pg.display.set_mode((1280,720))
        self.image_pointer = 0
        self.folder_structure = filedialog.askdirectory()
        self.files = [i for i in listdir(self.folder_structure) if i.lower().endswith('jpg') or i.lower().endswith('png')]
        self.deletefiles = []
        self.favfiles = []
        self.move_pointer(0)
        self.is_running = True
        self.fav_image = pg.transform.scale_by(pg.image.load('fav.png'),0.25)
        self.trash_image = pg.transform.scale_by(pg.image.load('trash.png'),0.25)
        
    def move_pointer(self,direction:int):
        self.image_pointer += direction
        if self.image_pointer < 0:
            self.image_pointer = 0
        if self.image_pointer > len(self.files) - 1:
            self.image_pointer = len(self.files) - 1
        if self.files:
            print(self.folder_structure + "\\" + self.files[self.image_pointer])
            img = pg.image.load(self.folder_structure + "\\" + self.files[self.image_pointer])
            imgX, imgY = img.get_size()
            aspect = 1
            if imgX != 1280 and imgY != 720:
                if imgX > 1280:
                    aspect = 1280 / imgX
                if imgY > 720:
                    aspect = 720 / imgY
            self.current_image = pg.transform.scale_by(img,aspect)
        else:
            self.current_image = pg.Surface((1,1))
    def run(self):
        while self.is_running:
            
            self.WINDOW.fill((0,0,0))
            self.WINDOW.blit(self.current_image,(640-(self.current_image.get_width()//2),0))
            if (self.files[self.image_pointer] in self.deletefiles) - (self.files[self.image_pointer] in self.favfiles) == 1:
                self.WINDOW.blit(self.trash_image,(0,0))
            elif (self.files[self.image_pointer] in self.deletefiles) - (self.files[self.image_pointer] in self.favfiles) == -1:
                self.WINDOW.blit(self.fav_image,(0,0))
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.move_pointer(-1)
                    if event.key == pg.K_RIGHT:
                        self.move_pointer(1)
                    if event.key == pg.K_RETURN:
                        if not path.isdir(f'{self.folder_structure}\\deleted\\'):
                            mkdir(f'{self.folder_structure}\\deleted\\')
                        for file in self.deletefiles:
                            with open(f'{self.folder_structure}\\{file}',"rb") as fIn:
                                with open(f'{self.folder_structure}\\deleted\\{file}',"wb") as fOut:
                                    fOut.write(fIn.read())
                            remove(f'{self.folder_structure}\\{file}')
                        if not path.isdir(f'{self.folder_structure}\\fav\\'):
                            mkdir(f'{self.folder_structure}\\fav\\')
                        for file in self.favfiles:
                            with open(f'{self.folder_structure}\\{file}',"rb") as fIn:
                                with open(f'{self.folder_structure}\\fav\\{file}',"wb") as fOut:
                                    fOut.write(fIn.read())
                            remove(f'{self.folder_structure}\\{file}')
                        self.is_running = False
                    if event.key == pg.K_ESCAPE:
                        if self.files[self.image_pointer] in self.deletefiles:
                            self.deletefiles.remove(self.files[self.image_pointer])
                        if self.files[self.image_pointer] not in self.favfiles:
                            self.favfiles.remove(self.files[self.image_pointer])
                    if event.key == pg.K_SPACE:
                        if self.files[self.image_pointer] in self.deletefiles:
                            self.deletefiles.remove(self.files[self.image_pointer])
                        if self.files[self.image_pointer] not in self.favfiles:
                            self.favfiles.append(self.files[self.image_pointer])
                    if event.key == pg.K_BACKSPACE:
                        if self.files[self.image_pointer] in self.favfiles:
                            self.favfiles.remove(self.files[self.image_pointer])
                        if self.files[self.image_pointer] not in self.deletefiles:
                            self.deletefiles.append(self.files[self.image_pointer])
                if event.type == pg.QUIT:
                    pg.quit()
                    self.is_running = False

APP = App()
APP.run()