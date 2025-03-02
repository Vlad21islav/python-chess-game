import os
import time
import pygame
import sys

# Инициализация Pygame
pygame.init()

# Создание окна с разрешением 500x500 пикселей, флаг RESIZABLE позволяет изменять размер окна
sc = pygame.display.set_mode((500, 500), flags=pygame.RESIZABLE)


# Функция для получения абсолютного пути к файлам (учитывает как режим разработки, так и работу через PyInstaller)
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))  # Проверка, что мы не в PyInstaller
    return os.path.join(base_path, relative_path)


# Установка заголовка окна и иконки
pygame.display.set_caption('Chess')
icon = pygame.image.load(resource_path('images/icon.jpg')).convert_alpha()  # Загрузка иконки
pygame.display.set_icon(icon)

# Инициализация переменных
size = (0, 0)
font = pygame.font.Font(None, 20)
start_time1 = time.time()
counter = 0
fps = ''
old_fps = ''


def possible_moves(figure):
    """Функция для определения возможных ходов фигуры"""
    highlighted.clear()  # Очищаем список подсвеченных клеток
    highlighted.append([x, y])  # Добавляем текущую позицию в список

    # Обработка различных фигур
    match figure[2:]:  # Сопоставляем фигуру по её типу
        case 'Rook':  # Ладья
            directions = [
                [1, 0],  # Движение вправо
                [-1, 0],  # Движение влево
                [0, 1],  # Движение вниз
                [0, -1]  # Движение вверх
            ]
            for direction in directions:
                pos = 1
                while True:
                    new_x = x + pos * direction[0]
                    new_y = y + pos * direction[1]

                    # Проверка выхода за пределы доски
                    if new_x < 0 or new_x >= 8 or new_y < 0 or new_y >= 8:
                        break

                    # Если клетка пуста, добавляем её в список подсветки
                    if field[new_y][new_x][0] == '.':
                        highlighted.append([new_x, new_y])
                    # Если клетка занята фигурой противника, также добавляем её, но не продолжаем движение
                    elif field[new_y][new_x][0] != turn:
                        highlighted.append([new_x, new_y])
                        break
                    else:
                        break
                    pos += 1

        # Аналогичная логика для других фигур (Конь, Слон, Ферзь, Король, Пешка) с их уникальными правилами движений
        case 'Knight':  # Конь
            new_positions = [
                [1, -2], [2, -1], [2, 1], [1, 2],
                [-1, -2], [-2, -1], [-2, 1], [-1, 2]
            ]

            for pos in new_positions:
                try:
                    if x + pos[0] < 0 or y + pos[1] < 0 or field[y + pos[1]][x + pos[0]][0] == turn:
                        pass
                    else:
                        highlighted.append([x + pos[0], y + pos[1]])  # Добавление допустимых позиций
                except IndexError:
                    pass

        case 'Bishop':  # Слон
            directions = [
                [1, 1], [-1, -1], [-1, 1], [1, -1]
            ]
            for direction in directions:
                pos = 1
                while True:
                    new_x = x + pos * direction[0]
                    new_y = y + pos * direction[1]

                    # Проверка выхода за пределы доски
                    if new_x < 0 or new_x >= 8 or new_y < 0 or new_y >= 8:
                        break

                    # Если клетка пуста или занята фигурой противника, добавляем её
                    if field[new_y][new_x][0] == '.':
                        highlighted.append([new_x, new_y])
                    elif field[new_y][new_x][0] != turn:
                        highlighted.append([new_x, new_y])
                        break
                    else:
                        break
                    pos += 1
        case 'Queen':  # Ферзь
            directions = [
                [1, 1], [-1, -1], [-1, 1], [1, -1],
                [1, 0], [-1, 0], [0, 1], [0, -1]
            ]
            for direction in directions:
                pos = 1
                while True:
                    new_x = x + pos * direction[0]
                    new_y = y + pos * direction[1]

                    # Проверка выхода за пределы доски
                    if new_x < 0 or new_x >= 8 or new_y < 0 or new_y >= 8:
                        break

                    # Если клетка пуста или занята фигурой противника, добавляем её
                    if field[new_y][new_x][0] == '.':
                        highlighted.append([new_x, new_y])
                    elif field[new_y][new_x][0] != turn:
                        highlighted.append([new_x, new_y])
                        break
                    else:
                        break
                    pos += 1
        case 'King':  # Король
            new_positions = [
                [1, 1], [-1, -1], [-1, 1], [1, -1],
                [1, 0], [-1, 0], [0, 1], [0, -1]
            ]

            # Логика рокировки
            if not figure_moved['King'][figure[0]] and field[y][5] == '.' and field[y][6] == '.' and not figure_moved['Rook'][figure[0]][1]:
                highlighted.append([7, y])  # Рокировка на правый фланг
            if not figure_moved['King'][figure[0]] and field[y][3] == '.' and field[y][2] == '.' and field[y][1] == '.' and not figure_moved['Rook'][figure[0]][0]:
                highlighted.append([0, y])  # Рокировка на левый фланг

            # Проверка возможных ходов
            for pos in new_positions:
                try:
                    if x + pos[0] < 0 or y + pos[1] < 0 or field[y + pos[1]][x + pos[0]][0] == turn:
                        pass
                    else:
                        highlighted.append([x + pos[0], y + pos[1]])  # Добавление допустимых позиций
                except IndexError:
                    pass

        case 'Pawn':  # Пешка
            if figure[0] == 'W':  # Белая пешка
                new_positions = [[0, -1]]  # Двигается на одну клетку вверх
                if y == 6:  # Если это начальная позиция, можно двигаться на две клетки
                    new_positions.append([0, -2])
            else:  # Чёрная пешка
                new_positions = [[0, 1]]  # Двигается на одну клетку вниз
                if y == 1:  # Начальная позиция
                    new_positions.append([0, 2])

            for pos in new_positions:
                new_x = x + pos[0]
                new_y = y + pos[1]

                # Проверка на допустимость перемещения по вертикали
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    if field[new_y][new_x][0] == '.':
                        highlighted.append([new_x, new_y])

                # Проверка на взятие пешки по диагонали
                if figure[0] == 'W':  # Для белых
                    if new_y == y - 1:
                        if x - 1 >= 0 and field[new_y][new_x - 1][0] != '.' and field[new_y][new_x - 1][0] != turn:
                            highlighted.append([new_x - 1, new_y])
                        if x + 1 < 8 and field[new_y][new_x + 1][0] != '.' and field[new_y][new_x + 1][0] != turn:
                            highlighted.append([new_x + 1, new_y])
                else:  # Для чёрных
                    if new_y == y + 1:
                        if x - 1 >= 0 and field[new_y][new_x - 1][0] != '.' and field[new_y][new_x - 1][0] != turn:
                            highlighted.append([new_x - 1, new_y])
                        if x + 1 < 8 and field[new_y][new_x + 1][0] != '.' and field[new_y][new_x + 1][0] != turn:
                            highlighted.append([new_x + 1, new_y])


def is_under_attack():
    """Функция для проверки, под атакой ли король"""
    king_row, king_col = king  # Получаем текущие координаты короля

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for direction in directions:
        row, col = king_row, king_col
        while 0 <= row < 8 and 0 <= col < 8:
            row += direction[0]
            col += direction[1]
            if 0 <= row < 8 and 0 <= col < 8:
                piece = field[col][row]
                if piece != '.':
                    if piece == f'{enemy_turn}_Queen' or \
                            (piece == f'{enemy_turn}_Rook' and direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]) or \
                            (piece == f'{enemy_turn}_Bishop' and direction in [(-1, -1), (-1, 1), (1, -1), (1, 1)]):
                        return True
                    break

    knight_moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    for move in knight_moves:
        row, col = king_row + move[0], king_col + move[1]
        if 0 <= row < 8 and 0 <= col < 8:
            if field[col][row] == f'{enemy_turn}_Knight':
                return True

    pawn_directions = [(-1, -1), (-1, 1)] if enemy_turn == 'B' else [(1, -1), (1, 1)]
    for direction in pawn_directions:
        row, col = king_row + direction[0], king_col + direction[1]
        if 0 <= row < 8 and 0 <= col < 8:
            if field[col][row] == f'{enemy_turn}_Pawn':
                return True

    return False


# Инициализация начальной позиции шахматной доски
field = [['B_Rook', 'B_Knight', 'B_Bishop', 'B_Queen', 'B_King', 'B_Bishop', 'B_Knight', 'B_Rook'],
         ['B_Pawn', 'B_Pawn', 'B_Pawn', 'B_Pawn', 'B_Pawn', 'B_Pawn', 'B_Pawn', 'B_Pawn'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['W_Pawn', 'W_Pawn', 'W_Pawn', 'W_Pawn', 'W_Pawn', 'W_Pawn', 'W_Pawn', 'W_Pawn'],
         ['W_Rook', 'W_Knight', 'W_Bishop', 'W_Queen', 'W_King', 'W_Bishop', 'W_Knight', 'W_Rook']]

# координаты в самом поле
field_x = 0
field_y = 0

highlighted = []  # Список для хранения подсвеченных клеток

# инициализация картинок
W_King, W_Queen, W_Rook, W_Knight, W_Bishop, W_Pawn = '......'
B_King, B_Queen, B_Rook, B_Knight, B_Bishop, B_Pawn = '......'
White_won, Black_won, Close = '...'

turn = 'W'  # Инициализация хода (белые начинают)
selected_figure = '.'  # Переменная для выбранной фигуры
figure_moved = {  # Состояние фигур (какие из них двигались)
    'Rook': {
        'W': [False, False],  # Белые ладьи
        'B': [False, False]  # Чёрные ладьи
    },
    'King': {
        'W': False,  # Белый король
        'B': False  # Чёрный король
    }
}

pawn_transformation = ['Queen', 'Rook', 'Bishop', 'Knight']  # Возможности превращения пешки
check = False  # Проверка на шах
who_won = ''  # Победитель

show_fps = False  # Показ FPS
winning_window_opened = False  # Окно победы открыто?

space = 0

game_is_over = False  # Игра окончена?
sc.fill((29, 32, 37))  # Заполнение экрана фоном

while True:
    # Обработка изменения размера окна
    if size != pygame.display.get_window_size():
        size = pygame.display.get_window_size()

        # Изменяем расположение шахматного поля в зависимости от размера окна
        if min(size) == size[0]:
            field_x = 0
            field_y = (max(size) - min(size)) // 2
        elif size[0] == size[1]:
            field_x = 0
            field_y = 0
        else:
            field_x = (max(size) - min(size)) // 2
            field_y = 0

        # Устанавливаем отступы для клеток поля
        space = min(size) // 100

        # Путь к изображениям фигур
        path = 'images/figures/'

        # Очищаем экран
        sc.fill((29, 32, 37))

        # Загружаем изображения всех фигур и масштабируем их в зависимости от размера окна
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
        White_won = pygame.transform.scale(pygame.image.load(resource_path('images/white_won.png')), (min(size), min(size)))
        Black_won = pygame.transform.scale(pygame.image.load(resource_path('images/white_won.png')), (min(size), min(size)))
        Close = pygame.transform.scale(pygame.image.load(resource_path('images/close.png')), (min(size) // 15, min(size) // 15))

        # Печатаем путь к изображению одной из фигур для отладки
        print(resource_path(path + 'B_Pawn.png'))

    # Получаем текущую позицию мыши и нажатые клавиши
    mouse = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    # Отображаем шахматное поле
    for x in range(8):
        for y in range(8):
            # Определяем цвет клетки в зависимости от ее координат
            if (x + y) % 2 == 0:
                color = (138, 178, 207)  # Светлый цвет
            else:
                color = (43, 53, 61)  # Темный цвет

            # Рисуем клетку на поле
            rect = pygame.draw.rect(sc, color, (field_x + min(size) // 8 * x + space, field_y + min(size) // 8 * y + space, min(size) // 8 - space, min(size) // 8 - space))

            # Проверяем, была ли нажата мышь на клетке с фигурой текущего игрока
            if rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and field[y][x][0] == turn and not game_is_over:
                king = [0, 0]

                # Находим позицию короля
                for figure_x in range(8):
                    for figure_y in range(8):
                        if field[figure_y][figure_x] == turn + '_' + 'King':
                            king = [figure_x, figure_y]

                check = False

                # Проверяем, находится ли король под атакой
                for figure_x in range(8):
                    for figure_y in range(8):
                        if field[figure_y][figure_x][0] != turn and field[figure_y][figure_x][0] != '.':
                            if turn == 'W':
                                enemy_turn = 'B'
                            else:
                                enemy_turn = 'W'
                            if is_under_attack():
                                check = True

                # Если выбрана фигура короля, проверяем возможность рокировки
                if selected_figure[0][2:] == 'King' and field[y][x][2:] == 'Rook' and [x, y] in highlighted:
                    # Если рокировка возможна, выполняем ее
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

                    # Меняем ход
                    if turn == 'W':
                        turn = 'B'
                    else:
                        turn = 'W'
                    highlighted.clear()
                else:
                    # Выбираем фигуру и показываем возможные ходы
                    selected_figure = [field[y][x], [x, y]]
                    possible_moves(figure=field[y][x])

            # Отображаем возможные ходы фигуры
            for i in highlighted:
                if (i[0], i[1]) == (x, y):
                    # Если король под атакой, выделяем клетку красным
                    if not check:
                        color = 'green'  # Зеленая клетка для возможного хода
                    else:
                        color = 'red'  # Красная клетка, если ход опасен

                    # Рисуем выделение клетки
                    rect = pygame.draw.rect(sc, color, (field_x + min(size) // 8 * i[0] + space, field_y + min(size) // 8 * i[1] + space, min(size) // 8 - space, min(size) // 8 - space))

                    # Если кликнули на клетку с возможным ходом, выполняем ход
                    if rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and field[i[1]][i[0]][0] != selected_figure[0][0] and not game_is_over:
                        print(selected_figure[0], i[0], i[1])
                        try:
                            # Если на клетке оказался король, завершаем игру
                            if field[i[1]][i[0]][2:] == 'King':
                                if field[i[1]][i[0]][0] == 'W':
                                    who_won = 'W'
                                else:
                                    who_won = 'B'
                                winning_window_opened = True
                                game_is_over = True
                                highlighted.clear()
                        except IndexError:
                            pass

                        # Выполняем ход
                        field[i[1]][i[0]] = selected_figure[0]
                        field[selected_figure[1][1]][selected_figure[1][0]] = '.'

                        # Если пешка дошла до последней линии, выполняем превращение
                        if selected_figure[0] == 'W_Pawn' and selected_figure[1][1] == 1 or selected_figure[0] == 'B_Pawn' and selected_figure[1][1] == 6:
                            time.sleep(0.5)
                            last_pressed = True
                            selecting = True
                            while selecting:
                                mouse = pygame.mouse.get_pos()

                                # Определяем направление движения пешки в зависимости от цвета
                                if selected_figure[0][0] == 'W':
                                    direction = 1
                                else:
                                    direction = -1

                                # Отображаем возможные фигуры для превращения
                                for figure in range(len(pawn_transformation)):
                                    rect = pygame.draw.rect(sc, 'white', (field_x + min(size) // 8 * i[0] + space, field_y + min(size) // 8 * (i[1] + figure * direction) + space,
                                                                          min(size) // 8 - space, min(size) // 8 - space))

                                    # Выбираем фигуру для превращения
                                    match selected_figure[0][0] + '_' + pawn_transformation[figure]:
                                        case 'W_Queen':
                                            image = W_Queen
                                        case 'W_Rook':
                                            image = W_Rook
                                        case 'W_Knight':
                                            image = W_Knight
                                        case 'W_Bishop':
                                            image = W_Bishop
                                        case 'B_Queen':
                                            image = B_Queen
                                        case 'B_Rook':
                                            image = B_Rook
                                        case 'B_Knight':
                                            image = B_Knight
                                        case 'B_Bishop':
                                            image = B_Bishop
                                        case _:
                                            image = ''

                                    # Рисуем фигуры для превращения
                                    if image:
                                        sc.blit(image, (field_x + min(size) // 8 * i[0] + space + (min(size) // 8 - space) // 4, field_y + min(size) // 8 * (i[1] + figure * direction)))

                                    # Если кликнули на фигуру, меняем пешку на эту фигуру
                                    if rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and not last_pressed:
                                        field[i[1]][i[0]] = selected_figure[0][0] + '_' + pawn_transformation[figure]
                                        selecting = False
                                    else:
                                        last_pressed = False

                                # Обновляем экран
                                pygame.display.update()

                                # Обработка на закрытие окна
                                for _ in pygame.event.get():
                                    if _.type == pygame.QUIT:
                                        sys.exit()

                        # Обновляем состояние фигуры, если это ладья или король
                        if selected_figure[0][2:] == 'Rook':
                            if selected_figure[1][0] == 0:
                                figure_moved['Rook'][selected_figure[0][0]][0] = True
                            if selected_figure[1][0] == 7:
                                figure_moved['Rook'][selected_figure[0][0]][1] = True
                        elif selected_figure[0][2:] == 'King':
                            figure_moved['King'][selected_figure[0][0]] = True

                        # Меняем ход
                        if turn == 'W':
                            turn = 'B'
                        else:
                            turn = 'W'
                        highlighted.clear()
                        break

            # Отображаем фигуры на доске
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
                case _:
                    image = ''

            # Рисуем фигуру на соответствующей клетке
            if image:
                sc.blit(image, (field_x + min(size) // 8 * x + space + (min(size) // 8 - space) // 4, field_y + min(size) // 8 * y))

    # Если игра закончена, отображаем окно с результатом
    if winning_window_opened:
        if who_won == 'W':
            sc.blit(White_won, (field_x, field_y))
        else:
            sc.blit(Black_won, (field_x, field_y))
        sc.blit(Close, (field_x + min(size) // 16 * 12.5, field_y + min(size) // 16 * 2.5))  # Выводим крести для закрытия окна с результатом
        close_rect = pygame.Rect(field_x + min(size) // 16 * 12.5, field_y + min(size) // 16 * 2.5, min(size) // 15, min(size) // 15)
        if close_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:  # проверяем крести на нажатие
            winning_window_opened = False  # Закрываем окно с результатами
            size = (0, 0)  # изменяем разммер для обновления поля

    # Стираем прошедшее FPS, если включено
    if show_fps:
        sc.blit(font.render(old_fps, True, (29, 32, 37)), (10, 10))

    # Обновляем FPS каждую секунду
    counter += 1
    if (time.time() - start_time1) > 1:
        old_fps = fps
        fps = "FPS: " + str(int(counter / (time.time() - start_time1)))
        counter = 0
        start_time1 = time.time()

    # Отображаем актуальное FPS, если включено
    if show_fps:
        sc.blit(font.render(fps, True, (180, 0, 0)), (10, 10))

    # Включение/выключение отображения FPS
    if keys[pygame.K_f]:
        time.sleep(0.5)
        if show_fps:
            show_fps = False
        else:
            show_fps = True
        size = (0, 0)  # Изменяем размер для обновления поля

    # Обновляем экран
    pygame.display.update()

    # Обработка на закрытие окна
    for _ in pygame.event.get():
        if _.type == pygame.QUIT:
            sys.exit()
