"""Módulo de la clase Biblioteca.

Este módulo define la clase `Biblioteca`, que representa una biblioteca con libros y usuarios.
"""

from libro import Libro
from usuario import Usuario

MAX_NOMBRE_LEN = 80


def validar_texto_corto(valor: str, campo: str, max_len: int) -> str:
    if not isinstance(valor, str):
        raise TypeError(f"{campo} debe ser una cadena de texto")
    if len(valor.strip()) == 0:
        raise ValueError(f"{campo} no puede estar vacío")
    if len(valor) > max_len:
        raise ValueError(f"{campo} no puede superar {max_len} caracteres")
    return valor


class Biblioteca:
    """Representa una biblioteca con libros y usuarios."""

    def __init__(self, nombre: str):
        self.nombre = validar_texto_corto(nombre, "Nombre", MAX_NOMBRE_LEN)
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro: Libro) -> None:
        self.libros.append(libro)

    def agregar_usuario(self, usuario: Usuario) -> None:
        self.usuarios.append(usuario)

    def buscar_libro(self, isbn: str):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def buscar_usuario(self, identificacion: str):
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None

    def prestar_libro(self, isbn: str, identificacion: str) -> bool:
        libro = self.buscar_libro(isbn)
        usuario = self.buscar_usuario(identificacion)
        if libro is None or usuario is None:
            return False
        return usuario.pedir_libro(libro)

    def devolver_libro(self, isbn: str, identificacion: str) -> bool:
        libro = self.buscar_libro(isbn)
        usuario = self.buscar_usuario(identificacion)
        if libro is None or usuario is None:
            return False
        return usuario.devolver_libro(libro)

    def mostrar_estado(self) -> str:
        textos = [libro.mostrar_info() for libro in self.libros]
        return "\n".join(textos)
