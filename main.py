import pygame
import asyncio
from handler import *


def start_game():
    pygame.init()
    camera = Camera()
    new_player = add_new_player()
    app_inventory()
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
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE] and keys[pygame.K_d]:
                    change_image(new_player, "player_right")
                    if checK_up_block("right", new_player):
                        new_player.rect.x += TITLE_WIDTH
                        new_player.rect.y -= TITLE_HEIGHT
                        pos_player += 1
                        change_Y -= 1
                        print(3123)

                elif keys[pygame.K_SPACE] and keys[pygame.K_a]:
                    change_image(new_player, "player_left")
                    if checK_up_block("left", new_player):
                        new_player.rect.x -= TITLE_WIDTH
                        new_player.rect.y -= TITLE_HEIGHT
                        pos_player -= 1
                        change_Y -= 1
                elif event.key == pygame.K_a:
                    change_image(new_player, "player_left")
                    if check_next_blocks(new_player, "left", change_Y):
                        new_player.rect.x -= WIDTH // 16
                        pos_player -= 1
                        chunk = pos_player // 17
                elif event.key == pygame.K_d:
                    change_image(new_player, "player_right")
                    if check_next_blocks(new_player, "right", change_Y):
                        new_player.rect.x += WIDTH // 16
                        pos_player += 1
                        chunk = pos_player // 17

                if len(LEFT_MAP) == abs(pos_player - 8) // 17 and pos_player - 8 < 0:
                    generate_level(-16.5, change_Y, 2, "left")
                    LEFT_MAP[chunk] = "@"
                if len(MAP_LIST) == abs(pos_player + 8) // 17 and pos_player + 8 > 0:
                    generate_level(17 - 0.5, change_Y, 2)
                    MAP_LIST[chunk] == "@"
                setting_map_list(chunk)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for sprite in all_sprites:
                        sprite_x = sprite.rect.x
                        sprite_y = sprite.rect.y
                        remove_blocks(sprite_x, sprite_y, new_player, event, sprite)
                if event.button == 3:
                    for sprite in all_sprites:
                        sprite_x = sprite.rect.x
                        sprite_y = sprite.rect.y
                        putting_blocks(sprite_x, sprite_y, new_player, event)
        camera.update(new_player)
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)
        screen.fill((0, 191, 255))
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
