
print(open("images.txt"))

texto = open("images.txt").readlines()
longitud_texto = len(texto)

for i in range(0, longitud_texto):
    elemento = texto[0].split()

    if elemento[0] == "0Cell":
        print(elemento[1])
