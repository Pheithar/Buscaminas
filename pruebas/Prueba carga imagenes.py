
print(open("images.txt"))

texto = open("images.txt").readlines()
longitud_texto = len(texto)

<<<<<<< HEAD
=======
for i in range(0, longitud_texto):
    elemento = texto[0].split()

>>>>>>> 4aed31b93c3ac5f2e24484e4bcd3013fcae7ef6d
    if elemento[0] == "0Cell":
        print(elemento[1])
