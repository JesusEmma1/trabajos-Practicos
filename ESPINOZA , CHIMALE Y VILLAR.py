import numpy as np
import math

def contar_digitos():
    num = input("Ingrese un número entero: ")
    print(f"Cantidad de dígitos: {len(num)}")

def contar_digitos_decimales():
    num = input("Ingrese un número decimal: ")
    entero, decimal = num.split('.') if '.' in num else (num, '')
    print(f"Dígitos en la parte entera: {len(entero)}, Dígitos en la parte decimal: {len(decimal)}")

def es_compuesto(n):
    if n < 2:
        return False
    return sum(n % i == 0 for i in range(1, n+1)) > 2

def numeros_compuestos():
    lista = list(map(int, input("Ingrese una lista de números separados por espacio: ").split()))
    print(f"Números compuestos: { [n for n in lista if es_compuesto(n)] }")

def invertir_vector():
    vector = input("Ingrese una lista de números separados por espacio: ").split()
    print(f"Vector invertido: {vector[::-1]}")

def filtrar_lista():
    lista = list(map(float, input("Ingrese una lista de números decimales separados por espacio: ").split()))
    resultado = [x for x in lista if sum(int(d) % 2 == 0 for d in str(int(x))) == 2 or sum(int(d) % 2 != 0 for d in str(int(x))) >= 2]
    print(f"Lista filtrada: {resultado}")

def insertar_k():
    lista = list(map(int, input("Ingrese una lista de números separados por espacio: ").split()))
    k = int(input("Ingrese el valor de k: "))
    resultado = []
    for num in lista:
        resultado.append(num)
        if num % k == 0:
            resultado.append(k)
    print(f"Lista modificada: {resultado}")

def promedios_matriz():
    m = int(input("Ingrese el número de filas de la matriz: "))
    n = int(input("Ingrese el número de columnas de la matriz: "))
    matriz = np.array([list(map(int, input(f"Fila {i+1}: ").split())) for i in range(m)])
    print(f"Matriz: \n{matriz}")
    print(f"Promedio por fila: {matriz.mean(axis=1)}")
    print(f"Promedio por columna: {matriz.mean(axis=0)}")

def matriz_factorial():
    m = int(input("Ingrese el tamaño de la matriz cuadrada: "))
    matriz = np.array([list(map(int, input(f"Fila {i+1}: ").split())) for i in range(m)])
    suma_diagonal = np.sum(np.diagonal(matriz))
    vector = list(set([num for fila in matriz for num in fila if math.factorial(num) >= suma_diagonal]))
    print(f"Matriz: \n{matriz}")
    print(f"Vector con números cuyo factorial es mayor o igual a {suma_diagonal}: {vector}")

def punto_silla():
    m = int(input("Ingrese el número de filas de la matriz: "))
    n = int(input("Ingrese el número de columnas de la matriz: "))
    matriz = np.array([list(map(int, input(f"Fila {i+1}: ").split())) for i in range(m)])
    k, h = map(int, input("Ingrese las coordenadas (fila columna) del punto a verificar: ").split())
    if k >= m or h >= n:
        print("Error: Índices fuera de rango")
        return
    es_punto_silla = matriz[k, h] == max(matriz[k, :]) and matriz[k, h] == min(matriz[:, h])
    print(f"Matriz: \n{matriz}")
    print(f"El punto en ({k}, {h}) es punto silla: {es_punto_silla}")

def es_simetrica():
    n = int(input("Ingrese el tamaño de la matriz cuadrada: "))
    matriz = np.array([list(map(int, input(f"Fila {i+1}: ").split())) for i in range(n)])
    print(f"Matriz: \n{matriz}")
    print(f"Es simétrica: {np.array_equal(matriz, matriz.T)}")

def ejecutar_ejemplo():
    opciones = {
        "1": contar_digitos,
        "2": contar_digitos_decimales,
        "3": numeros_compuestos,
        "4": invertir_vector,
        "5": filtrar_lista,
        "6": insertar_k,
        "7": promedios_matriz,
        "8": matriz_factorial,
        "9": punto_silla,
        "10": es_simetrica,
    }
    try:
        while True:
            print("\nMenú de opciones:")
            for i, key in enumerate(opciones.keys(), 1):
                print(f"{key}. {opciones[key].__name__}")
            print("0. Salir")
            try:
                opcion = input("Seleccione una opción: ")
                if opcion == "0":
                    break
                elif opcion in opciones:
                    opciones[opcion]()
                else:
                    print("Opción no válida. Intente de nuevo.")
            except EOFError:
                print("Entrada no disponible. Terminando programa.")
                break
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")

if __name__ == "__main__":
    ejecutar_ejemplo()
