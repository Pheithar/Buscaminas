class Cell():

    cord = int, int
    type = str   #Cover, Uncover o Flag
    value = int
    sprite = str #image


    def __init__(self, cord):
        self.cord = cord
        type = "Cover"
        value = 0

    #Si es del tipo cubierto, y si recibe boton derecho, se cambia a bandera, si
    #es botón izquierdo, se cambia a descubierto y aparece el valor
    #Si es bandera, y recibe boron derecho, cambia a cubierto, y si recibe
    #boton izquierdo, no hace nada
    #Si es descubierto, no hace nada de todas formas
    #Por parámetro debe recibir r_click para el botón derecho, y l_click para
    #el botón izquierdo
    def change_type(click):
        if type == "Cover":
            if click == "r_click":
                type == "Flag"
            elif click == "l_click":
                type == "Uncover"

        elif type == "Flag":
            if click == "r_click":
                type = "Cover"
