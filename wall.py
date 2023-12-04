import pygame as pg
from const import TILESIZE
from os import path
imagefolder = path.join(path.dirname(__file__), 'img')

class Wall(pg.sprite.Sprite):
    def __init__(self, col, row):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(path.join(imagefolder,"brick.jpg"))
        self.image = pg.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.grid_x = col * TILESIZE
        self.grid_y = row * TILESIZE
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y