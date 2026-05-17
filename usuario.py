from libro import Libro

MAX_NOMBRE_LEN = 50
MAX_IDENTIFICACION_LEN = 20


def validar_texto_corto(valor: str, campo: str, max_len: int) -> str:
    if not isinstance(valor, str):
        raise TypeError(f"{campo} debe ser una cadena de texto")
    if len(valor.strip()) == 0:
        raise ValueError(f"{campo} no puede estar vacío")
    if len(valor) > max_len:
        raise ValueError(f"{campo} no puede superar {max_len} caracteres")
    return valor


class Usuario:
    def __init__(self, nombre: str, identificacion: str):
        self.nombre = validar_texto_corto(nombre, "Nombre", MAX_NOMBRE_LEN)
        self.identificacion = validar_texto_corto(identificacion, "Identificación", MAX_IDENTIFICACION_LEN)
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
