import pygame
import asyncio
from handler import *


def start_game():
    pygame.init()
    camera = Camera()
    new_player = add_new_player()
    pygame.time.delay(1000)
    change_Y = 0
    generate_level(0, change_Y)
    pygame.display.set_caption('Minecraft')
    size = WIDTH, HEIGHT = 1600, 960
    screen = pygame.display.set_mode(size)
    running = True
    pos_player = new_player.rect.x // TITLE_WIDTH
    while running:
        chunk = 0
        flag = True
        for sprite in all_sprites:
            if check_down(new_player, sprite):
                flag = False
        if flag == True:
            new_player.rect.y += TITLE_HEIGHT
            change_Y += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    change_image(new_player, "player_left")
                    new_player.rect.x -= WIDTH // 16
                    pos_player -= 1
                    chunk = pos_player // 17

                    if len(LEFT_MAP) == abs(pos_player - 8) // 17 and pos_player - 8 < 0:
                        generate_level(-16.5, change_Y, 2, "left")
                        LEFT_MAP[chunk] = "@"

                if event.key == pygame.K_d:
                    change_image(new_player, "player_right")
                    new_player.rect.x += WIDTH // 16
                    pos_player += 1
                    chunk = pos_player // 17
                    print(chunk)
                    print(MAP_LIST)
                    print(pos_player)
                    Tile('block_of_land', 8,  2)

                    if len(MAP_LIST) == abs(pos_player + 8) // 17 and pos_player + 8 > 0:
                        generate_level(17 - 0.5, change_Y, 2)
                        pygame.time.delay(8000)
                        MAP_LIST[chunk] == "@"
                setting_map_list(chunk)
                print(LEFT_MAP, MAP_LIST)
            if event.type == pygame.MOUSEBUTTONDOWN:
                for sprite in all_sprites:
                    sprite_x = sprite.rect.x
                    sprite_y = sprite.rect.y
                    if (sprite_x <= event.pos[0] <= sprite_x + TITLE_WIDTH and sprite_y <= event.pos[
                        1] <= sprite_y + TITLE_HEIGHT) and sprite.name != "player" and (abs(
                        new_player.rect.x - sprite_x) < IMPACT_DISTANCE_X * TITLE_WIDTH and abs(
                        new_player.rect.y + new_player.rect.size[1] - sprite_y) <= IMPACT_DISTANCE_Y * TITLE_HEIGHT):
                        sprite.kill()
        camera.update(new_player)
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)
        screen.fill((0, 191, 255))
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
