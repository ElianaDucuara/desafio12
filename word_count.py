import sys

# Función para contar caracteres distintos
def contar_caracteres_distintos(texto):
    return len(set(texto))

# Función para contar palabras distintas
def contar_palabras_distintas(texto):
    palabras = texto.split()
    return len(set(palabras))
    #return palabras

def main(archivo):
    # Abrir el archivo para leer
    with open(archivo, "r", encoding="utf-8") as file:
        texto = file.read()

    # Conteo
    num_caracteres_distintos = contar_caracteres_distintos(texto)
    num_palabras_distintas = contar_palabras_distintas(texto)

    # print resultados
    print(f"El número de caracteres distintos es: {num_caracteres_distintos}")
    print(f"El número de palabras distintas es: {num_palabras_distintas}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Por favor, ingresa el nombre del archivo de texto como argumento.")
