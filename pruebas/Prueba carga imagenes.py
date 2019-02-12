<<<<<<< HEAD

#texto = open("ppp.txt")
texto = open("../Juego/images.txt")
lineas = texto.readlines()
longitud_texto = len(lineas)

print(lineas[0])

for i in range(0, longitud_texto):
    elemento = lineas[i].split()
=======
texto = open("../Juego/images.txt").readlines()
longitud_texto = len(texto)

for i in range(0, longitud_texto):
    elemento = texto[i].split()

>>>>>>> 94e23c591f2b40fb82e8109b0f23ccb37004bbdf
    if elemento[0] == "1Cell":
        print(elemento[1])
