import pygame

from handler import *


def start_game():
    pygame.init()
    new_player = add_new_player()

    pygame.display.set_caption('Minecraft')
    size = width, height = 1500, 1000
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        all_sprites.draw(screen)

        print(new_player.rect.w, new_player.rect.h)
        pygame.display.flip()
    pygame.quit()
