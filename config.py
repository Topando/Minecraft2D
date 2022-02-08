import pygame

import handler

TITLE_WIDTH = 50
TITLE_HEIGHT = 50


folder_blocks = "blocks"
folder_player = f"player/"

textures = {
    "stone_block": (folder_blocks + 'stone_block.png'),
    "cobblestone_block": (folder_blocks + 'cobblestone_block.png'),
    "block_of_land": (folder_blocks + 'block_of_land.png')
}

models = {
    "player": (folder_player + 'model_player.png')
}

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()