
#texto = open("ppp.txt")
texto = open("../Juego/images.txt")
lineas = texto.readlines()
longitud_texto = len(lineas)

print(lineas[0])

for i in range(0, longitud_texto):
    elemento = lineas[i].split()
    if elemento[0] == "1Cell":
        print(elemento[1])
