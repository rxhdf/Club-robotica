"""
Ejemplo de lista y bucles en Python
Demuestra el uso de listas y diferentes tipos de bucles.
"""

def ejemplo_listas():
    """Ejemplos con listas."""
    # Crear una lista
    numeros = [1, 2, 3, 4, 5]
    print("Lista de números:", numeros)
    
    # Agregar elementos
    numeros.append(6)
    print("Después de append:", numeros)
    
    # Recorrer con for
    print("\nRecorriendo la lista:")
    for num in numeros:
        print(f"Número: {num}")
    
    # List comprehension
    cuadrados = [x**2 for x in numeros]
    print("\nCuadrados:", cuadrados)
    
    # Lista de strings
    frutas = ["manzana", "banana", "naranja", "uva"]
    print("\nFrutas:", frutas)
    
    # Filtrar lista
    frutas_largas = [fruta for fruta in frutas if len(fruta) > 5]
    print("Frutas con más de 5 letras:", frutas_largas)

def ejemplo_bucles():
    """Ejemplos de diferentes tipos de bucles."""
    # While loop
    print("\nContando con while:")
    contador = 0
    while contador < 5:
        print(f"Contador: {contador}")
        contador += 1
    
    # For con range
    print("\nUsando range:")
    for i in range(5):
        print(f"i = {i}")
    
    # For con enumerate
    print("\nUsando enumerate:")
    colores = ["rojo", "verde", "azul"]
    for indice, color in enumerate(colores):
        print(f"Color {indice}: {color}")

if __name__ == "__main__":
    ejemplo_listas()
    ejemplo_bucles()
