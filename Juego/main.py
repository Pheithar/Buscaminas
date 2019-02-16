import pygame
pygame.init()

#Importar la clase configuracion
from configuration import Configuration
#Importar las clases
from casilla import Cell
from tablero import Board

#Tiempo
import time

#VARIABLES

config = Configuration()    #Clase con todas los valores numericos

#PRUEBA -------

board = Board(config.BOARD_SIZE, 0)

#------





end_game = False    #Variable para terminar el juego

clicked = False     #Variable para saber si el jugador ha clickado o no

fps_clock = pygame.time.Clock()     #Contador interno interno de PYGAME
windows = pygame.display.set_mode(config.SCREEN_SIZE)


#Cargar el archivo de imagenes y dividirlo en lineas
img_file = open("images.txt").readlines()
#Coger las lineas que nos interesan del archivo

#CARGA DE IMAGENES

for i in range(0, len(img_file)):
    #Array de los elemnetos de la linea
    img_line = img_file[i].split()

    #Carga de imagenes
    if img_line[0] == "HCell":
        #Carga
        c_basic = pygame.image.load(img_line[1])
        #Reescalado
        c_basic = pygame.transform.scale(c_basic, config.CELL_SIZE)
    if img_line[0] == "0Cell":
        #Carga
        c_0 = pygame.image.load(img_line[1])
        #Reescalado
        c_0 = pygame.transform.scale(c_0, config.CELL_SIZE)
    if img_line[0] == "1Cell":
        #Carga
        c_1 = pygame.image.load(img_line[1])
        #Reescalado
        c_1 = pygame.transform.scale(c_1, config.CELL_SIZE)
    if img_line[0] == "2Cell":
        #Carga
        c_2 = pygame.image.load(img_line[1])
        #Reescalado
        c_2 = pygame.transform.scale(c_2, config.CELL_SIZE)
    if img_line[0] == "3Cell":
        #Carga
        c_3 = pygame.image.load(img_line[1])
        #Reescalado
        c_3 = pygame.transform.scale(c_3, config.CELL_SIZE)
    if img_line[0] == "4Cell":
        #Carga
        c_4 = pygame.image.load(img_line[1])
        #Reescalado
        c_4 = pygame.transform.scale(c_4, config.CELL_SIZE)
    if img_line[0] == "5Cell":
        #Carga
        c_5 = pygame.image.load(img_line[1])
        #Reescalado
        c_5 = pygame.transform.scale(c_5, config.CELL_SIZE)
    if img_line[0] == "6Cell":
        #Carga
        c_6 = pygame.image.load(img_line[1])
        #Reescalado
        c_6 = pygame.transform.scale(c_6, config.CELL_SIZE)
    if img_line[0] == "7Cell":
        #Carga
        c_7 = pygame.image.load(img_line[1])
        #Reescalado
        c_7 = pygame.transform.scale(c_7, config.CELL_SIZE)
    if img_line[0] == "8Cell":
        #Carga
        c_8 = pygame.image.load(img_line[1])
        #Reescalado
        c_8 = pygame.transform.scale(c_8, config.CELL_SIZE)
    if img_line[0] == "BombCell":
        #Carga
        c_bomb = pygame.image.load(img_line[1])
        #Reescalado
        c_bomb = pygame.transform.scale(c_bomb, config.CELL_SIZE)
    if img_line[0] == "FlagCell":
        #Carga
        c_flag = pygame.image.load(img_line[1])
        #Reescalado
        c_flag = pygame.transform.scale(c_flag, config.CELL_SIZE)

#FIN DE LA CARGA DE IMAGENES
"""
#DIBUJAR EL TABLERO INICIAL
for i in range(0, board.size[0]):
    for j in range(0, board.size[1]):
        board.cells[i][j].sprite = c_basic
        windows.blit(board.cells[i][j].sprite, board.cells[i][j].cord)
"""

#COMIENZO BUCLE DEL JUEGO

while not end_game:
    fps_clock.tick(30)  #FPS del juego(creo)


    #calculo de la posicion del raton en cada iteracion del bucle
    pos_mouse = pygame.mouse.get_pos()
    #Se obtiene que boton del raton esta siendo clickado en cada momento
    r_click, m_click, l_click = pygame.mouse.get_pressed()


    #Evitar que se pueda clickear muy rapido
    #Si no se ha clickeado, se cambia a clickeado, y si se ha clickeado,
    #tiene que esperar 0,1s para poder volver a clickear
    if (l_click or m_click or r_click) and not clicked:
        clicked = True
    elif (l_click or m_click or r_click) and clicked:
        l_click = 0
        m_click = 0
        r_click = 0
        time.sleep(0.1)
        clicked = False

    for i in range(0, board.size[0]):
        for j in range(0, board.size[1]):
            #CAMBIAR LAS CASILLAS QUE LO REQUIEREN(Quiza hacer funcion??)
            #TIENE QUE IR LO PRIMERO(Porque la primera vez inicializa)
            if board.cells[i][j].type == "Cover":
                board.cells[i][j].sprite = c_basic
            if board.cells[i][j].type == "Uncover":
                board.cells[i][j].sprite = c_0
            if board.cells[i][j].type == "Flag":
                board.cells[i][j].sprite = c_flag

            #CONDICIONES PARA COMPROBAR
            #POR FIIIIIIIIN
            b_cond_0 = pos_mouse[0]>=board.cells[i][j].cord[0]
            b_cond_1 = pos_mouse[1]>=board.cells[i][j].cord[1]
            x_cond = pos_mouse[0]<board.cells[i][j].cord[0]+config.CELL_SIZE[0]
            y_cond = pos_mouse[1]<board.cells[i][j].cord[1]+config.CELL_SIZE[1]
            #print(b_cond, x_cond, y_cond)

            #COMPROBAR SI ALGUNA CASILLA CAMBIA
            #Si el raton esta encima de una casilla y se aprieta l_click
            #pos_mouse>=board.cells[i][j].cord[0]
            if b_cond_0 and b_cond_1 and x_cond and y_cond and l_click:
                board.cells[i][j].change_type("l_click")
                #print(board.cells[i][j].cord)
            if b_cond_0 and b_cond_1 and x_cond and y_cond and r_click:
                board.cells[i][j].change_type("r_click")




            #PINTAR LAS CASILLAS
            windows.blit(board.cells[i][j].sprite, board.cells[i][j].cord)





    #Obtener todos los eventos que puede obtener PYGAME
    #EJ:mover raton, pulsar tecla...
    for event in pygame.event.get():
        #Si se pulsa el boton X de la ventana, termina el bucle y el juego
        if event.type == pygame.QUIT:
            end_game = True


    pygame.display.update()     #Actualizar la pantalla

#FIN BUCLE

#TERMINAR JUEGO
pygame.quit()
