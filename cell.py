class Cell():

    cord_x  #int
    cord_y  #int
    type    #String-> Cover, Uncover o Flag
    value   #int


    def __init__(self, cord_x, cord_y):
        self.cord_x = cord_x
        self.cord_y = cord_y

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
                type ==
            elif click == "l_click":
                pass

        elif type == "Flag":
            if click == "r_click":
                pass
            elif click == "l_click":
                pass
