"""
Ejemplo de álgebra lineal con NumPy
Operaciones básicas con matrices y vectores
"""

import numpy as np

def operaciones_vectores():
    """Ejemplos de operaciones con vectores."""
    print("=== Operaciones con Vectores ===\n")
    
    # Crear vectores
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    
    print(f"Vector v1: {v1}")
    print(f"Vector v2: {v2}\n")
    
    # Suma de vectores
    suma = v1 + v2
    print(f"v1 + v2 = {suma}")
    
    # Resta de vectores
    resta = v1 - v2
    print(f"v1 - v2 = {resta}")
    
    # Producto escalar (dot product)
    producto_escalar = np.dot(v1, v2)
    print(f"v1 · v2 = {producto_escalar}")
    
    # Norma del vector (magnitud)
    norma_v1 = np.linalg.norm(v1)
    print(f"||v1|| = {norma_v1:.2f}\n")

def operaciones_matrices():
    """Ejemplos de operaciones con matrices."""
    print("=== Operaciones con Matrices ===\n")
    
    # Crear matrices
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    print("Matriz A:")
    print(A)
    print("\nMatriz B:")
    print(B)
    print()
    
    # Suma de matrices
    suma = A + B
    print("A + B =")
    print(suma)
    print()
    
    # Multiplicación de matrices
    producto = np.dot(A, B)
    # O también: producto = A @ B
    print("A × B =")
    print(producto)
    print()
    
    # Transpuesta
    A_T = A.T
    print("A^T =")
    print(A_T)
    print()
    
    # Determinante
    det_A = np.linalg.det(A)
    print(f"det(A) = {det_A:.2f}")
    
    # Inversa
    if det_A != 0:
        A_inv = np.linalg.inv(A)
        print("\nA^(-1) =")
        print(A_inv)
        
        # Verificar: A × A^(-1) = I
        identidad = np.dot(A, A_inv)
        print("\nA × A^(-1) =")
        print(np.round(identidad, 2))
    
    print()

def valores_propios():
    """Ejemplo de valores y vectores propios."""
    print("=== Valores y Vectores Propios ===\n")
    
    # Crear una matriz
    A = np.array([[4, 2], [1, 3]])
    
    print("Matriz A:")
    print(A)
    print()
    
    # Calcular valores y vectores propios
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    print("Valores propios (λ):")
    print(eigenvalues)
    print()
    
    print("Vectores propios:")
    print(eigenvectors)
    print()
    
    # Verificar: A × v = λ × v
    for i in range(len(eigenvalues)):
        v = eigenvectors[:, i]
        lambda_i = eigenvalues[i]
        
        Av = np.dot(A, v)
        lambda_v = lambda_i * v
        
        print(f"Para λ{i+1} = {lambda_i:.2f}:")
        print(f"A × v = {Av}")
        print(f"λ × v = {lambda_v}")
        print(f"¿Son iguales? {np.allclose(Av, lambda_v)}")
        print()

if __name__ == "__main__":
    # Nota: Necesitas instalar NumPy
    # pip install numpy
    
    try:
        operaciones_vectores()
        operaciones_matrices()
        valores_propios()
    except ImportError:
        print("Error: NumPy no está instalado.")
        print("Instala NumPy con: pip install numpy")
