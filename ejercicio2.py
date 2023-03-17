"""
Realiza el  código para calcular el determinante de una matriz cuadrada de [3 x 3], regla de Sarrus de forma recursiva y de forma iterativa
"""

# Matriz de ejemplo
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Cálculo del determinante utilizando la regla de Sarrus de forma recursiva
def determinant_sarrus_recursive(matrix):
    if len(matrix) == 2:
        return (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
    elif len(matrix) == 3:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[0][2]
        d = matrix[1][0]
        e = matrix[1][1]
        f = matrix[1][2]
        g = matrix[2][0]
        h = matrix[2][1]
        i = matrix[2][2]
        first = a*e*i + b*f*g + c*d*h
        second = c*e*g + b*d*i + a*f*h
        return first - second
    else:
        determinant = 0
        for i in range(len(matrix)):
            sub_matrix = [row[:i] + row[i+1:] for row in matrix[1:]]
            sign = (-1) ** i
            sub_determinant = determinant_sarrus_recursive(sub_matrix)
            determinant += sign * matrix[0][i] * sub_determinant
        return determinant

# Cálculo del determinante utilizando la regla de Sarrus de forma iterativa
def determinant_sarrus_iterative(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]
    d = matrix[1][0]
    e = matrix[1][1]
    f = matrix[1][2]
    g = matrix[2][0]
    h = matrix[2][1]
    i = matrix[2][2]
    first = a*e*i + b*f*g + c*d*h
    second = c*e*g + b*d*i + a*f*h
    return first - second

# Resultados
print("Matriz:", matrix)
print("Determinante (forma recursiva):", determinant_sarrus_recursive(matrix))
print("Determinante (forma iterativa):", determinant_sarrus_iterative(matrix))
