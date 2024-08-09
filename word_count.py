#Solicitamos al usuario que ingrese nombre del archivo .txt a procesar

archivo = input("Ingresa el nombre del archivo de texto incluyendo su extensión '.txt', ejemplo; texto.txt: ")
try:
    with open(archivo, "r") as file:
        texto = file.read()
        palabras = len(set(texto.split()))
        letras = len(set(texto))
        print(f"El número de caracteres distintos es: {letras}")
        print(f"El número de palabras distintas es: {palabras}")
except IndexError:
    print("Por favor, ingrese el nombre del archivo como argumento.")