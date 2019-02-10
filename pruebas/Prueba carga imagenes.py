texto = open("../Juego/images.txt").readlines()
longitud_texto = len(texto)

for i in range(0, longitud_texto):
    elemento = texto[i].split()

    if elemento[0] == "1Cell":
        print(elemento[1])
