# Guía de Contribución

¡Gracias por tu interés en contribuir al Club de Robótica! 🎉

## Cómo contribuir

### 1. Reportar errores o sugerir mejoras

Si encuentras un error o tienes una sugerencia:
1. Verifica que no exista un issue similar
2. Crea un nuevo issue describiendo el problema o sugerencia
3. Proporciona detalles y ejemplos cuando sea posible

### 2. Contribuir con código o materiales

#### Proceso general

1. **Fork** el repositorio
2. **Clona** tu fork localmente:
   ```bash
   git clone https://github.com/tu-usuario/Club-robotica.git
   ```
3. **Crea una rama** para tus cambios:
   ```bash
   git checkout -b nombre-de-tu-rama
   ```
4. **Realiza tus cambios** siguiendo las guías de estilo
5. **Commit** tus cambios:
   ```bash
   git add .
   git commit -m "Descripción clara de los cambios"
   ```
6. **Push** a tu fork:
   ```bash
   git push origin nombre-de-tu-rama
   ```
7. **Crea un Pull Request** desde tu fork al repositorio principal

### 3. Tipos de contribuciones

#### Código de ejemplo
- Debe ser claro y bien comentado
- Incluir docstrings o comentarios explicativos
- Seguir las convenciones del lenguaje
- Incluir instrucciones de ejecución si es necesario

#### Ejercicios
- Debe tener una descripción clara del problema
- Incluir pistas o ayudas cuando sea apropiado
- Opcionalmente, incluir una solución en un archivo separado

#### Tutoriales o guías
- Usar markdown para el formato
- Incluir ejemplos prácticos
- Ser claro y conciso
- Verificar que los enlaces funcionen

#### Recursos adicionales
- Verificar que el recurso es relevante y de calidad
- Incluir una breve descripción
- Asegurar que los enlaces estén activos

## Estructura de directorios

```
Club-robotica/
├── IA/
│   ├── README.md
│   └── ejemplos/
├── Python/
│   ├── README.md
│   ├── ejemplos/
│   └── ejercicios/
├── C++/
│   ├── README.md
│   ├── ejemplos/
│   └── ejercicios/
├── Matematicas/
│   ├── README.md
│   └── ejemplos/
└── Recursos/
    └── README.md
```

## Guías de estilo

### Python
- Seguir PEP 8
- Usar docstrings para funciones y clases
- Nombres descriptivos en español para variables
- Comentarios en español

Ejemplo:
```python
def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    
    Args:
        numeros (list): Lista de números
        
    Returns:
        float: El promedio de los números
    """
    return sum(numeros) / len(numeros)
```

### C++
- Usar camelCase o snake_case consistentemente
- Comentarios claros en español
- Incluir headers necesarios
- Usar `using namespace std;` solo en ejemplos simples

Ejemplo:
```cpp
/*
 * Calcula el promedio de un vector de números
 */
double calcularPromedio(const vector<double>& numeros) {
    double suma = 0;
    for (double num : numeros) {
        suma += num;
    }
    return suma / numeros.size();
}
```

### Markdown
- Usar títulos jerárquicos apropiadamente
- Incluir bloques de código con el lenguaje especificado
- Usar listas para enumerar items
- Incluir enlaces con texto descriptivo

## Revisión de Pull Requests

Los Pull Requests serán revisados considerando:
- Calidad del código/contenido
- Claridad y utilidad para estudiantes
- Seguimiento de las guías de estilo
- Funcionamiento correcto del código

## Código de conducta

- Sé respetuoso y constructivo
- Ayuda a crear un ambiente de aprendizaje positivo
- Acepta feedback con apertura
- Da crédito cuando uses trabajo de otros

## Preguntas

Si tienes preguntas sobre cómo contribuir, abre un issue con la etiqueta "question".

¡Esperamos tus contribuciones! 🚀
