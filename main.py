from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario


def main() -> None:
    biblioteca = Biblioteca("Biblioteca Escolar")

    libro1 = Libro("Matemáticas 101", "Ana Pérez", "978-0001")
    libro2 = Libro("Historia Universal", "Carlos Ruiz", "978-0002")
    libro3 = Libro("Programación en Python", "María Gómez", "978-0003")

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    usuario1 = Usuario("Lucas", "U001")
    usuario2 = Usuario("Sofía", "U002")

    biblioteca.agregar_usuario(usuario1)
    biblioteca.agregar_usuario(usuario2)

    print("== Estado inicial de la biblioteca ==")
    print(biblioteca.mostrar_estado())
    print()

    print("== Préstamos ==")
    biblioteca.prestar_libro("978-0001", "U001")
    biblioteca.prestar_libro("978-0003", "U002")
    print(usuario1.mostrar_resumen())
    print(usuario2.mostrar_resumen())
    print()

    print("== Estado tras préstamos ==")
    print(biblioteca.mostrar_estado())
    print()

    print("== Devoluciones ==")
    biblioteca.devolver_libro("978-0001", "U001")
    print(usuario1.mostrar_resumen())
    print()

    print("== Estado final de la biblioteca ==")
    print(biblioteca.mostrar_estado())


if __name__ == "__main__":
    main()
