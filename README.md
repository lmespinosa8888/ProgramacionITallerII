# Proyecto Python - Sistema de Biblioteca Escolar

Este proyecto es un ejemplo simple de gestión de una biblioteca escolar.
Incluye clases para libros, usuarios y la biblioteca, y muestra cómo
prestar y devolver libros.

## Contenido de los archivos

- `libro.py`
  - Define la clase `Libro`.
  - Controla los atributos `titulo`, `autor`, `isbn` y `disponible`.
  - Incluye métodos para `prestar`, `devolver` y `mostrar_info`.

- `usuario.py`
  - Define la clase `Usuario`.
  - Controla los atributos `nombre`, `identificacion` y `libros_prestados`.
  - Incluye métodos para `pedir_libro`, `devolver_libro` y `mostrar_resumen`.

- `biblioteca.py`
  - Define la clase `Biblioteca`.
  - Administra colecciones de `libros` y `usuarios`.
  - Incluye funciones para agregar libros y usuarios, buscar por ISBN o ID,
    prestar libros y devolver libros.

- `main.py`
  - Script de ejecución principal.
  - Crea una biblioteca, libros y usuarios de ejemplo.
  - Realiza operaciones de préstamo y devolución.
  - Imprime el estado inicial, el estado tras los préstamos y el estado final.

## Funcionamiento de la aplicación

1. Se crea una biblioteca llamada "Biblioteca Escolar".
2. Se agregan tres libros de ejemplo.
3. Se crean dos usuarios.
4. Se presta un libro a cada usuario.
5. Se muestra el estado de los usuarios y la biblioteca.
6. Se devuelve un libro y se muestra el estado final.

## Cómo ejecutar

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta:

```bash
python main.py
```

## Resultados esperados

- Lista de libros con sus estados de disponibilidad.
- Información sobre qué libros tiene cada usuario.
- Cambios en el estado de los libros después de préstamos y devoluciones.
