import pygame

from handler import *
from config import player_group, all_sprites, WIDTH, HEIGHT
import handler


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image):
        super().__init__(player_group, all_sprites)
        self.name = "player"
        player_image = handler.image_player_right(image)
        player_image = pygame.transform.scale(player_image, (WIDTH // 16, HEIGHT // 4))
        self.image = player_image
        self.rect = self.image.get_rect().move(
            WIDTH // 2, HEIGHT // 2)


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.name = tile_type
        self.image = handler.image_texture(tile_type)
        self.image = pygame.transform.scale(self.image, (TITLE_WIDTH, TITLE_HEIGHT))
        self.rect = self.image.get_rect().move(
            TITLE_WIDTH * pos_x, TITLE_HEIGHT * pos_y)
        print(pos_x * TITLE_WIDTH)


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)
