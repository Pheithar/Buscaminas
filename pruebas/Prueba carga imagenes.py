
texto = open("../Juego/images.txt", "r").readlines()
longitud_texto = len(texto)

for i in range(0, longitud_texto):
    elemento = texto[i].split()
    if elemento[0] == "1Cell":
    if elemento[0] == "0Cell":
        print(elemento[1])
