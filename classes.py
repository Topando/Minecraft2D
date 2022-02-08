import pygame

from handler import *
from config import player_group, all_sprites
import handler


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)

        player_image = handler.image_player()
        self.image = player_image
        self.rect = self.image.get_rect().move(
            TITLE_WIDTH * pos_x + 15, TITLE_HEIGHT * pos_y + 5)
