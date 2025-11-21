# Guía de Inicio Rápido

¡Bienvenido al Club de Robótica! Esta guía te ayudará a comenzar rápidamente.

## 🎯 Primeros pasos

### 1. Clonar el repositorio

```bash
git clone https://github.com/rxhdf/Club-robotica.git
cd Club-robotica
```

### 2. Explorar el contenido

El repositorio está organizado por temas:

- **IA/**: Inteligencia Artificial y Machine Learning
- **Python/**: Programación en Python
- **C++/**: Programación en C++
- **Matematicas/**: Matemáticas para programación e IA
- **Recursos/**: Herramientas y enlaces útiles

### 3. Ejecutar los ejemplos

#### Python

```bash
# Navegar a la carpeta de ejemplos
cd Python/ejemplos

# Ejecutar un ejemplo
python3 01_hola_mundo.py
```

#### C++

```bash
# Navegar a la carpeta de ejemplos
cd C++/ejemplos

# Compilar
g++ -std=c++11 01_hola_mundo.cpp -o hola_mundo

# Ejecutar
./hola_mundo
```

## 📚 Rutas de aprendizaje sugeridas

### Para principiantes absolutos

1. Comienza con **Python/ejemplos/**
   - `01_hola_mundo.py` - Tu primer programa
   - `02_listas_bucles.py` - Estructuras básicas
2. Intenta los ejercicios en **Python/ejercicios/**
3. Lee el **README.md** de cada carpeta para más recursos

### Para estudiantes intermedios

1. Explora **IA/ejemplos/** para machine learning básico
2. Revisa **Matematicas/ejemplos/** para fundamentos matemáticos
3. Practica con **C++/ejemplos/** si quieres aprender un lenguaje compilado

### Para estudiantes avanzados

1. Implementa tus propios proyectos usando los ejemplos como base
2. Contribuye al repositorio (ver **CONTRIBUTING.md**)
3. Explora los recursos avanzados en **Recursos/README.md**

## 🔧 Configuración del entorno

### Python

#### Windows
```bash
# Descargar desde python.org
python --version
pip --version
```

#### Linux/Mac
```bash
python3 --version
pip3 --version

# Instalar pip si no está disponible
sudo apt-get install python3-pip  # Ubuntu/Debian
```

#### Entorno virtual (recomendado)
```bash
python3 -m venv mi_entorno
source mi_entorno/bin/activate  # Linux/Mac
mi_entorno\Scripts\activate      # Windows
```

### C++

#### Windows
- Instalar MinGW-w64 o Visual Studio
- Verificar: `g++ --version`

#### Linux
```bash
sudo apt-get install build-essential
g++ --version
```

#### Mac
```bash
xcode-select --install
g++ --version
```

## 📦 Dependencias para ejemplos de IA

Si quieres ejecutar los ejemplos de Machine Learning:

```bash
pip install numpy pandas scikit-learn matplotlib
```

Para ejemplos de matemáticas:

```bash
pip install numpy scipy matplotlib
```

## 💡 Consejos útiles

### Para aprender efectivamente

1. **Lee el código antes de ejecutarlo** - Trata de entender qué hace
2. **Modifica los ejemplos** - Experimenta cambiando valores
3. **Resuelve los ejercicios** - La práctica es fundamental
4. **Haz preguntas** - Abre un issue si tienes dudas

### Para no frustrarte

- No trates de aprender todo a la vez
- Está bien cometer errores
- Los mensajes de error son tus amigos (te dicen qué arreglar)
- Tómate descansos cuando sea necesario

## 🚀 Proyectos para practicar

### Proyectos de Python (dificultad creciente)

1. ✅ Completar **Python/ejercicios/ejercicio_01_calculadora.py**
2. 📝 Hacer un programa de lista de tareas
3. 🎮 Crear un juego simple (piedra, papel, tijera)
4. 📊 Analizar un dataset con pandas
5. 🤖 Entrenar tu primer modelo de ML

### Proyectos de C++

1. ✅ Completar **C++/ejercicios/ejercicio_01_calculadora.cpp**
2. 📚 Sistema de gestión de biblioteca
3. 🎲 Juego de texto (aventura, RPG)
4. 🗄️ Implementar estructuras de datos (pila, cola, árbol)

## 📖 Recursos adicionales

- [Python.org](https://www.python.org/) - Documentación oficial
- [cppreference.com](https://en.cppreference.com/) - Referencia de C++
- [3Blue1Brown](https://www.youtube.com/c/3blue1brown) - Matemáticas visuales
- [Kaggle Learn](https://www.kaggle.com/learn) - Tutoriales de ML

## 🤝 Contribuir

¿Quieres agregar tus propios ejemplos o mejorar los existentes?
Lee **CONTRIBUTING.md** para saber cómo contribuir.

## ❓ Obtener ayuda

- 📖 Lee el README.md de cada carpeta para más detalles
- 💬 Abre un issue con tus preguntas
- 🔍 Busca en los recursos listados en **Recursos/README.md**

---

¡Feliz aprendizaje! 🎉
Jesus armando