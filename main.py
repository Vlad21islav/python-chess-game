import pygame
import sys

pygame.init()
sc = pygame.display.set_mode((500, 500), flags=pygame.RESIZABLE)
size = (0, 0)


field = [['B_Rook', 'B_Knight', 'B_Bishop', 'B_Queen', 'B_King', 'B_Bishop', 'B_Knight', 'B_Rook'],
         ['B_Pawn', 'B_Pawn', 'B_Pawn', 'B_Pawn', 'B_Pawn', 'B_Pawn', 'B_Pawn', 'B_Pawn'],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['W_Pawn', 'W_Pawn', 'W_Pawn', 'W_Pawn', 'W_Pawn', 'W_Pawn', 'W_Pawn', 'W_Pawn'],
         ['W_Rook', 'W_Knight', 'W_Bishop', 'W_Queen', 'W_King', 'W_Bishop', 'W_Knight', 'W_Rook']]

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

        path = 'images/figures/'

        W_King   = pygame.transform.scale(pygame.image.load(path+'W_King.png'  ), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        W_Queen  = pygame.transform.scale(pygame.image.load(path+'W_Queen.png' ), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        W_Rook   = pygame.transform.scale(pygame.image.load(path+'W_Rook.png'  ), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        W_Knight = pygame.transform.scale(pygame.image.load(path+'W_Knight.png'), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        W_Bishop = pygame.transform.scale(pygame.image.load(path+'W_Bishop.png'), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        W_Pawn   = pygame.transform.scale(pygame.image.load(path+'W_Pawn.png'  ), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        B_King   = pygame.transform.scale(pygame.image.load(path+'B_King.png'  ), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        B_Queen  = pygame.transform.scale(pygame.image.load(path+'B_Queen.png' ), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        B_Rook   = pygame.transform.scale(pygame.image.load(path+'B_Rook.png'  ), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        B_Knight = pygame.transform.scale(pygame.image.load(path+'B_Knight.png'), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        B_Bishop = pygame.transform.scale(pygame.image.load(path+'B_Bishop.png'), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        B_Pawn   = pygame.transform.scale(pygame.image.load(path+'B_Pawn.png'  ), ((min(size) // 8 - space) // 2, min(size) // 8 - space))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    sc.fill((29, 32, 37))
    mouse = pygame.mouse.get_pos()

    for x in range(8):
        for y in range(8):

            if (x + y) % 2 == 0:
                color = (138, 178, 207)
            else:
                color = (43, 53, 61)

            rect = pygame.draw.rect(sc, color, (sq_x + min(size) // 8 * x + space, sq_y + min(size) // 8 * y + space, min(size) // 8 - space, min(size) // 8 - space))

            match field[y][x]:
                case 'W_King':
                    image = W_King
                case 'W_Queen':
                    image = W_Queen
                case 'W_Rook':
                    image = W_Rook
                case 'W_Knight':
                    image = W_Knight
                case 'W_Bishop':
                    image = W_Bishop
                case 'W_Pawn':
                    image = W_Pawn

                case 'B_King':
                    image = B_King
                case 'B_Queen':
                    image = B_Queen
                case 'B_Rook':
                    image = B_Rook
                case 'B_Knight':
                    image = B_Knight
                case 'B_Bishop':
                    image = B_Bishop
                case 'B_Pawn':
                    image = B_Pawn

                case '':
                    image = ''

            if image:
                sc.blit(image, (sq_x + min(size) // 8 * x + space + (min(size) // 8 - space) // 4, sq_y + min(size) // 8 * y))

    pygame.display.update()
