import cell.Cell

class Board:
    #constructor de tablero
    def __init__(self, size_X, size_y, bombs)
    self.size_X  = size_X
    self.size_Y = size_Y
    self.bombs = bombs #se pone un número inicial de bombas al crear el tablero

    #creamos el tablero inicial
    for i in range(size_X):
        for j in range(size_Y):
            cells[i][j] = Cell(i,j)
