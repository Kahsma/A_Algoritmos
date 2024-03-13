import sys
import numpy as np
import time
#Camilo Martinez y Alberto vigna
def recursive_mult(A):
    """
    Calcula recursivamente el costo mínimo de multiplicar una cadena de matrices.

    Parámetros:
    A (list): Lista de enteros que representan las dimensiones de las matrices.

    Retorna:
    float: El costo mínimo de multiplicar las matrices.
    """
    n = len(A) - 1
    return recursive_mult_aux(1, n)

def recursive_mult_aux(i, j):
    """
    Calcula recursivamente el costo mínimo de multiplicar matrices desde el índice i hasta el índice j.

    Parámetros:
    i (int): El índice inicial de la cadena de matrices.
    j (int): El índice final de la cadena de matrices.

    Retorna:
    float: El costo mínimo de multiplicar las matrices.
    """
    if i == j:
        return 0
    
    min_cost = float('inf')
    for k in range(i, j):
        cost = recursive_mult_aux(i, k) + recursive_mult_aux(k+1, j) + A[i-1] * A[k] * A[j]
        if cost < min_cost:
            min_cost = cost
    
    return min_cost

def memoized_mult(A):
    """
    Calcula el costo mínimo de multiplicar matrices utilizando memoización.

    Parámetros:
    A (list): Lista de enteros que representan las dimensiones de las matrices.

    Retorna:
    float: El costo mínimo de multiplicar las matrices.
    """
    n = len(A)
    memo = [[-1] * n for _ in range(n)]
    
    cost = recursive_mult_memo(1, n-1, memo)
    return cost

def recursive_mult_memo(i, j, memo):
    """
    Calcula recursivamente el costo mínimo de multiplicar matrices desde el índice i hasta el índice j utilizando memoización.

    Parámetros:
    i (int): El índice inicial de la cadena de matrices.
    j (int): El índice final de la cadena de matrices.
    memo (list): Una tabla de memoización para almacenar los valores calculados previamente.

    Retorna:
    float: El costo mínimo de multiplicar las matrices desde el índice i hasta j.
    """
    if i == j:
        return 0
    
    if memo[i][j] != -1:
        return memo[i][j]
    memo[i][j] = float('inf')
    
    min_cost = float('inf')
    for k in range(i, j):
        if memo[i][k] == -1:
            memo[i][k] = recursive_mult_memo(i, k,memo)
        if memo[k+1][j] == -1:
            memo[k+1][j] = recursive_mult_memo(k+1, j,memo)
        
        cost = memo[i][k] + memo[k+1][j] + A[i-1] * A[k] * A[j]
        if cost < min_cost:
            min_cost = cost
    
    memo[i][j] = min_cost
    return min_cost

def bottom_up_mult(A):
    """
    Calcula el costo mínimo de multiplicar matrices utilizando el enfoque de abajo hacia arriba.

    Parámetros:
    A (list): Lista de enteros que representan las dimensiones de las matrices.

    Retorna:
    int: El costo mínimo de multiplicar las matrices.
    """
    n = len(A)
    dp = [[0] * n for _ in range(n)]
    
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i + L - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + A[i-1] * A[k] * A[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    
    return dp[1][n-1]
    
def mat_mult(A, mult_func):
    """
    Multiplica las matrices en la lista A utilizando la función de multiplicación especificada.

    Parámetros:
    A (list): Lista de matrices a multiplicar.
    mult_func (función): Función para realizar la multiplicación de matrices.

    Retorna:
    cost: El resultado de la multiplicación de matrices.
    """
    init = time.time_ns()
    n = len(A)
    cost = mult_func(A)
    end = time.time_ns()
    
    print(f'Tiempo total: {(end - init)} para {n} matrices usando {mult_func.__name__}')
    return cost

# Modificación de bottom-up para devolver la matriz de costos y usarla en find_solution_shorter y get_solution_tree
def bottom_up_mult_dp(A):
    """
    Calcula el costo mínimo de multiplicar matrices utilizando el enfoque de abajo hacia arriba.

    Parámetros:
    A (list): Lista de enteros que representan las dimensiones de las matrices.

    Retorna:
    dp (list): La matriz de costos mínimos.
    n (int): El tamaño de la lista de matrices.
    """
    n = len(A)
    dp = [[0] * n for _ in range(n)]
    
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i + L - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + A[i-1] * A[k] * A[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    
    return dp,n

def find_solution_shorter(A,M):
    """
    Encuentra la solución óptima para multiplicar matrices de manera más concisa.

    Parámetros:
    A (list): Lista de enteros que representan las dimensiones de las matrices.
    M (list): Matriz de costos mínimos.

    Retorna:
    lista (list): El orden óptimo para multiplicar las matrices.
    """
    n = len(A)
    lista = []
    lista.append(ingeniria_inversa(1,n-1,M))
    return lista

def ingeniria_inversa(i, j,M):
    """
    Trata la solución óptima para multiplicar matrices.

    Parámetros:
    i (int): Índice inicial de la cadena de matrices.
    j (int): Índice final de la cadena de matrices.
    M (list): Matriz de costos mínimos.

    Retorna:
    str: La solución óptima para multiplicar las matrices.
    """
    if i == j:
        return str(i)
    else:
        for k in range(i, j):
            if M[i][j] == M[i][k] + M[k+1][j] + A[i-1] * A[k] * A[j]:
                return f"({ingeniria_inversa(i, k,M)} x {ingeniria_inversa(k+1, j,M)})"

#Solución utilizando estructura de árbol formal, esta saca la memoria de la solución por si misma por eso no se necesita la matriz de costos.Esta solución esta escrita de una manera poco intutiva. la estructura se entiende mejor  enla  funcion find_solution_shorter. 
def get_solution_tree(A):
    """
    Obtiene los elementos necesarios para obtener la solución óptima utilizando una estructura de árbol.

    Parámetros:
    A (list): Lista de enteros que representan las dimensiones de las matrices.

    Retorna:
    list: Los elementos necesarios para obtener la solución óptima.
    """
    class Node:
        def __init__(self, i, j):
            self.i = i
            self.j = j
            self.children = []

    def build_tree(i, j):
        if i == j:
            return Node(i, j)

        root = Node(i, j)
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + A[i-1] * A[k] * A[j]
            if cost == dp[i][j]:
                root.children.append(build_tree(i, k))
                root.children.append(build_tree(k+1, j))
                break

        return root

    def traverse_tree(node):
        if not node.children:
            return [node.i]

        left = traverse_tree(node.children[0])
        right = traverse_tree(node.children[1])
        return left + right

    n = len(A)
    dp = [[0] * n for _ in range(n)]

    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i + L - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + A[i-1] * A[k] * A[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    root = build_tree(1, n-1)
    solution = traverse_tree(root)
    return solution



if len(sys.argv) < 2:
    print("Usage: python3", sys.argv[0], "input_file")
    sys.exit(1)

Af = open(sys.argv[1], 'r').readlines()
A = [int(a) for a in Af][1:]

print(A)
print(f"Recursive: {mat_mult(A,recursive_mult)}")
print(f"Memoized: {mat_mult(A, memoized_mult)}")
print(f"Bottom-up: {mat_mult(A, bottom_up_mult)}")
dp,n = bottom_up_mult_dp(A)
print(f"dp={dp}")
print(f"n={n}")
print(f"Solution (Tree): {get_solution_tree(A)}")
print(f"Solution option: {find_solution_shorter(A,dp)}")

