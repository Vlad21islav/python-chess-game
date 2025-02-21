import pygame
import sys

pygame.init()
sc = pygame.display.set_mode((500, 500), flags=pygame.RESIZABLE)
size = (0, 0)


def possible_moves():
    figure = field[y][x]

    highlighted.clear()
    highlighted.append([x, y])

    match figure[2:]:
        case 'Rook':
            directions = [
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1]
            ]
            for direction in directions:
                pos = 1
                try:
                    while field[y + pos * direction[1]][x + pos * direction[0]][0] != turn:
                        if (x + pos * direction[0]) < 0 or (y + pos * direction[1]) < 0:
                            break
                        highlighted.append([x + pos * direction[0], y + pos * direction[1]])
                        pos += 1
                        if field[y + pos * direction[1]][x + pos * direction[0]][0] != turn and field[y + pos * direction[1]][x + pos * direction[0]][0] != '.':
                            highlighted.append([x + pos * direction[0], y + pos * direction[1]])
                            break
                except IndexError:
                    pass
        case 'Knight':
            new_positions = [
                [1, -2],
                [2, -1],
                [2, 1],
                [1, 2],
                [-1, -2],
                [-2, -1],
                [-2, 1],
                [-1, 2]
            ]

            for pos in new_positions:
                try:
                    if x + pos[0] < 0 or y + pos[1] < 0 or field[y + pos[1]][x + pos[0]][0] == turn:
                        pass
                    else:
                        highlighted.append([x + pos[0], y + pos[1]])
                except IndexError:
                    pass
        case 'Bishop':
            directions = [
                [1, 1],
                [-1, -1],
                [-1, 1],
                [1, -1]
            ]
            for direction in directions:
                pos = 1
                try:
                    while field[y + pos * direction[1]][x + pos * direction[0]][0] != turn:
                        if (x + pos * direction[0]) < 0 or (y + pos * direction[1]) < 0:
                            break
                        highlighted.append([x + pos * direction[0], y + pos * direction[1]])
                        pos += 1
                        if field[y + pos * direction[1]][x + pos * direction[0]][0] != turn and field[y + pos * direction[1]][x + pos * direction[0]][0] != '.':
                            highlighted.append([x + pos * direction[0], y + pos * direction[1]])
                            break
                except IndexError:
                    pass
        case 'Queen':
            directions = [
                [1, 1],
                [-1, -1],
                [-1, 1],
                [1, -1],
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1]
            ]
            for direction in directions:
                pos = 1
                try:
                    while field[y + pos * direction[1]][x + pos * direction[0]][0] != turn:
                        if (x + pos * direction[0]) < 0 or (y + pos * direction[1]) < 0:
                            break
                        highlighted.append([x + pos * direction[0], y + pos * direction[1]])
                        pos += 1
                        if field[y + pos * direction[1]][x + pos * direction[0]][0] != turn and field[y + pos * direction[1]][x + pos * direction[0]][0] != '.':
                            highlighted.append([x + pos * direction[0], y + pos * direction[1]])
                            break
                except IndexError:
                    pass
        case 'King':
            new_positions = [
                [1, 1],
                [-1, -1],
                [-1, 1],
                [1, -1],
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1]
            ]

            for pos in new_positions:
                try:
                    if x + pos[0] < 0 or y + pos[1] < 0 or field[y + pos[1]][x + pos[0]][0] == turn:
                        pass
                    else:
                        highlighted.append([x + pos[0], y + pos[1]])
                except IndexError:
                    pass
        case 'Pawn':
            if figure[0] == 'W':
                new_positions = [
                    [0, -1]
                ]
                if y == 6:
                    new_positions.append([0, -2])
            else:
                new_positions = [
                    [0, 1]
                ]
                if y == 1:
                    new_positions.append([0, 2])

            for pos in new_positions:
                try:
                    if figure[0] == 'W' and field[y - 1][x - 1][0] != turn and field[y - 1][x - 1][0] != '.':
                        highlighted.append([x - 1, y - 1])
                    if figure[0] == 'W' and field[y - 1][x + 1][0] != turn and field[y - 1][x + 1][0] != '.':
                        highlighted.append([x + 1, y - 1])
                    if figure[0] == 'B' and field[y + 1][x + 1][0] != turn and field[y + 1][x + 1][0] != '.':
                        highlighted.append([x + 1, y + 1])
                    if figure[0] == 'B' and field[y + 1][x - 1][0] != turn and field[y + 1][x - 1][0] != '.':
                        highlighted.append([x - 1, y + 1])
                    if x + pos[0] < 0 or y + pos[1] < 0 or field[y + pos[1]][x + pos[0]][0] != '.':
                        break
                    else:
                        highlighted.append([x + pos[0], y + pos[1]])
                except IndexError:
                    pass


field = [['B_Rook', 'B_Knight', 'B_Bishop', 'B_Queen', 'B_King', 'B_Bishop', 'B_Knight', 'B_Rook'],
         ['B_Pawn', 'B_Pawn', 'B_Pawn', 'B_Pawn', 'B_Pawn', 'B_Pawn', 'B_Pawn', 'B_Pawn'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['W_Pawn', 'W_Pawn', 'W_Pawn', 'W_Pawn', 'W_Pawn', 'W_Pawn', 'W_Pawn', 'W_Pawn'],
         ['W_Rook', 'W_Knight', 'W_Bishop', 'W_Queen', 'W_King', 'W_Bishop', 'W_Knight', 'W_Rook']]

field_x = 0
field_y = 0

highlighted = []

turn = 'W'
selected_figure = '.'

space = 0

while True:
    if size != pygame.display.get_window_size():
        size = pygame.display.get_window_size()

        if min(size) == size[0]:
            field_x = 0
            field_y = (max(size) - min(size)) // 2
        elif size[0] == size[1]:
            field_x = 0
            field_y = 0
        else:
            field_x = (max(size) - min(size)) // 2
            field_y = 0

        space = min(size) // 100

        path = 'images/figures/'

        W_King = pygame.transform.scale(pygame.image.load(path + 'W_King.png'), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        W_Queen = pygame.transform.scale(pygame.image.load(path + 'W_Queen.png'), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        W_Rook = pygame.transform.scale(pygame.image.load(path + 'W_Rook.png'), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        W_Knight = pygame.transform.scale(pygame.image.load(path + 'W_Knight.png'), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        W_Bishop = pygame.transform.scale(pygame.image.load(path + 'W_Bishop.png'), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        W_Pawn = pygame.transform.scale(pygame.image.load(path + 'W_Pawn.png'), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        B_King = pygame.transform.scale(pygame.image.load(path + 'B_King.png'), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        B_Queen = pygame.transform.scale(pygame.image.load(path + 'B_Queen.png'), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        B_Rook = pygame.transform.scale(pygame.image.load(path + 'B_Rook.png'), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        B_Knight = pygame.transform.scale(pygame.image.load(path + 'B_Knight.png'), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        B_Bishop = pygame.transform.scale(pygame.image.load(path + 'B_Bishop.png'), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        B_Pawn = pygame.transform.scale(pygame.image.load(path + 'B_Pawn.png'), ((min(size) // 8 - space) // 2, min(size) // 8 - space))

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

            rect = pygame.draw.rect(sc, color, (field_x + min(size) // 8 * x + space, field_y + min(size) // 8 * y + space, min(size) // 8 - space, min(size) // 8 - space))
            if rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and field[y][x][0] == turn:
                selected_figure = [field[y][x], [x, y]]
                possible_moves()

            for i in highlighted:
                if (i[0], i[1]) == (x, y):
                    rect = pygame.draw.rect(sc, 'green', (field_x + min(size) // 8 * i[0] + space, field_y + min(size) // 8 * i[1] + space, min(size) // 8 - space, min(size) // 8 - space))

                    if rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and field[i[1]][i[0]][0] != turn:
                        print(selected_figure[0], selected_figure[1][1])
                        if selected_figure[0] == 'W_Pawn' and selected_figure[1][1] == 1:
                            field[i[1]][i[0]] = 'W_Queen'
                        elif selected_figure[0] == 'B_Pawn' and selected_figure[1][1] == 6:
                            field[i[1]][i[0]] = 'B_Queen'
                        else:
                            field[i[1]][i[0]] = selected_figure[0]
                        field[selected_figure[1][1]][selected_figure[1][0]] = '.'
                        if turn == 'W':
                            turn = 'B'
                        else:
                            turn = 'W'
                        highlighted.clear()
                        break

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

                case '.':
                    image = ''

            if image:
                sc.blit(image, (field_x + min(size) // 8 * x + space + (min(size) // 8 - space) // 4, field_y + min(size) // 8 * y))

    pygame.display.update()
