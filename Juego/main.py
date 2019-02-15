import pygame
pygame.init()

#Importar la clase configuracion
from configuration import Configuration
#Importar las clases
from casilla import Cell
from tablero import Board

#VARIABLES

config = Configuration()    #Clase con todas los valores numericos

#PRUEBA -------

board = Board(5, 5, 0)

#------





end_game = False    #Variable para terminar el juego

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

#COMIENZO BUCLE DEL JUEGO

while not end_game:
    fps_clock.tick(30)  #FPS del juego(creo)

    #Obtener todos los eventos que puede obtener PYGAME
    #EJ:mover raton, pulsar tecla...
    for event in pygame.event.get():
        #Si se pulsa el boton X de la ventana, termina el bucle y el juego
        if event.type == pygame.QUIT:
            end_game = True


    cell.sprite = c_0
    windows.blit(cell.sprite, (0, 0))




    pygame.display.update()     #Actualizar la pantalla

#FIN BUCLE

#TERMINAR JUEGO
pygame.quit()