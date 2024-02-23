import sys

def contar_caracteres_distintos(texto):
    # Usamos un conjunto para almacenar caracteres únicos
    caracteres_unicos = set(texto)
    #caracteres_unicos.discard(' ')
    return len(caracteres_unicos)

def contar_palabras_distintas(texto):
    # Dividimos el texto en palabras y usamos un conjunto para almacenar palabras únicas
    palabras_unicas = (texto.split())
    return len(palabras_unicas)

def main(archivo):
    # Leer el archivo de texto
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            texto = file.read()
    except FileNotFoundError:
        print(f"No se encontró el archivo: {archivo}")
        return

    # Realizar conteos
    num_caracteres_distintos = contar_caracteres_distintos(texto)
    num_palabras_distintas = contar_palabras_distintas(texto)

    # Imprimir los resultados
    print(f"El número de caracteres distintos es: {num_caracteres_distintos}")
    print(f"El número de palabras distintas es: {num_palabras_distintas}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Uso: python word_count.py <archivo>")
