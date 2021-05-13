import socket
import pygame
import pickle
import os
import sys
from random import randint
from data import pygame_textinput


size = width, height = 1600, 1000
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Colonization Strategy')
running = True


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удалось загрузить изображение:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


def terminate():
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()


def menu():
    fon = load_image('Main_menu.png')
    screen.blit(fon, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 290 <= event.pos[0] <= 510 and 430 <= event.pos[1] <= 510:
                    pass
                elif 50 <= event.pos[0] <= 270 and 430 <= event.pos[1] <= 510:
                    pass
                elif 530 <= event.pos[0] <= 750 and 430 <= event.pos[1] <= 510:
                    pass
        screen.blit(fon, (0, 0))
        pygame.display.flip()
        clock.tick(60)



menu()
