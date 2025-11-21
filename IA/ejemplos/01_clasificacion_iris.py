"""
Ejemplo básico de Machine Learning con scikit-learn
Clasificación de flores Iris usando k-Nearest Neighbors
"""

# Importar bibliotecas necesarias
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

def ejemplo_clasificacion_iris():
    """
    Ejemplo de clasificación con el dataset Iris.
    Este es uno de los datasets más famosos en Machine Learning.
    """
    print("=== Clasificación de Flores Iris ===\n")
    
    # 1. Cargar el dataset
    iris = load_iris()
    X = iris.data  # Características (features)
    y = iris.target  # Etiquetas (labels)
    
    print(f"Forma del dataset: {X.shape}")
    print(f"Número de clases: {len(np.unique(y))}")
    print(f"Nombres de características: {iris.feature_names}")
    print(f"Nombres de clases: {iris.target_names}\n")
    
    # 2. Dividir en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    
    print(f"Tamaño del conjunto de entrenamiento: {len(X_train)}")
    print(f"Tamaño del conjunto de prueba: {len(X_test)}\n")
    
    # 3. Crear y entrenar el modelo
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    
    print("Modelo entrenado exitosamente!\n")
    
    # 4. Hacer predicciones
    y_pred = knn.predict(X_test)
    
    # 5. Evaluar el modelo
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Precisión del modelo: {accuracy:.2%}\n")
    
    print("Reporte de clasificación:")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))
    
    # 6. Ejemplo de predicción individual
    # Características de una nueva flor
    nueva_flor = [[5.1, 3.5, 1.4, 0.2]]
    prediccion = knn.predict(nueva_flor)
    nombre_clase = iris.target_names[prediccion[0]]
    
    print(f"\nPredicción para una nueva flor {nueva_flor[0]}:")
    print(f"Clase predicha: {nombre_clase}")

if __name__ == "__main__":
    # Nota: Necesitas instalar scikit-learn
    # pip install scikit-learn numpy
    
    try:
        ejemplo_clasificacion_iris()
    except ImportError:
        print("Error: No se encontraron las bibliotecas necesarias.")
        print("Instala las dependencias con:")
        print("pip install scikit-learn numpy")
