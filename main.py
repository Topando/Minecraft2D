import pygame

from handler import *


def start_game():
    pygame.init()
    camera = Camera()

    new_player = add_new_player()
    pygame.time.delay(1000)
    generate_level(0)
    pygame.display.set_caption('Minecraft')
    size = WIDTH, HEIGHT = 1600, 960
    screen = pygame.display.set_mode(size)
    running = True
    pos_player = new_player.rect.x // TITLE_WIDTH
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    change_image(new_player, "player_left")
                    new_player.rect.x -= WIDTH // 16
                    pos_player -= 1
                    chunk = pos_player // 17
                if event.key == pygame.K_d:
                    change_image(new_player, "player_right")
                    new_player.rect.x += WIDTH // 16
                    pos_player += 1
                    chunk = pos_player // 17
                    print(chunk)
                    print(MAP_LIST)
                    try:
                        MAP_LIST[(pos_player + 8) // 17]
                    except Exception:
                        generate_level(pos_player + 8 - 0.5, 2)
                        pygame.time.delay(8000)
                MAP_LIST[chunk] = "@"

                setting_map_list(chunk)
        camera.update(new_player)
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)
        screen.fill((0, 191, 255))
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
