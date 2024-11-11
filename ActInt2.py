import numpy as np
from collections import deque

def leer_entrada():
    # Leer el número de nodos
    size = int(input("Ingrese el número de colonias: "))
    
    # Leer la matriz de distancias
    matriz_distancias = []
    print("Ingrese la matriz de distancias:")
    for _ in range(size):
        fila = list(map(int, input().strip().split()))
        matriz_distancias.append(fila)
    matriz_distancias = np.array(matriz_distancias)
    
    # Leer la matriz de capacidades de transmisión
    matriz_capacidades = []
    print("Ingrese la matriz de capacidades de transmisión:")
    for _ in range(size):
        fila = list(map(int, input().strip().split()))
        matriz_capacidades.append(fila)
    matriz_capacidades = np.array(matriz_capacidades)
    
    return size, matriz_distancias, matriz_capacidades

def mostrar_matriz_kms(size, matriz):
    print("\nKms de colonia a colonia\n")
    for fila in matriz:
        print(" ".join(map(str, fila)))
    print("\nSalida:")
    
    letras = [chr(65 + i) for i in range(size)]
    for i in range(size):
        for j in range(size):
            if i != j:
                print(f"Km de colonia {letras[i]} a colonia {letras[j]}: {matriz[i][j]}")
    print()

def cableado_minimo(size, matriz):
    visitado = [0]  
    pares = []
    nodoActual = 0
    
    for _ in range(size - 1):  
        menor = float('inf')
        siguienteNodo = -1
        
        for nodo in visitado:
            for j in range(size):
                if j not in visitado and matriz[nodo][j] != 0 and matriz[nodo][j] < menor:
                    menor = matriz[nodo][j]
                    siguienteNodo = j
                    nodoActual = nodo
        
        if siguienteNodo != -1:
            pares.append([nodoActual, siguienteNodo, menor])
            visitado.append(siguienteNodo)
    
    return pares

def mostrar_tsp_ruta(size, matriz):
    visitado = [False] * size
    ruta = []
    nodo_actual = 0
    visitado[nodo_actual] = True
    ruta.append(nodo_actual)

    for _ in range(size - 1):
        menor = float('inf')
        siguiente_nodo = -1

        for j in range(size):
            if not visitado[j] and 0 < matriz[nodo_actual][j] < menor:
                menor = matriz[nodo_actual][j]
                siguiente_nodo = j

        visitado[siguiente_nodo] = True
        ruta.append(siguiente_nodo)
        nodo_actual = siguiente_nodo

    ruta.append(0)
    ruta_letras = [chr(65 + i) for i in ruta]
    
    print("Camino más corto:", " ---> ".join(ruta_letras))
    print()

def bfs(capacidades, fuente, sumidero, padre):
    visitado = [False] * len(capacidades)
    cola = deque([fuente])
    visitado[fuente] = True
    
    while cola:
        u = cola.popleft()
        for v, capacidad in enumerate(capacidades[u]):
            if not visitado[v] and capacidad > 0:
                cola.append(v)
                visitado[v] = True
                padre[v] = u
                if v == sumidero:
                    return True
    return False

def flujo_maximo(capacidades, fuente, sumidero):
    n = len(capacidades)
    flujo_total = 0
    padre = [-1] * n
    
    while bfs(capacidades, fuente, sumidero, padre):
        flujo_camino = float('Inf')
        v = sumidero
        while v != fuente:
            u = padre[v]
            flujo_camino = min(flujo_camino, capacidades[u][v])
            v = u
        
        v = sumidero
        while v != fuente:
            u = padre[v]
            capacidades[u][v] -= flujo_camino
            capacidades[v][u] += flujo_camino
            v = u
        
        flujo_total += flujo_camino
    
    return flujo_total

def mostrar_matriz_capacidades(matriz):
    print("Capacidades máximas de transmisión\n")
    print("Entrada:")
    for fila in matriz:
        print(" ".join(map(str, fila)))

# Programa principal
size, matriz_distancias, matriz_capacidades = leer_entrada()

# Número de nodos
print(f"\nNúmero de nodos: {size}")

# Mostrar matriz de kms y los kms detallados entre colonias
mostrar_matriz_kms(size, matriz_distancias)

# Punto 1: Calcular el cableado óptimo
pares = cableado_minimo(size, matriz_distancias)

# Punto 2: Calcular la ruta mínima de TSP
mostrar_tsp_ruta(size, matriz_distancias)

# Punto 3: Mostrar matriz de capacidades y calcular flujo máximo
mostrar_matriz_capacidades(matriz_capacidades)
fuente = 0
sumidero = size - 1
flujo_total = flujo_maximo(matriz_capacidades.tolist(), fuente, sumidero)
print("\nSalida:")
print("Flujo máximo:", flujo_total)