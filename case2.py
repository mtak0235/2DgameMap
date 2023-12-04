import sys
import pygame as pg
from pygame.locals import *
from player import Player
from item import Item
from wall import Wall
from field import Field
import random

# 프로그램 초기화
pg.init()

#기본 객체 생성
screen = pg.display.set_mode((1024, 768))
clock = pg.time.Clock()

# 기본 설정
pg.key.set_repeat(1,1)

#음악 설정
bgm = pg.mixer.Sound("bgm.mp3")
bgm.play()

rect = screen.get_rect()
player = Player("player.webp", rect.center)
player_group = pg.sprite.RenderPlain(player)

# 맵 가져오기
map_data = []
with open('map.txt', 'r') as file:
    for line in file:
        map_data.append(line.strip('\n'))

map_group = pg.sprite.RenderPlain()
# field_group = pg.sprite.RenderPlain()
for row in range(len(map_data)):
    for col in range(len(map_data[0])):
        if map_data[row][col] == 's':
            boundary = Wall(col, row)
            map_group.add(boundary)
        elif map_data[row][col] == 'g':
            field = Field(col, row)
            # field_group.add(field)

# item 가져오기
items = []
items.append(Item(3,4))
items.append(Item(4,4))
items.append(Item(5,5))
# for i in range(10):
#     for row in range(random.randint(0, len(map_data))):
#         for col in range(random.randint(0, len(map_data[0]))):
#             if map_data[row][col] != 's':
#                 item = Item(col, row)
#                 items.append(item)
item_group = pg.sprite.RenderPlain(*items)

# 배경화면 뿌리기
background = pg.image.load("background.png")
background = pg.transform.scale(background, (screen.get_width(), screen.get_height()))
screen.blit(background, (0, 0))
TILESIZE = 64
lev = 0
levimg = []
lev1 = pg.image.load("player1.png")
lev1 = pg.transform.scale(lev1, (TILESIZE, TILESIZE))
levimg.append(lev1)
lev2 = pg.image.load("player2.webp")
lev2 = pg.transform.scale(lev2, (TILESIZE, TILESIZE))
levimg.append(lev2)
lev3 = pg.image.load("player3.webp")
lev3 = pg.transform.scale(lev3, (TILESIZE, TILESIZE))
levimg.append(lev3)
lev4 = pg.image.load("player4.webp")
lev4 = pg.transform.scale(lev4, (TILESIZE, TILESIZE))
levimg.append(lev4)


while True:
    deltat = clock.tick(60)
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
        
        if pg.sprite.spritecollide(player, item_group, True):
            player.image = levimg[lev]
            lev += 1
            lev = lev % len(levimg)
            player.speed = 0
            player_group.update()

        if pg.sprite.spritecollide(player, map_group, False):
            player.user_speed *= -1
            player_group.update()
            player.user_speed = 0


    player_group.update()
    collisions= pg.sprite.spritecollide(player, item_group, False)
    item_group.update(collisions)
    
    map_group.clear(screen, background)
    player_group.clear(screen, background)
    item_group.clear(screen, background)

    map_group.draw(screen)
    player_group.draw(screen)
    item_group.draw(screen)
    pg.display.flip()
