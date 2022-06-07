import pygame
from Colors import Colors
import math
import Locations
import Constants
import Diagonal

pygame.init()

NoTiles = 8
w = 600
h = 600
screen = pygame.display.set_mode((w, h))
cellSize = h // NoTiles
pygame.display.set_caption("Chess")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
first_click = False

Master = {key: {"status": '0', "element_color": "", "element_type": "", "moved": "0", "tile_color": Colors['white']} for
          key in
          [str(i) + str(j) for i in range(1, 9) for j in range(1, 9)]}


def get_coords(mouse_pos, cellSize):
    xPos, yPos = mouse_pos
    return math.ceil(xPos / cellSize), math.ceil(yPos / cellSize)


def get_position_details(mouse_pos, cellSize, Master):
    xPos, yPos = get_coords(mouse_pos, cellSize)
    return Master[str(xPos) + str(yPos)]


def reset_kings(cellSize, Master):
    Elephant_loc = Locations.Kings(cellSize)

    elephant_img_white = pygame.image.load('king_white.png')
    elephant_img_white = pygame.transform.scale(elephant_img_white, (50, 50))
    init_elephant_X_white, _ = elephant_img_white.get_rect().size
    Elephant_loc_white, el = Elephant_loc.white(init_elephant_X_white)
    for pos, p in zip(Elephant_loc_white, el):
        add_element(elephant_img_white, pos, 'white', 'king', Master, p)
        update_master(p, "1", 'white', 'king', Master, "0")

    elephant_img_white = pygame.image.load('king_black.png')
    elephant_img_white = pygame.transform.scale(elephant_img_white, (50, 50))
    init_elephant_X_white, _ = elephant_img_white.get_rect().size
    Elephant_loc_white, el = Elephant_loc.black(init_elephant_X_white)
    for pos, p in zip(Elephant_loc_white, el):
        add_element(elephant_img_white, pos, 'black', 'king', Master, p)
        update_master(p, "1", 'black', 'king', Master, "0")


def reset_queens(cellSize, Master):
    Elephant_loc = Locations.Queens(cellSize)

    elephant_img_white = pygame.image.load('queen_white.png')
    elephant_img_white = pygame.transform.scale(elephant_img_white, (50, 50))
    init_elephant_X_white, _ = elephant_img_white.get_rect().size
    Elephant_loc_white, el = Elephant_loc.white(init_elephant_X_white)
    for pos, p in zip(Elephant_loc_white, el):
        add_element(elephant_img_white, pos, 'white', 'queen', Master, p)
        update_master(p, "1", 'white', 'queen', Master, "0")

    elephant_img_white = pygame.image.load('queen_black.png')
    elephant_img_white = pygame.transform.scale(elephant_img_white, (50, 50))
    init_elephant_X_white, _ = elephant_img_white.get_rect().size
    Elephant_loc_white, el = Elephant_loc.black(init_elephant_X_white)
    for pos, p in zip(Elephant_loc_white, el):
        add_element(elephant_img_white, pos, 'black', 'queen', Master, p)
        update_master(p, "1", 'black', 'queen', Master, "0")


def reset_horses(cellSize, Master):
    Elephant_loc = Locations.Horses(cellSize)

    elephant_img_white = pygame.image.load('knight_white.png')
    elephant_img_white = pygame.transform.scale(elephant_img_white, (50, 50))
    init_elephant_X_white, _ = elephant_img_white.get_rect().size
    Elephant_loc_white, el = Elephant_loc.white(init_elephant_X_white)
    for pos, p in zip(Elephant_loc_white, el):
        add_element(elephant_img_white, pos, 'white', 'horse', Master, p)
        update_master(p, "1", 'white', 'horse', Master, "0")

    elephant_img_white = pygame.image.load('knight_black.png')
    elephant_img_white = pygame.transform.scale(elephant_img_white, (50, 50))
    init_elephant_X_white, _ = elephant_img_white.get_rect().size
    Elephant_loc_white, el = Elephant_loc.black(init_elephant_X_white)
    for pos, p in zip(Elephant_loc_white, el):
        add_element(elephant_img_white, pos, 'black', 'horse', Master, p)
        update_master(p, "1", 'black', 'horse', Master, "0")


def reset_camels(cellSize, Master):
    Elephant_loc = Locations.Camels(cellSize)

    elephant_img_white = pygame.image.load('bishop_white.png')
    elephant_img_white = pygame.transform.scale(elephant_img_white, (50, 50))
    init_elephant_X_white, _ = elephant_img_white.get_rect().size
    Elephant_loc_white, el = Elephant_loc.white(init_elephant_X_white)
    for pos, p in zip(Elephant_loc_white, el):
        add_element(elephant_img_white, pos, 'white', 'camel', Master, p)
        update_master(p, "1", 'white', 'camel', Master, "0")

    elephant_img_white = pygame.image.load('bishop_black.png')
    elephant_img_white = pygame.transform.scale(elephant_img_white, (50, 50))
    init_elephant_X_white, _ = elephant_img_white.get_rect().size
    Elephant_loc_white, el = Elephant_loc.black(init_elephant_X_white)
    for pos, p in zip(Elephant_loc_white, el):
        add_element(elephant_img_white, pos, 'black', 'camel', Master, p)
        update_master(p, "1", 'black', 'camel', Master, "0")


def reset_pawns(cellSize, Master):
    Pawn_loc = Locations.Pawns(cellSize)

    pawn_img_black = pygame.image.load('pawn_black.png')
    init_pawn_X_black, _ = pawn_img_black.get_rect().size
    Pawn_loc_black, pl = Pawn_loc.black(init_pawn_X_black)
    for pos, p in zip(Pawn_loc_black, pl):
        add_element(pawn_img_black, pos, 'black', 'pawn', Master, p)
        update_master(p, "1", 'black', 'pawn', Master, "0")

    pawn_img_white = pygame.image.load('pawn_white.png')
    init_pawn_X_white, _ = pawn_img_white.get_rect().size
    Pawn_loc_white, pl = Pawn_loc.white(init_pawn_X_white)
    for pos, p in zip(Pawn_loc_white, pl):
        add_element(pawn_img_white, pos, 'white', 'pawn', Master, p)
        update_master(p, "1", 'white', 'pawn', Master, "0")


def reset_elephants(cellSize, Master):
    Elephant_loc = Locations.Elephants(cellSize)

    elephant_img_white = pygame.image.load('elephant_white.png')
    elephant_img_white = pygame.transform.scale(elephant_img_white, (50, 50))
    init_elephant_X_white, _ = elephant_img_white.get_rect().size
    Elephant_loc_white, el = Elephant_loc.white(init_elephant_X_white)
    for pos, p in zip(Elephant_loc_white, el):
        add_element(elephant_img_white, pos, 'white', 'elephant', Master, p)
        update_master(p, "1", 'white', 'elephant', Master, "0")

    elephant_img_white = pygame.image.load('elephant_black.png')
    elephant_img_white = pygame.transform.scale(elephant_img_white, (50, 50))
    init_elephant_X_white, _ = elephant_img_white.get_rect().size
    Elephant_loc_white, el = Elephant_loc.black(init_elephant_X_white)
    for pos, p in zip(Elephant_loc_white, el):
        add_element(elephant_img_white, pos, 'black', 'elephant', Master, p)
        update_master(p, "1", 'black', 'elephant', Master, "0")


def draw_rectangle(board, color, position):
    pygame.draw.rect(board, color, position)


def add_element(img, pos, element_color, element_type, Master, pos_rc):
    screen.blit(img, pos)


def update_master(pos, status, element_color, element_type, Master, moved):
    key = "".join([str(c) for c in pos])
    # if element_color is not None:
    Master[key]['status'] = status
    # if element_type is not None:
    Master[key]['element_color'] = element_color
    Master[key]['element_type'] = element_type
    if moved is not None:
        Master[key]['moved'] = moved


def get_opponent_color(color):
    if color == 'black':
        return 'white'
    else:
        return 'black'


def get_img_resized(color, element_type, x=50, y=50):
    img = pygame.image.load(Constants.loc[color][element_type])
    return pygame.transform.scale(img, (x, y))


def reset_element_selection(Master, selected_element):
    # print('resetting to', Master[selected_element])
    old_xPos = int(selected_element[0])
    old_yPos = int(selected_element[-1])
    draw_rectangle(screen, Master[selected_element]['tile_color'],
                   ((old_xPos - 1) * cellSize, (old_yPos - 1) * cellSize, cellSize, cellSize))

    if Master[selected_element]['element_type'] == 'pawn':
        img = pygame.image.load(Constants.loc[Master[selected_element]['element_color']]['pawn'])

    else:
        img = get_img_resized(Master[selected_element]['element_color'], Master[selected_element]['element_type'])

    init_X, _ = img.get_rect().size
    POS = (init_X // 4 + (old_xPos - 1) * cellSize, (old_yPos - 1) * cellSize + init_X // 4)

    add_element(img, POS,
                Master[selected_element]['element_color'],
                Master[selected_element]['element_type'], Master, (old_xPos, old_yPos))

    update_master((old_xPos, old_yPos), "1", Master[selected_element]['element_color'],
                  Master[selected_element]['element_type'], Master, None)
    pygame.display.flip()


def check_move_validity(selected_element, new_xPos, new_yPos, Master):
    if Master[selected_element]['element_type'] == 'pawn':
        if Master[selected_element]['element_color'] == 'black':
            if Master[selected_element]['moved'] == "0":
                steps = 2
            else:
                steps = 1
        else:
            if Master[selected_element]['moved'] == "0":
                steps = -2
            else:
                steps = -1

        if Master[selected_element]['element_color'] == 'black':
            Y_RANGE = list(range(int(selected_element[-1]) + 1, int(selected_element[-1]) + steps + 1))
        else:
            Y_RANGE = list(range(int(selected_element[-1]) - 1, int(selected_element[-1]) + steps - 1, -1))

        X_RANGE = []
        old_xPos = int(selected_element[0])
        for x in [old_xPos - 1, old_xPos, old_xPos + 1]:
            if x in range(1, 9):
                if x == old_xPos:
                    if Master[str(x) + str(Y_RANGE[0])]['status'] == "0":
                        X_RANGE.append(x)
                elif Master[str(x) + str(Y_RANGE[0])]['status'] == "1":
                    if Master[str(x) + str(Y_RANGE[0])]['element_color'] != Master[selected_element]['element_color']:
                        X_RANGE.append(x)

            # print(f"{X_RANGE=}, {Y_RANGE=}")

        if new_xPos in X_RANGE and new_yPos in Y_RANGE:
            return True

        reset_element_selection(Master, selected_element)
        return False

    elif Master[selected_element]['element_type'] == 'elephant':
        old_xPos = int(selected_element[0])
        old_yPos = int(selected_element[-1])

        RANGE = get_elephant_range(old_xPos, old_yPos)
        if (new_xPos, new_yPos) in RANGE:
            if Master[str(new_xPos) + str(new_yPos)]['status'] == "1" and Master[str(new_xPos) + str(new_yPos)][
                'element_color'] != Master[selected_element]['element_color']:
                return True
            elif Master[str(new_xPos) + str(new_yPos)]['status'] != "1":
                return True
            else:
                reset_element_selection(Master, selected_element)
                return False
        else:
            reset_element_selection(Master, selected_element)
            return False

    elif Master[selected_element]['element_type'] == 'camel':
        old_xPos = int(selected_element[0])
        old_yPos = int(selected_element[-1])

        RANGE = list(set(Diagonal.get_diagonal_1(old_xPos, old_yPos) + Diagonal.get_diagonal_2(old_xPos, old_yPos)))
        # print(f"{new_xPos=}, {new_yPos=}, {RANGE=}")
        if (new_xPos, new_yPos) in RANGE:
            if Master[str(new_xPos) + str(new_yPos)]['status'] == "1" and Master[str(new_xPos) + str(new_yPos)][
                'element_color'] != Master[selected_element]['element_color']:
                return True
            elif Master[str(new_xPos) + str(new_yPos)]['status'] != "1":
                return True
            else:
                reset_element_selection(Master, selected_element)
                return False
        else:
            reset_element_selection(Master, selected_element)
            return False

    elif Master[selected_element]['element_type'] == 'horse':
        old_xPos = int(selected_element[0])
        old_yPos = int(selected_element[-1])
        RANGE = get_horse_range(old_xPos, old_yPos)
        # print(f"{new_xPos=}, {new_yPos=}, {RANGE=}")
        if (new_xPos, new_yPos) in RANGE:
            if Master[str(new_xPos) + str(new_yPos)]['status'] == "1" and Master[str(new_xPos) + str(new_yPos)][
                'element_color'] != Master[selected_element]['element_color']:
                return True
            elif Master[str(new_xPos) + str(new_yPos)]['status'] != "1":
                return True
            else:
                reset_element_selection(Master, selected_element)
                return False
        else:
            reset_element_selection(Master, selected_element)
            return False


    elif Master[selected_element]['element_type'] == 'queen':
        old_xPos = int(selected_element[0])
        old_yPos = int(selected_element[-1])
        RANGE = get_queen_range(old_xPos, old_yPos)
        # print(f"{new_xPos=}, {new_yPos=}, {RANGE=}")
        if (new_xPos, new_yPos) in RANGE:
            if Master[str(new_xPos) + str(new_yPos)]['status'] == "1" and Master[str(new_xPos) + str(new_yPos)][
                'element_color'] != Master[selected_element]['element_color']:
                return True
            elif Master[str(new_xPos) + str(new_yPos)]['status'] != "1":
                return True
            else:
                reset_element_selection(Master, selected_element)
                return False
        else:
            reset_element_selection(Master, selected_element)
            return False

    elif Master[selected_element]['element_type'] == 'king':
        old_xPos = int(selected_element[0])
        old_yPos = int(selected_element[-1])
        RANGE = get_king_range(old_xPos, old_yPos)
        # print(f"{new_xPos=}, {new_yPos=}, {RANGE=}")
        if (new_xPos, new_yPos) in RANGE:
            if Master[str(new_xPos) + str(new_yPos)]['status'] == "1" and Master[str(new_xPos) + str(new_yPos)][
                'element_color'] != Master[selected_element]['element_color']:
                return True
            elif Master[str(new_xPos) + str(new_yPos)]['status'] != "1":
                return True
            else:
                reset_element_selection(Master, selected_element)
                return False
        else:
            reset_element_selection(Master, selected_element)
            return False


def get_king_range(x_pos, y_pos):
    RANGE = []
    for x in (x_pos - 1, x_pos, x_pos + 1):
        for y in (y_pos - 1, y_pos, y_pos + 1):
            if x in range(1, 9) and y in range(1, 9):
                RANGE.append((x, y))
    return list(set(RANGE))


def get_queen_range(x_pos, y_pos):
    RANGE = Diagonal.get_diagonal_1(x_pos, y_pos) + Diagonal.get_diagonal_2(x_pos, y_pos) + get_elephant_range(x_pos,
                                                                                                               y_pos)
    return list(set(RANGE))


def get_horse_range(x_pos, y_pos):
    RANGE = []
    for x in (x_pos + 2, x_pos - 2):
        for y in (y_pos - 1, y_pos + 1):
            if x in range(1, 9) and y in range(1, 9):
                RANGE.append((x, y))

    for y in (y_pos + 2, y_pos - 2):
        for x in (x_pos - 1, x_pos + 1):
            if x in range(1, 9) and y in range(1, 9):
                RANGE.append((x, y))

    return list(set(RANGE))


def get_elephant_range(x_pos, y_pos):
    RANGE = []
    for x in range(1, 9):
        for y in range(1, 9):
            if x == x_pos and y != y_pos:
                RANGE.append((x, y))
            elif y == y_pos and x != x_pos:
                RANGE.append((x, y))

    return list(set(RANGE))


def highlight_tile(color):
    if color == Colors['gray']:
        return Colors['highlight_gray']
    else:
        return Colors['highlight_white']


def select_element(xPos, yPos, Master, selected_element):
    if Master[str(xPos) + str(yPos)]['status'] == "1":
        if Master[selected_element]['element_type'] == 'pawn':
            img = pygame.image.load(
                Constants.loc[Master[selected_element]['element_color']][Master[selected_element]['element_type']])
        else:
            img = get_img_resized(Master[selected_element]['element_color'], Master[selected_element]['element_type'])
        init_X, init_Y = img.get_rect().size
        draw_rectangle(screen, highlight_tile(Master[selected_element]['tile_color']),
                       ((xPos - 1) * cellSize, (yPos - 1) * cellSize, cellSize, cellSize))

        resize_val = 3 if Master[selected_element]['element_type'] == 'pawn' else 1
        img_resized = pygame.transform.scale(img, (init_X + resize_val, init_Y + resize_val))
        init_X, init_Y = img_resized.get_rect().size
        POS = (init_X // 4 + (xPos - 1) * cellSize, (yPos - 1) * cellSize + init_Y // 4)
        add_element(img_resized,
                    POS,
                    Master[selected_element]['element_color'],
                    Master[selected_element]['element_type'],
                    Master,
                    (xPos, yPos))
        pygame.display.flip()


def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element


def check_turn(current_player_color, selected_element_color):
    if current_player_color == selected_element_color:
        return True
    else:
        return False


def move_element(new_xPos, new_yPos, Master, selected_element):
    new_element = str(new_xPos) + str(new_yPos)
    old_xPos = int(selected_element[0])
    old_yPos = int(selected_element[-1])

    if Master[new_element]['status'] != "1" or Master[new_element]['element_color'] != Master[selected_element][
        'element_color']:
        draw_rectangle(screen, Master[selected_element]['tile_color'],
                       ((old_xPos - 1) * cellSize, (old_yPos - 1) * cellSize, cellSize, cellSize))
        draw_rectangle(screen, Master[new_element]['tile_color'],
                       ((new_xPos - 1) * cellSize, (new_yPos - 1) * cellSize, cellSize, cellSize))
        pygame.display.flip()

        if Master[selected_element]['element_type'] == 'pawn':
            img = pygame.image.load(
                Constants.loc[Master[selected_element]['element_color']][Master[selected_element]['element_type']])
        else:
            img = get_img_resized(Master[selected_element]['element_color'], Master[selected_element]['element_type'])
        init_X, init_Y = img.get_rect().size
        POS = (init_X // 4 + (xPos - 1) * cellSize, (yPos - 1) * cellSize + init_X // 4)

        add_element(img,
                    POS,
                    Master[selected_element]['element_color'],
                    Master[selected_element]['element_type'], Master, (new_xPos, new_yPos))

        update_master((new_xPos, new_yPos), "1", Master[selected_element]['element_color'],
                      Master[selected_element]['element_type'], Master, "1")
        pygame.display.flip()

        update_master((old_xPos, old_yPos), "0", "", "", Master, "1")


    else:
        # print(f"{selected_element} cannot be moved to {str(xPos), str(yPos)}")
        draw_rectangle(screen, Master[selected_element]['tile_color'],
                       ((old_xPos - 1) * cellSize, (old_yPos - 1) * cellSize, cellSize, cellSize))

        if Master[selected_element]['element_type'] == 'pawn':
            img = pygame.image.load(
                Constants.loc[Master[selected_element]['element_color']][Master[selected_element]['element_type']])
        else:
            img = get_img_resized(Master[selected_element]['element_color'], Master[selected_element]['element_type'])
        init_X, init_Y = img.get_rect().size

        POS = (init_X // 4 + (old_xPos - 1) * cellSize, (new_yPos - 1) * cellSize + init_X // 4)
        add_element(img,
                    POS,
                    Master[selected_element]['element_color'], Master[selected_element]['element_type'], Master,
                    (old_xPos, old_yPos))
        pygame.display.flip()

def get_winner(Master):
    winner = []
    for val in Master.values():
        if val['element_type'] == 'king':
            winner.append(val)

    if len(winner) == 1:
        return winner[0]['element_color']
    else:
        return False


for y in range(0, 8):
    for x in range(0, 8):
        if (x + y) % 2 != 0:
            draw_rectangle(screen, Colors['gray'], (x * cellSize, y * cellSize, cellSize, cellSize))
            Master[str(x + 1) + str(y + 1)]['tile_color'] = Colors['gray']
        else:
            draw_rectangle(screen, Colors['white'], (x * cellSize, y * cellSize, cellSize, cellSize))
            Master[str(x + 1) + str(y + 1)]['tile_color'] = Colors['white']

reset_pawns(cellSize, Master)
reset_elephants(cellSize, Master)
reset_camels(cellSize, Master)
reset_horses(cellSize, Master)
reset_kings(cellSize, Master)
reset_queens(cellSize, Master)

iter_func = cycle(['white', 'black'])
current_player = next(iter_func)

running = True
game_complete = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                mouse_pos = event.pos
                xPos, yPos = get_coords(mouse_pos, cellSize)
                first_click = not first_click
                TURN = check_turn(current_player_color = current_player,
                                  selected_element_color = Master[str(xPos) + str(yPos)]['element_color'])

                print(f"{TURN=}, {first_click=}")
                if first_click:
                    if TURN:
                        selected_element = str(xPos) + str(yPos)
                        select_element(xPos, yPos, Master, selected_element)
                    else:
                        first_click = not first_click
                    # print(get_position_details(mouse_pos, cellSize, Master))
                else:
                    if check_move_validity(selected_element, xPos, yPos, Master):
                        move_element(xPos, yPos, Master, selected_element)
                        current_player = next(iter_func)
                        game_complete = get_winner(Master)
            elif event.button == 3:  # Right click
                mouse_pos = event.pos

            if game_complete:
                pygame.draw.rect(screen, Colors['white'], (cellSize * 2, cellSize * 3, cellSize * 4, cellSize * 2))
                screen.blit(pygame.font.SysFont('Arial', 26).render(f'{game_complete} is the Winner..!', True,
                                                                    Colors['black']),
                            ((cellSize * 2) + 50, (cellSize * 3) + 50))
                # print(get_position_details(mouse_pos, cellSize, Master))

    pygame.display.update()
