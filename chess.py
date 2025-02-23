import os
import pygame
import sys

pygame.init()
sc = pygame.display.set_mode((500, 500), flags=pygame.RESIZABLE)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


pygame.display.set_caption('Chess')
icon = pygame.image.load(resource_path('images/icon.jpg')).convert_alpha()
pygame.display.set_icon(icon)
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
                while True:
                    new_x = x + pos * direction[0]
                    new_y = y + pos * direction[1]

                    if new_x < 0 or new_x >= 8 or new_y < 0 or new_y >= 8:
                        break

                    if field[new_y][new_x][0] == '.':
                        highlighted.append([new_x, new_y])
                    elif field[new_y][new_x][0] != turn:
                        highlighted.append([new_x, new_y])
                        break
                    else:
                        break
                    pos += 1

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
                while True:
                    new_x = x + pos * direction[0]
                    new_y = y + pos * direction[1]

                    if new_x < 0 or new_x >= 8 or new_y < 0 or new_y >= 8:
                        break

                    if field[new_y][new_x][0] == '.':
                        highlighted.append([new_x, new_y])
                    elif field[new_y][new_x][0] != turn:
                        highlighted.append([new_x, new_y])
                        break
                    else:
                        break
                    pos += 1
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
                while True:
                    new_x = x + pos * direction[0]
                    new_y = y + pos * direction[1]

                    if new_x < 0 or new_x >= 8 or new_y < 0 or new_y >= 8:
                        break

                    if field[new_y][new_x][0] == '.':
                        highlighted.append([new_x, new_y])
                    elif field[new_y][new_x][0] != turn:
                        highlighted.append([new_x, new_y])
                        break
                    else:
                        break
                    pos += 1
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

            if not figure_moved['King'][figure[0]] and field[y][5] == '.' and field[y][6] == '.' and not figure_moved['Rook'][figure[0]][1]:
                highlighted.append([7, y])
            if not figure_moved['King'][figure[0]] and field[y][3] == '.' and field[y][2] == '.' and field[y][1] == '.' and not figure_moved['Rook'][figure[0]][0]:
                highlighted.append([0, y])

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
                new_x = x + pos[0]
                new_y = y + pos[1]

                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    if field[new_y][new_x][0] == '.':
                        highlighted.append([new_x, new_y])

                if figure[0] == 'W':
                    if new_y == y - 1:
                        if x - 1 >= 0 and field[new_y][new_x - 1][0] != '.' and field[new_y][new_x - 1][0] != turn:
                            highlighted.append([new_x - 1, new_y])
                        if x + 1 < 8 and field[new_y][new_x + 1][0] != '.' and field[new_y][new_x + 1][0] != turn:
                            highlighted.append([new_x + 1, new_y])
                else:
                    if new_y == y + 1:
                        if x - 1 >= 0 and field[new_y][new_x - 1][0] != '.' and field[new_y][new_x - 1][0] != turn:
                            highlighted.append([new_x - 1, new_y])
                        if x + 1 < 8 and field[new_y][new_x + 1][0] != '.' and field[new_y][new_x + 1][0] != turn:
                            highlighted.append([new_x + 1, new_y])


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
figure_moved = {
    'Rook': {
        'W': [False, False],
        'B': [False, False]
    },
    'King': {
        'W': False,
        'B': False
    }
}

space = 0

game_is_over = False

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

        W_King = pygame.transform.scale(pygame.image.load(resource_path(path + 'W_King.png')), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        W_Queen = pygame.transform.scale(pygame.image.load(resource_path(path + 'W_Queen.png')), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        W_Rook = pygame.transform.scale(pygame.image.load(resource_path(path + 'W_Rook.png')), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        W_Knight = pygame.transform.scale(pygame.image.load(resource_path(path + 'W_Knight.png')), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        W_Bishop = pygame.transform.scale(pygame.image.load(resource_path(path + 'W_Bishop.png')), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        W_Pawn = pygame.transform.scale(pygame.image.load(resource_path(path + 'W_Pawn.png')), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        B_King = pygame.transform.scale(pygame.image.load(resource_path(path + 'B_King.png')), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        B_Queen = pygame.transform.scale(pygame.image.load(resource_path(path + 'B_Queen.png')), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        B_Rook = pygame.transform.scale(pygame.image.load(resource_path(path + 'B_Rook.png')), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        B_Knight = pygame.transform.scale(pygame.image.load(resource_path(path + 'B_Knight.png')), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        B_Bishop = pygame.transform.scale(pygame.image.load(resource_path(path + 'B_Bishop.png')), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        B_Pawn = pygame.transform.scale(pygame.image.load(resource_path(path + 'B_Pawn.png')), ((min(size) // 8 - space) // 2, min(size) // 8 - space))
        print(resource_path(path + 'B_Pawn.png'))

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
            if rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and field[y][x][0] == turn and not game_is_over:
                if selected_figure[0][2:] == 'King' and field[y][x][2:] == 'Rook' and [x, y] in highlighted:
                    if x == 0:
                        figure_moved['Rook'][selected_figure[0][0]][0] = True
                        figure_moved['King'][selected_figure[0][0]] = True
                        field[y][2] = selected_figure[0]
                        field[selected_figure[1][1]][selected_figure[1][0]] = '.'
                        field[y][3] = field[y][x]
                        field[y][x] = '.'
                    elif x == 7:
                        figure_moved['Rook'][selected_figure[0][0]][1] = True
                        figure_moved['King'][selected_figure[0][0]] = True
                        field[y][6] = selected_figure[0]
                        field[selected_figure[1][1]][selected_figure[1][0]] = '.'
                        field[y][5] = field[y][x]
                        field[y][x] = '.'

                    if turn == 'W':
                        turn = 'B'
                    else:
                        turn = 'W'
                    highlighted.clear()
                else:
                    selected_figure = [field[y][x], [x, y]]
                    possible_moves()

            for i in highlighted:
                if (i[0], i[1]) == (x, y):
                    rect = pygame.draw.rect(sc, 'green', (field_x + min(size) // 8 * i[0] + space, field_y + min(size) // 8 * i[1] + space, min(size) // 8 - space, min(size) // 8 - space))

                    if rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and field[i[1]][i[0]][0] != selected_figure[0][0] and not game_is_over:
                        print(selected_figure[0], i[0], i[1])
                        try:
                            if field[i[1]][i[0]][2:] == 'King':
                                game_is_over = True
                                highlighted.clear()
                        except IndexError:
                            pass
                        if selected_figure[0] == 'W_Pawn' and selected_figure[1][1] == 1:
                            field[i[1]][i[0]] = 'W_Queen'
                        elif selected_figure[0] == 'B_Pawn' and selected_figure[1][1] == 6:
                            field[i[1]][i[0]] = 'B_Queen'
                        else:
                            field[i[1]][i[0]] = selected_figure[0]
                        field[selected_figure[1][1]][selected_figure[1][0]] = '.'

                        if selected_figure[0][2:] == 'Rook':
                            if selected_figure[1][0] == 0:
                                figure_moved['Rook'][selected_figure[0][0]][0] = True
                            if selected_figure[1][0] == 7:
                                figure_moved['Rook'][selected_figure[0][0]][1] = True
                        elif selected_figure[0][2:] == 'King':
                            figure_moved['King'][selected_figure[0][0]] = True

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
