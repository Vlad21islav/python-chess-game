import pygame
import sys

clock = pygame.time.Clock()
sc = pygame.display.set_mode((500, 500))
w, h = pygame.display.get_surface().get_size()

square_size = 200
x = square_size // 2
y = h // 2
direction = False

image = pygame.transform.scale(pygame.image.load('images.jpeg'), (square_size, square_size))

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # заливаем фон
    sc.fill("white")
    # рисуем квадрат
    sc.blit(image, (x - square_size // 2, y - square_size // 2))
    # обновляем окно
    pygame.display.update()

    if not direction:
        x += 1
    else:
        x -= 1

    if x >= w - square_size // 2:
        direction = True
    elif x <= square_size // 2:
        direction = False

    clock.tick(120)
