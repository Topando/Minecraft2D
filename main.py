import pygame
import asyncio
from handler import *


def start_game():
    pygame.init()

    camera = Camera()
    size = WIDTH, HEIGHT = 1600, 960
    new_player = add_new_player()
    app_inventory()
    pygame.time.delay(1000)
    change_Y = 0
    generate_level(0, change_Y)
    pygame.display.set_caption('Minecraft')
    screen = pygame.display.set_mode(size)
    running = True
    start(screen)
    set_music("all.mp3")
    pygame.mixer.music.play(-1)
    pos_player = new_player.rect.x // TITLE_WIDTH
    Flright = False
    Flleft = False
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
                if keys[pygame.K_ESCAPE]:
                    game_over(screen)
                    running = False
                if keys[pygame.K_SPACE] and keys[pygame.K_d]:
                    change_image(new_player, "player_right")
                    if checK_up_block("right", new_player):
                        new_player.rect.x += TITLE_WIDTH
                        new_player.rect.y -= TITLE_HEIGHT
                        pos_player += 1
                        change_Y -= 1
                        set_sound("jump_sound")

                elif keys[pygame.K_SPACE] and keys[pygame.K_a]:
                    change_image(new_player, "player_left")
                    if checK_up_block("left", new_player):
                        new_player.rect.x -= TITLE_WIDTH
                        new_player.rect.y -= TITLE_HEIGHT
                        pos_player -= 1
                        change_Y -= 1
                        set_sound("jump_sound")

                elif event.key == pygame.K_a:
                    change_image(new_player, "player_left")
                    if check_next_blocks(new_player, "left", change_Y):
                        change_image(new_player, "model_player_left_go")
                        Flleft = True
                        new_player.rect.x -= WIDTH // 16
                        pos_player -= 1
                        chunk = pos_player // 17
                elif event.key == pygame.K_d:
                    if check_next_blocks(new_player, "right", change_Y):
                        change_image(new_player, "model_player_right_go")
                        Flright = True
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
                if keys[pygame.K_0]:
                    pygame.mixer.music.pause()
                if keys[pygame.K_9]:
                    pygame.mixer.music.unpause()
                if keys[pygame.K_p]:
                    volume = pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(volume + 0.25)
                if keys[pygame.K_MINUS]:
                    volume = pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(volume - 0.25)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for sprite in all_sprites:
                        sprite_x = sprite.rect.x
                        sprite_y = sprite.rect.y
                        remove_blocks(sprite_x, sprite_y, new_player, event, sprite)
                    set_sound("break_block_sound")
                    broken_blocks()

                if event.button == 3:
                    for sprite in all_sprites:
                        sprite_x = sprite.rect.x
                        sprite_y = sprite.rect.y
                        putting_blocks(sprite_x, sprite_y, new_player, event)
                    set_sound("put_block_sound")

        camera.update(new_player)
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)
        screen.fill((0, 191, 255))
        all_sprites.draw(screen)
        pygame.display.flip()
        if Flright:
            change_image(new_player, "player_right")
            Flright = False
        elif Flleft:
            change_image(new_player, "player_left")
            Flleft = False

        pygame.time.delay(200)
    clear_file()
    pygame.quit()
