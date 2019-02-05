#Importar e inicializar pygame
import pygame
pygame.init()



#crear una ventana con los parámetors (altura, anchura)
win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height))

#Definr un nombre para la ventana de pygame
pygame.display.set_caption("First Game")

#Propiedades del "Jugador"
x = 50
y = 420
width = 64
height = 64
vel = 5

run = True

#Saltos
is_jumping = False
jump_count = 10

#Animaciones
left = False
right = False
step_count = 0


# Cargar las imagenes de movimiento, fondo y estático
walkRight = [pygame.image.load('Pygame-Images/R1.png'),
pygame.image.load('Pygame-Images/R2.png'), pygame.image.load('Pygame-Images/R3.png'),
pygame.image.load('Pygame-Images/R4.png'), pygame.image.load('Pygame-Images/R5.png'),
pygame.image.load('Pygame-Images/R6.png'), pygame.image.load('Pygame-Images/R7.png'),
pygame.image.load('Pygame-Images/R8.png'), pygame.image.load('Pygame-Images/R9.png')]
walkLeft = [pygame.image.load('Pygame-Images/L1.png'),
pygame.image.load('Pygame-Images/L2.png'), pygame.image.load('Pygame-Images/L3.png'),
pygame.image.load('Pygame-Images/L4.png'), pygame.image.load('Pygame-Images/L5.png'),
pygame.image.load('Pygame-Images/L6.png'), pygame.image.load('Pygame-Images/L7.png'),
pygame.image.load('Pygame-Images/L8.png'), pygame.image.load('Pygame-Images/L9.png')]
bg = pygame.image.load('Pygame-Images/bg.jpg')
char = pygame.image.load('Pygame-Images/standing.png')

while run:
    #Esperar 0.05s
    pygame.time.delay(50)

    #Detectar eventos
    for event in pygame.event.get():
        #Si pulsas la X de la pestaña, run=false(termina el programa)
        if event.type == pygame.QUIT:
            run = False

    #Guarda la tecla que está siendo pulsada
    keys = pygame.key.get_pressed()

    #Mover en los 4 ejes. Si se usan elif no permite movimientos diagonales
    #Bloquea para que no se salga de la pantalla
    if keys[pygame.K_LEFT] and x >= vel: #Si esta en la posicion x < vel, quiere
    #decir que está lo más al borde que puede estar
        x-= vel
    if keys[pygame.K_RIGHT] and x <  (win_width - width):
        x += vel

    #Solo pued ocurrir si no está saltando
    if not(is_jumping):
        """
        if keys[pygame.K_UP] and y >= vel:
            y -= vel
        if keys[pygame.K_DOWN] and y <  (win_height - height):
            y += vel
        """
        #Saltos
        if keys[pygame.K_SPACE]:
            is_jumping = True

    #El salto actua durant 20 iteracones, cada vez moveindo menos hasta llegar
    #a 0, y luego comienza a bajar.
    #Durante la primera mitad, tiee que ir restando en el y, y en la segunda
    #mitad sumar. Para eso es la variable neg
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2)/2 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10

    #Poner a pantalla de un solo color, para que no se pinten figuras infinitas
    win.fill((122, 0, 255))

    """
    #Pintar un rectangulo, y los parámetros son pestaña, (R, G, B), (posicionX,
    #posicionY, anchura, altura)
    pygame.draw.rect(win, (255, 255, 0), (x, y, width, height))

    #Refrescar la ventana continuamente(Sin eso no funciona nada)
    pygame.display.update()
    """

pygame.quit()
