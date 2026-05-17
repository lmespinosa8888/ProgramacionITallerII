from libro import Libro


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
