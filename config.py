import pygame

import handler
WIDTH, HEIGHT = 1600, 960

TITLE_WIDTH = WIDTH // 16
TITLE_HEIGHT = HEIGHT // 16


folder_blocks = "blocks/"
folder_player = f"player/"

textures = {
    "stone_block": (folder_blocks + 'stone_block.png'),
    "cobblestone_block": (folder_blocks + 'cobblestone_block.png'),
    "block_of_land": (folder_blocks + 'block_of_land.png')
}

models = {
    "player_right": (folder_player + 'model_player_right.png'),
    "player_left": (folder_player + 'model_player_left.png')

}

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()