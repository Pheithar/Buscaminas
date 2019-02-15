from casilla import Cell
from configuration import Configuration

class Board:

    config = Configuration()

    size = int, int
    n_bombs = int
    cells = []

    #IMPORTANTE ACORDARSE COMO CREAR MATRICES, Y USAR SELF (A mi se me habia
    #olvidado y he estado un buen rato)
    #Creacion del tablero en la forma inicial
    def create_board(self):
        #Posicion que va invrementando, donde se ponen las casillas
        cord_offset = self.config.BOARD_OFFSET

        for i in range(0, self.size[0]):
            self.cells.append([])
            for j in range(0, self.size[1]):
                self.cells[i].append(Cell(cord_offset))

                #Aumentar el offset en x(Las tuplas son inmutables, se requiere
                #de crear una nueva)
                cord_offset = cord_offset[0] + self.config.CELL_SIZE[0], cord_offset[1]

            #Aumentar el offset en y(Las tuplas son inmutables, se requiere
            #de crear una nueva)
            cord_offset = self.config.BOARD_OFFSET[0], cord_offset[1] + self.config.CELL_SIZE[0]

    #constructor de tablero
    def __init__(self, size, n_bombs):
        self.size = size    #Es una tupla de dos elementos
        self.n_bombs = n_bombs #se pone un número inicial de bombas al crear el tablero
        self.create_board()
