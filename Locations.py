
class Pawns:
    def __init__(self, cellSize):
        self.cellSize = cellSize

    def white(self, init_pawn_X_white):
        pawns = []
        p = []
        y = 7
        for x in range(0, 8):
            pawns.append((init_pawn_X_white // 4 + x * self.cellSize, self.cellSize*6 + init_pawn_X_white // 4 ))
            p.append((x + 1, y))
        return pawns, p

    def black(self, init_pawn_X_black):
        pawns = []
        p = []
        y = 2
        for x in range(8):
            pawns.append( (init_pawn_X_black//4 + x*self.cellSize, init_pawn_X_black//4 + self.cellSize ))
            p.append((x + 1, y))
        return pawns, p

class Elephants:
    def __init__(self, cellSize):
        self.cellSize = cellSize

    def black(self, init_X):
        elephants = []
        e = []
        y = 0
        for x in [0, 7]:
            elephants.append( (init_X // 4 + (x * self.cellSize), self.cellSize*(y) + init_X//4  ) )
            e.append( (x + 1, y + 1) )
        return elephants, e

    def white(self, init_X):
        elephants = []
        e = []
        y = 7
        for x in [0, 7]:
            elephants.append( (init_X // 4 + (x * self.cellSize), self.cellSize*(y) + init_X//4  ) )
            e.append( (x + 1, y + 1) )
        return elephants, e

class Camels:
    def __init__(self, cellSize):
        self.cellSize = cellSize

    def black(self, init_X):
        elephants = []
        e = []
        y = 0
        for x in [1, 6]:
            elephants.append( (init_X // 4 + (x * self.cellSize), self.cellSize*(y) + init_X//4  ) )
            e.append( (x + 1, y + 1) )
        return elephants, e

    def white(self, init_X):
        elephants = []
        e = []
        y = 7
        for x in [1, 6]:
            elephants.append( (init_X // 4 + (x * self.cellSize), self.cellSize*(y) + init_X//4  ) )
            e.append( (x + 1, y + 1) )
        return elephants, e


class Horses:
    def __init__(self, cellSize):
        self.cellSize = cellSize

    def black(self, init_X):
        elephants = []
        e = []
        y = 0
        for x in [2, 5]:
            elephants.append( (init_X // 4 + (x * self.cellSize), self.cellSize*(y) + init_X//4  ) )
            e.append( (x + 1, y + 1) )
        return elephants, e

    def white(self, init_X):
        elephants = []
        e = []
        y = 7
        for x in [2, 5]:
            elephants.append( (init_X // 4 + (x * self.cellSize), self.cellSize*(y) + init_X//4  ) )
            e.append( (x + 1, y + 1) )
        return elephants, e

class Kings:
    def __init__(self, cellSize):
        self.cellSize = cellSize

    def black(self, init_X):
        x = 5
        y = 1
        return [(init_X // 4 + ((x - 1) * self.cellSize), self.cellSize*(y - 1) + init_X//4  )], [(x, y)]

    def white(self, init_X):
        x = 5
        y = 8
        return [(init_X // 4 + ((x - 1) * self.cellSize), self.cellSize * (y - 1) + init_X // 4)], [(x, y)]

class Queens:
    def __init__(self, cellSize):
        self.cellSize = cellSize

    def black(self, init_X):
        x = 4
        y = 1
        return [(init_X // 4 + ((x - 1) * self.cellSize), self.cellSize*(y - 1) + init_X//4  )], [(x, y)]

    def white(self, init_X):
        x = 4
        y = 8
        return [(init_X // 4 + ((x - 1) * self.cellSize), self.cellSize * (y - 1) + init_X // 4)], [(x, y)]