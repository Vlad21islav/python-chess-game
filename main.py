import pygame
import sys

sc = pygame.display.set_mode((500, 500), flags=pygame.RESIZABLE)
size = (0, 0)


sq_x = 0
sq_y = 0

space = 0


while True:
    if size != pygame.display.get_window_size():
        size = pygame.display.get_window_size()

        if min(size) == size[0]:
            sq_x = 0
            sq_y = (max(size) - min(size)) // 2
        elif size[0] == size[1]:
            sq_x = 0
            sq_y = 0
        else:
            sq_x = (max(size) - min(size)) // 2
            sq_y = 0

        space = min(size) // 100

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    sc.fill((29, 32, 37))
    mouse = pygame.mouse.get_pos()

    for x in range(8):
        for y in range(8):
            rect = pygame.draw.rect(sc, 'white', (sq_x + min(size) // 8 * x + space, sq_y + min(size) // 8 * y + space, min(size) // 8 - space, min(size) // 8 - space))

    pygame.display.update()
