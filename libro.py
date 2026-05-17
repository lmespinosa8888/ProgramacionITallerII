"""Módulo de la clase Libro.

Define los atributos y comportamientos de un libro en la biblioteca.
"""

MAX_TITULO_LEN = 100
MAX_AUTOR_LEN = 60
MAX_ISBN_LEN = 20


def validar_texto_corto(valor: str, campo: str, max_len: int) -> str:
    if not isinstance(valor, str):
        raise TypeError(f"{campo} debe ser una cadena de texto")
    if len(valor.strip()) == 0:
        raise ValueError(f"{campo} no puede estar vacío")
    if len(valor) > max_len:
        raise ValueError(f"{campo} no puede superar {max_len} caracteres")
    return valor


class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str):
        self.titulo = validar_texto_corto(titulo, "Título", MAX_TITULO_LEN)
        self.autor = validar_texto_corto(autor, "Autor", MAX_AUTOR_LEN)
        self.isbn = validar_texto_corto(isbn, "ISBN", MAX_ISBN_LEN)
        self.disponible = True

    def prestar(self) -> bool:
        if not self.disponible:
            return False
        self.disponible = False
        return True

    def devolver(self) -> bool:
        if self.disponible:
            return False
        self.disponible = True
        return True

    def mostrar_info(self) -> str:
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Libro: {self.titulo} | Autor: {self.autor} | ISBN: {self.isbn} | Estado: {estado}"
