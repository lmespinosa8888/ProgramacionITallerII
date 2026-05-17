class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
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


class Usuario:
    def __init__(self, nombre: str, identificacion: str):
        self.nombre = nombre
        self.identificacion = identificacion
        self.libros_prestados = []

    def pedir_libro(self, libro: Libro) -> bool:
        if libro.prestar():
            self.libros_prestados.append(libro)
            return True
        return False

    def devolver_libro(self, libro: Libro) -> bool:
        if libro in self.libros_prestados and libro.devolver():
            self.libros_prestados.remove(libro)
            return True
        return False

    def mostrar_resumen(self) -> str:
        titulos = [libro.titulo for libro in self.libros_prestados]
        libros = ", ".join(titulos) if titulos else "Ninguno"
        return f"Usuario: {self.nombre} | ID: {self.identificacion} | Libros prestados: {libros}"


from libro import Libro
from usuario import Usuario


class Biblioteca:
    def __init__(self, nombre: str):
        self.nombre = nombre
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
