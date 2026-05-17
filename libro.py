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
