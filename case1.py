import pygame as pg
import math
from os import path
imagefolder = path.join(path.dirname(__file__), 'img')
screen_width = 800 #x
screen_height = 600 #y
pg.init()
screen = pg.display.set_mode((screen_width, screen_height))
screen_rect = screen.get_rect()
clock = pg.time.Clock()
running = True

class Player(pg.sprite.Sprite):
    def __init__(self, image, position):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image)
        self.image = pg.transform.scale(self.image, (40, 40))
        self.position = position
        self.speed = 0
        self.rotation = 0
        self.rotataion_speed = 0
        self.rect = self.image.get_rect()
        self.rect.center = position
    

    def update(self):
        self.rotation += self.rotataion_speed
        x , y = self.position # (15, 80)
        rad = self.rotation * math.pi / 180
        x += -self.speed * math.sin(rad)
        y += -self.speed * math.cos(rad)
        self.position = (x, y)
        self.image = pg.transform.rotate(self.image, self.rotation)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

player = Player(path.join(imagefolder, "player.webp"), screen_rect.center)
player_group = pg.sprite.RenderPlain(player)
# player_group.add(player)

#color 
black_color = (0,0,0)
powder_blue_color = (102,255,255)
TILESIZE = 64
class Wall(pg.sprite.Sprite):
    def __init__(self, row, col):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(path.join(imagefolder,"brick.jpg"))
        self.image = pg.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.grid_x = col * TILESIZE
        self.grid_y = row * TILESIZE
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y
class Item(pg.sprite.Sprite):
    def __init__(self, row, col):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(path.join(imagefolder,"item.jpg"))
        self.image = pg.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.grid_x = col * TILESIZE
        self.grid_y = row * TILESIZE
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y
map_data = []
with open('map.txt','r') as file:
    for line in file:
        map_data.append(line.strip('\n'))
map_group = pg.sprite.RenderPlain()
for row in range(len(map_data)):
    for col in range(len(map_data[0])):
        if map_data[row][col] == 's':
            boundary = Wall(col, row) #todo
            map_group.add(boundary)
    
import random
items = []
items.append(Item(3,4))
items.append(Item(4,4))
items.append(Item(5,5))
# for i in range(5):
#     for row in range(random.randint(0, len(map_data))):
#         for col in range(random.randint(0, len(map_data[0]))):
#             if map_data[row][col] != 's':
#                 item = Item(row, col)
#                 items.append(item)
item_group = pg.sprite.RenderPlain(*items)

background = pg.image.load(path.join(imagefolder,"background.png"))
background = pg.transform.scale(background, (screen.get_width(), screen.get_height()))
screen.blit(background, (0, 0))

lev = 0
levimg = []
lev1 = pg.image.load(path.join(imagefolder,"player1.png"))
lev1 = pg.transform.scale(lev1, (TILESIZE, TILESIZE))
levimg.append(lev1)
lev2 = pg.image.load(path.join(imagefolder,"player2.webp"))
lev2 = pg.transform.scale(lev2, (TILESIZE, TILESIZE))
levimg.append(lev2)
lev3 = pg.image.load(path.join(imagefolder,"player3.webp"))
lev3 = pg.transform.scale(lev3, (TILESIZE, TILESIZE))
levimg.append(lev3)
lev4 = pg.image.load(path.join(imagefolder,"player4.webp"))
lev4 = pg.transform.scale(lev4, (TILESIZE, TILESIZE))
levimg.append(lev4)

while running:#todo
    fps = clock.tick(100)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False#todo
        key_event = pg.key.get_pressed()
        if key_event:
            if event.type == pg.KEYDOWN:
                if key_event[pg.K_LEFT]:
                    player.speed = 0
                    player.rotataion_speed = 5
                if key_event[pg.K_RIGHT]:
                    player.speed = 0
                    player.rotataion_speed = -5
                if key_event[pg.K_UP]:
                    player.speed = fps * 0.1
                if key_event[pg.K_DOWN]:
                    player.speed = fps * -0.1
            elif event.type == pg.KEYUP:
                player.speed = 0
                player.rotataion_speed = 0
        player_group.update()
    
    if pg.sprite.spritecollide(player, item_group, True):
        player.image = levimg[lev]
        lev += 1
        lev = lev % len(levimg)
        # player.speed = 0
    item_group.update()
    
    
    if pg.sprite.spritecollide(player, map_group, False):
        player.speed *= -1
        player_group.update()
        # player.speed = 0
    map_group.update()


    # map_group.clear(screen, background)
    # item_group.clear(screen, background)
    player_group.clear(screen, background)

    player_group.draw(screen)
    map_group.draw(screen)
    item_group.draw(screen)
    pg.display.flip()
pg.quit()