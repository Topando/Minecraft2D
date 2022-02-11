import os
import sys
from config import *
import pygame
from main import *
from classes import *
import config
import asyncio
import time


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


def generate_level(pos_x, pos_y=0):
    MAP_LIST.append("*")
    for y in range(20):
        for x in range(17):
            if y == 12:
                print(y)
                Tile('block_of_land', pos_x + x, y - pos_y)
            elif 12 < y < 30:
                Tile('stone_block', pos_x + x, y - pos_y)

