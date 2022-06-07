
def get_diagonal_1(x_pos, y_pos):
    diag = []

    i = x_pos
    j = y_pos
    while i > 0 and j > 0:
        diag.append((i, j))
        i -= 1
        j -= 1

    i = x_pos
    j = y_pos
    while i < 9 and j < 9:
        diag.append((i, j))
        i += 1
        j += 1

    return list(set(diag))


def get_diagonal_2(x_pos, y_pos):
    diag = []

    i = x_pos
    j = y_pos
    while i < 9 and j > 0:
        diag.append((i, j))
        i += 1
        j -= 1

    i = x_pos
    j = y_pos
    while i > 0 and j < 9:
        diag.append((i, j))
        i -= 1
        j += 1

    return list(set(diag))