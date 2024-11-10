import numpy as np

# Tamaño del grafo (número de nodos)
size = 4

# Inicializa el nodo visitado y otras variables
visitado = [0]  # Lista de nodos ya en el MST
pares = []       # Lista de arcos en el MST

# Entrada en formato de texto: Matriz de adyacencia del grafo (simétrica y completa)
entrada = """
0 16 45 32
16 0 18 21
45 18 0 7
32 21 7 0
"""

matriz = np.array([list(map(int, fila.split())) for fila in entrada.strip().splitlines()])

nodoActual = 0  
for i in range(size - 1):  
    menor = 99999
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

print("Lista de arcos de la forma (A,B), para clabear las colonias")
for par in pares:
    print(chr(par[0]+ 65),chr(par[1]+ 65))
    

# Variables para el algoritmo TSP (vecino más cercano)
n = size
visitado = [False] * n
ruta = []
costo_total = 0

# Nodo inicial
nodo_actual = 0
visitado[nodo_actual] = True
ruta.append(nodo_actual)


for _ in range(n - 1):
    menor = float('inf')
    siguiente_nodo = -1

    # Encuentra el vecino más cercano no visitado
    for j in range(n):
        if not visitado[j] and 0 < matriz[nodo_actual][j] < menor:
            menor = matriz[nodo_actual][j]
            siguiente_nodo = j

    # Mueve al siguiente nodo
    visitado[siguiente_nodo] = True
    ruta.append(siguiente_nodo)
    costo_total += menor
    nodo_actual = siguiente_nodo

# Volver al nodo inicial
ruta.append(0)
costo_total += matriz[nodo_actual][0]

# Convertir nodos a letras (A, B, C, ...)
ruta_letras = [chr(65 + i) for i in ruta]

# Mostrar la ruta y el costo total
print(("Ruta a seguir:", " -> ".join(ruta_letras)))
print("Costo total:", costo_total)