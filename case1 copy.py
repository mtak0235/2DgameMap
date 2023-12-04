import pygame as pg
import math
from os import path
import sys
from player import Player
imagefolder = path.join(path.dirname(__file__), 'img')
screen_width = 1024 #x
screen_height = 768 #y
TILESIZE = 64
pg.init()
screen = pg.display.set_mode((screen_width, screen_height))
screen_rect = screen.get_rect()
clock = pg.time.Clock()
pg.key.set_repeat(1,1) # todo
font = pg.font.Font('d2.ttf', 30) #todo

bgm = pg.mixer.Sound("bgm.mp3")
bgm.play(-1)

class Player(pg.sprite.Sprite):
    user_size = 40
    def __init__(self, image, position):
        pg.sprite.Sprite.__init__(self)
        self.user_image = pg.image.load(image)
        self.user_image = pg.transform.scale(self.user_image, (self.user_size, self.user_size))
        self.user_position = position
        self.user_speed = 0
        self.user_rotation = 0
        self.user_rotation_speed = 0
        
        self.rect = self.user_image.get_rect()

        self.lev = 0
        self.levimgs = []
        lev1 = pg.image.load(path.join(imagefolder,"player1.png"))
        lev1 = pg.transform.scale(lev1, (self.user_size, self.user_size))
        self.levimgs.append(lev1)
        lev2 = pg.image.load(path.join(imagefolder,"player2.webp"))
        lev2 = pg.transform.scale(lev2, (self.user_size, self.user_size))
        self.levimgs.append(lev2)
        lev3 = pg.image.load(path.join(imagefolder,"player3.webp"))
        lev3 = pg.transform.scale(lev3, (self.user_size, self.user_size))
        self.levimgs.append(lev3)
        lev4 = pg.image.load(path.join(imagefolder,"player4.webp"))
        lev4 = pg.transform.scale(lev4, (self.user_size, self.user_size))
        self.levimgs.append(lev4)

    def update(self):
        self.user_rotation += self.user_rotation_speed
        x,y = self.user_position
        rad = self.user_rotation * math.pi / 180
        x += -self.user_speed * math.sin(rad)
        y += -self.user_speed *math.cos(rad)
        self.user_position = (x,y)

        self.image = pg.transform.rotate(self.user_image, self.user_rotation)
        self.rect = self.image.get_rect()
        self.rect.center = self.user_position

player = Player(path.join(imagefolder, "player.webp"), screen_rect.center)
player_group = pg.sprite.RenderPlain(player)

#color 
black_color = (0,0,0)
powder_blue_color = (102,255,255)

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
item_group = pg.sprite.RenderPlain()#todo
for row in range(len(map_data)):
    for col in range(len(map_data[0])):
        if map_data[row][col] == 's':
            boundary = Wall(row, col) #todo
            map_group.add(boundary)
        if map_data[row][col] == 'i':
            item = Item(row, col) #todo
            item_group.add(item)
    

background = pg.image.load(path.join(imagefolder,"background.png"))
background = pg.transform.scale(background, (screen.get_width(), screen.get_height()))
screen.blit(background, (0, 0))

limit_time = 5000000000000000
target_level = len(player.levimgs)
success_img = pg.image.load(path.join(imagefolder, "success.png"))
fail_img = pg.image.load(path.join(imagefolder, "fail.png"))
while True: #todo
    deltat = clock.tick(60)
    time_text = font.render(str(pg.time.get_ticks() // 1000) + "  초", True, (0, 0, 0), (255, 255, 255))
    if pg.time.get_ticks() // 1000 >= limit_time:
        if player.lev >= target_level:
            screen.blit(success_img, screen_rect.center)
        else:
            screen.blit(fail_img, screen_rect.center)
        
        pg.display.update()
        pg.time.wait(3000)
        break
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()
        
        # player 움직임
        keys = pg.key.get_pressed()
        if keys:
            if e.type == pg.KEYDOWN:
                if keys[pg.K_RIGHT]:
                    player.user_speed = 0
                    player.user_rotation_speed = -5
                elif keys[pg.K_LEFT]:
                    player.user_speed = 0
                    player.user_rotation_speed = 5
                elif keys[pg.K_UP]:
                    player.user_speed = deltat * 0.1
                elif keys[pg.K_DOWN]:
                    player.user_speed = deltat * -0.1
            elif e.type == pg.KEYUP:
                player.user_speed = 0
                player.user_rotation_speed = 0
    if 0 > player.user_position[0]:
        player.user_position= (0, player.user_position[1])
    elif player.user_position[0] > screen.get_width():
        player.user_position= (screen.get_width(), player.user_position[1])
    if 0 > player.user_position[1]:
        player.user_position= (player.user_position[0], 0)
    elif player.user_position[1] > screen.get_height():
        player.user_position= (player.user_position[0], screen.get_height())
        
    if pg.sprite.spritecollide(player, item_group, True): 
        player.user_image = player.levimgs[player.lev]
        player.lev += 1
        player.lev = player.lev % len(player.levimgs) 
        player.speed = 0
    item_group.update()


    if pg.sprite.spritecollide(player, map_group, False):
        player.user_speed *= -1
        player_group.update()
        player.user_speed = 0
    # map_group.update()

    player_group.update()
    map_group.clear(screen, background)
    player_group.clear(screen, background)
    item_group.clear(screen, background)

    screen.blit(background, (0, 0))
    map_group.draw(screen)
    player_group.draw(screen)
    item_group.draw(screen)
    screen.blit(time_text, (screen_width*0.15, screen_height*0.15))
    pg.display.flip()
pg.quit()