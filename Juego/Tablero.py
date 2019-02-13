import cell.Cell

class Board:
    #constructor de tablero
    def __init__(self, size_X, size_y, bombs)
    self.size_X  = size_X
    self.size_Y = size_Y
    self.bombs = bombs #se pone un número inicial de bombas al crear el tablero
    create_board()

    def create_board():
    #creamos el tablero inicial
    i = 0
    j = 0
    #i = 0
    #j = 0
    for i in range(0, self.size_X):
        for j in range(0, self.size_Y):
            cells[i][j] = Cell(i,j)
