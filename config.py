import pygame

import handler

# Size
WIDTH, HEIGHT = 1600, 960
######
# MAP
MAP_LIST = []
LEFT_MAP = []
####

# Size BLOCK
TITLE_WIDTH = WIDTH // 16
TITLE_HEIGHT = HEIGHT // 16
###

# distance
IMPACT_DISTANCE_X = 4
IMPACT_DISTANCE_Y = 5
###
folder_blocks = "blocks/"
folder_player = f"player/"

textures = {
    "stone_block": (folder_blocks + 'stone_block.png'),
    "cobblestone_block": (folder_blocks + 'cobblestone_block.png'),
    "block_of_land": (folder_blocks + 'grass_block.png'),
    "ground_block": (folder_blocks + 'ground_block.png'),
    "block_of_iron": (folder_blocks + 'block_of_iron.png'),
    "gold_block": (folder_blocks + 'gold_block.png'),
    "bedrock_block": (folder_blocks + 'bedrock_block.png')
}

models = {
    "player_right": (folder_player + 'model_player_right.png'),
    "player_left": (folder_player + 'model_player_left.png')

}

INVENTORY = {

}


all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
