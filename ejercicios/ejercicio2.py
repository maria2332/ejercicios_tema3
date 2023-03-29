"""
Realiza el  código para calcular el determinante de una matriz cuadrada de [3 x 3], regla de Sarrus de forma recursiva y de forma iterativa
"""

class Matriz3x3:
    def _init_(self, elementos):
        if len(elementos) != 3 or not all(len(row) == 3 for row in elementos):
            raise ValueError("La matriz debe ser de tamaño 3x3")
        self.elementos = elementos

def determinante_iterativo(matriz):
    if len(matriz) != 3 or not all(len(row) == 3 for row in matriz):
        raise ValueError("La matriz debe ser de tamaño 3x3")
        
    det = 0
    for i in range(3):
        prod_pos = 1
        prod_neg = 1
        for j in range(3):
            prod_pos *= matriz[j][(i+j) % 3]
            prod_neg *= matriz[j][(i-j) % 3]
        det += prod_pos - prod_neg
    return det

def determinante_recursivo(matriz):
    n = len(matriz)
    if not all(len(row) == n for row in matriz):
        raise ValueError("La matriz debe ser cuadrada")

    if n == 1:
        return matriz[0][0]
    elif n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    else:
        det = 0
        for i in range(n):
            submatriz = [row[:i] + row[i+1:] for row in matriz[1:]]
            det += matriz[0][i] * ((-1) ** i) * determinante_recursivo(submatriz)
        return det

# Ejemplo de uso
matriz_3x3 = [
    [2, 3, 1],
    [4, 1, 3],
    [3, 2, 1]
]

print("Determinante iterativo (Regla de Sarrus): ", determinante_iterativo(matriz_3x3))
print("Determinante recursivo (Expansión por cofactores): ", determinante_recursivo(matriz_3x3))