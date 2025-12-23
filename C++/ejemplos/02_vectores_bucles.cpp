/*
 * Ejemplo de vectores y bucles en C++
 * Demuestra el uso de vector<T> y diferentes tipos de bucles.
 */

#include <iostream>
#include <vector>
#include <string>

using namespace std;

void ejemplo_vectores() {
    cout << "=== Ejemplo de Vectores ===" << endl;
    
    // Crear un vector de enteros
    vector<int> numeros = {1, 2, 3, 4, 5};
    
    // Mostrar elementos
    cout << "Vector de números: ";
    for (int num : numeros) {
        cout << num << " ";
    }
    cout << endl;
    
    // Agregar elementos
    numeros.push_back(6);
    numeros.push_back(7);
    
    cout << "Después de push_back: ";
    for (int num : numeros) {
        cout << num << " ";
    }
    cout << endl;
    
    // Acceso por índice
    cout << "Primer elemento: " << numeros[0] << endl;
    cout << "Último elemento: " << numeros[numeros.size() - 1] << endl;
    
    // Vector de strings
    vector<string> frutas = {"manzana", "banana", "naranja", "uva"};
    cout << "\nFrutas:" << endl;
    for (size_t i = 0; i < frutas.size(); i++) {
        cout << i << ": " << frutas[i] << endl;
    }
}

void ejemplo_bucles() {
    cout << "\n=== Ejemplo de Bucles ===" << endl;
    
    // For tradicional
    cout << "For tradicional:" << endl;
    for (int i = 0; i < 5; i++) {
        cout << "i = " << i << endl;
    }
    
    // While loop
    cout << "\nWhile loop:" << endl;
    int contador = 0;
    while (contador < 5) {
        cout << "Contador: " << contador << endl;
        contador++;
    }
    
    // Do-while loop
    cout << "\nDo-while loop:" << endl;
    int j = 0;
    do {
        cout << "j = " << j << endl;
        j++;
    } while (j < 3);
}

int main() {
    ejemplo_vectores();
    ejemplo_bucles();
    
    return 0;
}
