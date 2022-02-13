import os
import sys
from config import *
import pygame
from main import *
from classes import *
import config
import asyncio
import time
import random


def add_new_player():
    return Player(8, 10, "player_right")


def load_image(name, colorkey=None):
    fullname = os.path.join('data/', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def change_image(new_player, image):
    player_img = image_player_right(image)
    player_img = pygame.transform.scale(player_img, (WIDTH // 16, HEIGHT // 4))
    new_player.image = player_img


def image_player_right(image):
    return load_image(models[image])


def image_texture(texture_imgage):
    return load_image(textures[texture_imgage])


def create_sprite_group():
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    return all_sprites, tiles_group, player_group


def generate_level(pos_x, change_Y, pos_y=0, place="right"):
    if place == "right":
        MAP_LIST.append("*")
    else:
        LEFT_MAP.append("*")
    for y in range(12, 20):
        for x in range(17):
            if y == 12:
                print(y)
                Tile('block_of_land', pos_x + x, y - pos_y - change_Y)
            elif 12 < y < 15:
                Tile(blocks_spawn_y_13(), pos_x + x, y - pos_y - change_Y)
            elif 14 < y < 20:
                Tile(blocks_spawn_y_15_19(), pos_x + x, y - pos_y - change_Y)


def blocks_spawn_y_13():
    if random.randint(0, 1) == 1:
        return "stone_block"
    return "ground_block"


def blocks_spawn_y_15_19():
    y = random.randint(0, 10)
    if y <= 5:
        return "stone_block"
    elif 5 < y < 7:
        return "ground_block"
    elif y == 9:
        return "gold_block"
    return "block_of_iron"


def setting_map_list(chunk):
    global MAP_LIST
    global LEFT_MAP
    if chunk > 0:
        for i in range(len(MAP_LIST)):
            if i != chunk and MAP_LIST[i] == "@":
                MAP_LIST[i] = "*"
        for i in range(len(LEFT_MAP)):
            LEFT_MAP[i] = "*"
    else:
        for i in range(len(MAP_LIST)):
            MAP_LIST[i] = "*"
        for i in range(len(LEFT_MAP)):
            if -i != chunk and LEFT_MAP[i] == "@":
                LEFT_MAP[i] = "*"


def check_down(player, sprite):
    if sprite.rect.y == player.rect.y + player.rect.size[1] and sprite.rect.x == player.rect.x:
        return True
