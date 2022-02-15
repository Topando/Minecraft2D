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
    for y in range(12, 22):
        for x in range(17):
            if y == 12:
                Tile('block_of_land', pos_x + x, y - pos_y - change_Y)
            elif 12 < y < 15:
                Tile(blocks_spawn_y_13(), pos_x + x, y - pos_y - change_Y)
            elif 14 < y < 19:
                Tile(blocks_spawn_y_15_18(), pos_x + x, y - pos_y - change_Y)
            elif 19 <= y < 21:
                Tile(blocks_spawn_y_19_20(), pos_x + x, y - pos_y - change_Y)
            elif y == 21:
                Tile("bedrock_block", pos_x + x, y - pos_y - change_Y)


def blocks_spawn_y_13():
    if random.randint(0, 1) == 1:
        return "stone_block"
    return "ground_block"


def blocks_spawn_y_15_18():
    y = random.randint(0, 10)
    if y <= 5:
        return "stone_block"
    elif 5 < y < 7:
        return "ground_block"
    elif y == 9:
        return "gold_block"
    return "block_of_iron"


def blocks_spawn_y_19_20():
    y = random.randint(0, 1)
    if y == 0:
        return "stone_block"
    else:
        return "bedrock_block"


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


def putting_blocks(sprite_x, sprite_y, new_player, event):
    if sprite_x <= event.pos[0] <= sprite_x + TITLE_WIDTH and sprite_y <= event.pos[1] <= sprite_y + TITLE_HEIGHT:
        if abs(new_player.rect.x - sprite_x) < IMPACT_DISTANCE_X * TITLE_WIDTH and abs(
                new_player.rect.y + new_player.rect.size[
                    1] - sprite_y) <= IMPACT_DISTANCE_Y * TITLE_HEIGHT:
            if sprite_y <= event.pos[1] <= sprite_y + TITLE_HEIGHT * 0.33:
                Tile('block_of_land', (sprite_x // TITLE_WIDTH) + 0.5,
                     (sprite_y // TITLE_HEIGHT) - 1)

            elif sprite_y + TITLE_HEIGHT * 0.66 <= event.pos[1] <= sprite_y + TITLE_HEIGHT:
                Tile('block_of_land', (sprite_x // TITLE_WIDTH) + 0.5,
                     (sprite_y // TITLE_HEIGHT) + 1)
            elif sprite_x <= event.pos[0] <= sprite_x + TITLE_WIDTH * 0.5 and (
                    new_player.rect.x - sprite_x) < 0:
                Tile('block_of_land', (sprite_x // TITLE_WIDTH) - 0.5,
                     (sprite_y // TITLE_HEIGHT))
            elif sprite_x + TITLE_WIDTH * 0.5 <= event.pos[0] <= sprite_x + TITLE_WIDTH and (
                    new_player.rect.x - sprite_x) > 0:
                Tile('block_of_land', (sprite_x // TITLE_WIDTH) + 1.5,
                     (sprite_y // TITLE_HEIGHT))


def remove_blocks(sprite_x, sprite_y, new_player, event, sprite):
    if (sprite_x <= event.pos[0] <= sprite_x + TITLE_WIDTH and sprite_y <= event.pos[
        1] <= sprite_y + TITLE_HEIGHT) and sprite.name != "player" and sprite.name != "bedrock_block" and (abs(
        new_player.rect.x - sprite_x) < IMPACT_DISTANCE_X * TITLE_WIDTH and abs(
        new_player.rect.y + new_player.rect.size[
            1] - sprite_y) <= IMPACT_DISTANCE_Y * TITLE_HEIGHT):
        sprite.kill()


def check_next_blocks(new_player, side, change_Y):
    for sprite in all_sprites:
        if side == "right":
            if (sprite.rect.x != new_player.rect.x + TITLE_WIDTH) or ((
                                                                              new_player.rect.y <= sprite.rect.y < new_player.rect.y +
                                                                              new_player.rect.size[1]) is False):
                continue
            else:
                print(new_player.rect.y + change_Y * TITLE_HEIGHT, change_Y,
                      new_player.rect.y + new_player.rect.size[1] + change_Y * TITLE_HEIGHT, sprite.rect.y)
                return False
        else:
            if (sprite.rect.x != new_player.rect.x - TITLE_WIDTH) or ((
                                                                              new_player.rect.y <= sprite.rect.y < new_player.rect.y +
                                                                              new_player.rect.size[1]) is False):
                continue
            else:
                print(new_player.rect.y + change_Y * TITLE_HEIGHT, change_Y,
                      new_player.rect.y + new_player.rect.size[1] + change_Y * TITLE_HEIGHT, sprite.rect.y)
                return False
    return True
