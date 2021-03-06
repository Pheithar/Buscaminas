from configuration import Configuration

class Cell():

    config = Configuration()

    cord = int, int
    type = str   #Cover, Uncover o Flag
    value = int
    sprite = str #image


    def __init__(self, cord):
        self.cord = cord
        self.type = "Cover"
        self.value = 0

    #Si es del tipo cubierto, y si recibe boton izquierdo, se cambia a bandera, si
    #es botón derecho, se cambia a descubierto y aparece el valor
    #Si es bandera, y recibe boron izquierdo, cambia a cubierto, y si recibe
    #boton derecho, no hace nada
    #Si es descubierto, no hace nada de todas formas
    #Por parámetro debe recibir r_click para el botón derecho, y l_click para
    #el botón izquierdo
    def change_type(self, click):
        if self.type == "Cover":
            if click == "r_click":
                self.type = "Uncover"
            elif click == "l_click":
                self.type = "Flag"

        elif self.type == "Flag":
            if click == "l_click":
                self.type = "Cover"
