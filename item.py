import pygame as pg
from const import TILESIZE
from os import path
imagefolder = path.join(path.dirname(__file__), 'img')

class Item(pg.sprite.Sprite):
    def __init__(self, col, row):
        pg.sprite.Sprite.__init__(self)
        self.user_image_normal = pg.image.load(path.join(imagefolder,"item.jpg"))
        self.user_image_normal = pg.transform.scale(self.user_image_normal, (TILESIZE, TILESIZE))
        self.user_image_hit = pg.image.load(path.join(imagefolder,"item.jpg"))
        self.user_image_hit = pg.transform.scale(self.user_image_hit, (TILESIZE, TILESIZE))
        self.image = self.user_image_normal
        self.grid_x = col * TILESIZE
        self.grid_y = row * TILESIZE
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

    def update(self, hit_list):
        if self in hit_list:
            self.image = self.user_image_hit
        else:
            self.image = self.user_image_normal
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y
    

    # def update(self, hit_list):
    #     if self in hit_list:
    #         self.image = self.user_image_hit
    #     else:
    #         self.image = self.user_image_normal
    #     self.rect = self.image.get_rect()
    #     self.rect.center = self.user_position