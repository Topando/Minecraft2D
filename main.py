import pygame

from handler import *


def start_game():
    pygame.init()
    camera = Camera()

    new_player = add_new_player()
    generate_level()
    pygame.display.set_caption('Minecraft')
    size = WIDTH, HEIGHT = 1600, 960
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    change_image(new_player, "player_left")
                    new_player.rect.x -= WIDTH // 16

                if event.key == pygame.K_d:
                    change_image(new_player, "player_right")
                    new_player.rect.x += WIDTH // 16
        camera.update(new_player);
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)
        screen.fill((0, 191, 255))
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
