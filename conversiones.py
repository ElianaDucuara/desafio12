import sys

def convertir_divisas(tasa_sol, tasa_peso_argentino, tasa_dolar_americano, monto_chileno):
    soles = monto_chileno * tasa_sol
    pesos_argentinos = monto_chileno * tasa_peso_argentino
    dolares = monto_chileno * tasa_dolar_americano
    return soles, pesos_argentinos, dolares

def main():
    if len(sys.argv) != 5:
        print("Uso: python conversiones.py <tasa_sol> <tasa_peso_argentino> <tasa_dolar_americano> <monto_chileno>")
        return

    # Conversión de argumentos a tipos de datos adecuados
    tasa_sol = float(sys.argv[1])
    tasa_peso_argentino = float(sys.argv[2])
    tasa_dolar_americano = float(sys.argv[3])
    monto_chileno = float(sys.argv[4])

    # Realizar conversión
    soles, pesos_argentinos, dolares = convertir_divisas(
        tasa_sol, tasa_peso_argentino, tasa_dolar_americano, monto_chileno
    )

    print(f"Los {monto_chileno} pesos equivalen a:")
    print(f"{soles} Soles")
    print(f"{pesos_argentinos} Pesos Argentinos")
    print(f"{dolares} Dólares")

if __name__ == "__main__":
    main()
