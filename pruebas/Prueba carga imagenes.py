
texto = open("../Juego/images.txt", "r").readlines()
longitud_texto = len(texto)

<<<<<<< HEAD
=======
for i in range(0, longitud_texto):
    elemento = texto[i].split()

<<<<<<< HEAD
    if elemento[0] == "1Cell":
=======
>>>>>>> 4aed31b93c3ac5f2e24484e4bcd3013fcae7ef6d
    if elemento[0] == "0Cell":
>>>>>>> dde0056a4cffe1f87c18935970ba6b49fbf49284
        print(elemento[1])
