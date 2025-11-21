# C++

Bienvenido a la sección de C++. Aquí encontrarás recursos para aprender programación en C++ desde lo básico hasta temas avanzados.

## 📖 Contenido

### Nivel Básico
- Instalación y configuración del compilador
- Estructura de un programa en C++
- Variables y tipos de datos
- Operadores
- Entrada y salida (cin/cout)
- Estructuras de control (if, switch, loops)
- Funciones
- Arrays y strings

### Nivel Intermedio
- Punteros y referencias
- Memoria dinámica (new/delete)
- Estructuras y uniones
- Programación orientada a objetos
  - Clases y objetos
  - Constructores y destructores
  - Herencia
  - Polimorfismo
  - Encapsulamiento
- Manejo de archivos
- Plantillas (Templates)

### Nivel Avanzado
- STL (Standard Template Library)
  - Containers (vector, list, map, set)
  - Iteradores
  - Algoritmos
- Smart pointers
- Move semantics
- Lambda expressions
- Multithreading
- Exception handling
- C++11/14/17/20 features

## 🔧 Instalación

### Windows
```bash
# MinGW-w64
# O Visual Studio con C++
# O CLion IDE

g++ --version
```

### Linux
```bash
# GCC/G++
sudo apt-get install build-essential  # Ubuntu/Debian
sudo yum install gcc-c++  # Fedora/RHEL

g++ --version
```

### macOS
```bash
# Xcode Command Line Tools
xcode-select --install

# O Homebrew
brew install gcc

g++ --version
```

## 🏗️ Compilación básica

```bash
# Compilar un programa simple
g++ programa.cpp -o programa

# Ejecutar
./programa  # Linux/Mac
programa.exe  # Windows

# Con flags de optimización
g++ -O2 -Wall -std=c++17 programa.cpp -o programa

# Con depuración
g++ -g programa.cpp -o programa
```

## 📚 Recursos adicionales

### Documentación
- [cppreference.com](https://en.cppreference.com/)
- [cplusplus.com](http://www.cplusplus.com/)
- [ISO C++ Standards](https://isocpp.org/)

### Tutoriales
- [LearnCpp.com](https://www.learncpp.com/)
- [GeeksforGeeks C++](https://www.geeksforgeeks.org/c-plus-plus/)
- [C++ Tutorial for Beginners](https://www.youtube.com/watch?v=vLnPwxZdW4Y)

### Libros
- "C++ Primer" por Stanley Lippman
- "Effective C++" por Scott Meyers
- "The C++ Programming Language" por Bjarne Stroustrup
- "Modern C++ Design" por Andrei Alexandrescu

### Práctica
- [HackerRank C++](https://www.hackerrank.com/domains/cpp)
- [LeetCode](https://leetcode.com/)
- [Codeforces](https://codeforces.com/)
- [Project Euler](https://projecteuler.net/)

## 🎯 Proyectos sugeridos

1. **Calculadora simple**
2. **Sistema de gestión de estudiantes**
3. **Juego de texto (aventura, batalla)**
4. **Implementación de estructuras de datos**
   - Lista enlazada
   - Pila (Stack)
   - Cola (Queue)
   - Árbol binario
5. **Mini base de datos en archivos**
6. **Simulador de sistema bancario**
7. **Parser de expresiones matemáticas**
8. **Sistema de gestión de biblioteca**

## 💡 Mejores prácticas

### Estilo de código
- Usa nombres descriptivos para variables y funciones
- Indentación consistente (2 o 4 espacios)
- Comentarios claros y concisos
- Una responsabilidad por función

### Gestión de memoria
- Siempre libera la memoria que aloques
- Prefiere smart pointers sobre punteros raw
- Evita memory leaks
- Usa herramientas como Valgrind

### Seguridad
- Valida entrada de usuario
- Evita buffer overflows
- No uses funciones inseguras (gets, strcpy sin límite)
- Compila con warnings (-Wall -Wextra)

### Modern C++
- Prefiere auto cuando el tipo es obvio
- Usa range-based for loops
- Usa nullptr en lugar de NULL
- Usa constexpr cuando sea posible
- Usa std::array en lugar de arrays C

## 🔨 Herramientas útiles

### IDEs
- Visual Studio
- Visual Studio Code con extensiones
- CLion
- Code::Blocks
- Eclipse CDT

### Compiladores
- GCC/G++
- Clang
- MSVC (Microsoft Visual C++)

### Depuradores
- GDB
- LLDB
- Visual Studio Debugger

### Análisis de código
- Valgrind (memory leaks)
- Clang-Tidy (static analysis)
- Cppcheck
- AddressSanitizer

## 📝 Ejemplo básico

```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
    std::vector<std::string> mensajes {"Hola", "Club", "Robótica"};
    
    for (const auto& mensaje : mensajes) {
        std::cout << mensaje << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
```
