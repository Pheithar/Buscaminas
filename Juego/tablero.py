from casilla import Cell
from configuration import Configuration

class Board:

    config = Configuration()

    size_x = int
    size_y = int
    n_bombs = int
    cells = []

    #IMPORTANTE ACORDARSE COMO CREAR MATRICES, Y USAR SELF (A mi se me habia
    #olvidado y he estado un buen rato)
    #Creacion del tablero en la forma inicial
    def create_board(self):
        #Posicion que va invrementando, donde se ponen las casillas
        cord_offset = 0, 0

        for i in range(0, self.size_x):
            self.cells.append([])
            for j in range(0, self.size_y):
                self.cells[i].append(Cell(cord_offset))

                #Aumentar el offset en x(Las tuplas son inmutables, se requiere
                #de crear una nueva)
                cord_offset = cord_offset[0] + self.config.CELL_SIZE[0], cord_offset[1]
            #Aumentar el offset en y(Las tuplas son inmutables, se requiere
            #de crear una nueva)
            cord_offset = cord_offset[0], cord_offset[1] + self.config.CELL_SIZE[0]

    #constructor de tablero
    def __init__(self, size_x, size_y, n_bombs):
        self.size_x  = size_x
        self.size_y = size_y
        self.n_bombs = n_bombs #se pone un número inicial de bombas al crear el tablero
        self.create_board()
