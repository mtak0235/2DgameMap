import pygame as pg
import math 
class Player(pg.sprite.Sprite):
    def __init__(self, image, position):
        pg.sprite.Sprite.__init__(self)
        self.user_src_image = pg.image.load(image)
        self.user_src_image = pg.transform.scale(self.user_src_image, (40, 40))
        self.user_position = position
        self.user_speed = 0
        self.user_rotation = 0
        self.user_rotation_speed = 0
        
        self.rect = self.user_src_image.get_rect()

    def update(self):
        self.user_rotation += self.user_rotation_speed
        x,y = self.user_position
        rad = self.user_rotation * math.pi / 180
        x += -self.user_speed * math.sin(rad)
        y += -self.user_speed *math.cos(rad)
        self.user_position = (x,y)

        self.image = pg.transform.rotate(self.user_src_image, self.user_rotation)
        self.rect = self.image.get_rect()
        self.rect.center = self.user_position