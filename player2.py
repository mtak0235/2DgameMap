import pygame as pg
import math 
class Player(pg.sprite.Sprite):
    def __init__(self, image, position):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image)
        self.image = pg.transform.scale(self.image, (40, 40))
        self.position = position
        self.speed = 0
        self.rotation = 0
        self.rotation_speed = 0
        
        self.rect = self.image.get_rect()

    def update(self):
        self.rotation += self.rotation_speed
        x,y = self.position
        rad = self.rotation * math.pi / 180
        x += -self.speed * math.sin(rad)
        y += -self.speed *math.cos(rad)
        self.position = (x,y)

        self.image = pg.transform.rotate(self.image, self.rotation)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
# class Player(pg.sprite.Sprite):
#     def __init__(self, image, position):
#         pg.sprite.Sprite.__init__(self)
#         self.image = pg.image.load(image)
#         self.image = pg.transform.scale(self.image, (40, 40))
#         self.position = position
#         self.speed = 0
#         self.rotation = 0
#         self.rotation_speed = 0
#         self.rect = self.image.get_rect()
#         self.rect.center = position
    

#     def update(self):
#         self.rotation += self.rotation_speed
#         x , y = self.position # (15, 80)
#         rad = self.rotation * math.pi / 180
#         x += -self.speed * math.sin(rad)
#         y += -self.speed * math.cos(rad)
#         self.position = (x, y)
#         self.image = pg.transform.rotate(self.image, self.rotation)
#         self.rect = self.image.get_rect()
#         self.rect.center = self.position