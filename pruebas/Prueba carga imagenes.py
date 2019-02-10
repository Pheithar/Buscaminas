
texto = open ("images.txt").readlines()
longitud_texto = len(texto)
i=0
for i in longitud_texto:
    elemento = texto.split()

    if elemento[0] == "0Cell":
        print(elemento[1])
