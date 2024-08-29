from datetime import datetime, timedelta

class Persona:
    def __init__(self, nombre, tarjeta_id):
        self.nombre = nombre
        self.tarjeta_id = tarjeta_id

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.fecha_prestamo = None
        self.fecha_devolucion = None

class Biblioteca:
    def __init__(self):
        self.prestamos = {}
        self.historial = []

    def prestar_libro(self, persona, libro):
        fecha_actual = datetime.now()
        fecha_limite = fecha_actual + timedelta(days=20)  # 20 días de préstamo
        libro.fecha_prestamo = fecha_actual
        libro.fecha_devolucion = fecha_limite
        if persona.tarjeta_id not in self.prestamos:
            self.prestamos[persona.tarjeta_id] = []
        self.prestamos[persona.tarjeta_id].append(libro)
        self.historial.append((persona.nombre, libro.titulo, fecha_actual, fecha_limite))
        print(f"Libro '{libro.titulo}' prestado a {persona.nombre} hasta el {fecha_limite}.")

    def devolver_libro(self, persona, libro):
        libros_prestados = self.prestamos.get(persona.tarjeta_id, [])
        if libro in libros_prestados:
            fecha_actual = datetime.now()
            if fecha_actual > libro.fecha_devolucion:
                print(f"Devolución tardía de '{libro.titulo}'. Sanción aplicada.")
            else:
                print(f"Libro '{libro.titulo}' devuelto a tiempo.")
            libros_prestados.remove(libro)
            if not libros_prestados:
                del self.prestamos[persona.tarjeta_id]
        else:
            print(f"{persona.nombre} no tiene el libro '{libro.titulo}' prestado.")

    def mostrar_historial(self):
        print("Historial de préstamos:")
        for registro in self.historial:
            print(f"Persona: {registro[0]}, Libro: {registro[1]}, Fecha de préstamo: {registro[2]}, Fecha de devolución: {registro[3]}")

# Ejemplo:
biblioteca = Biblioteca()

persona1 = Persona("Derick Adam", "12345")
libro1 = Libro("El Principito")
libro2 = Libro("Harry Potter")

biblioteca.prestar_libro(persona1, libro1)
biblioteca.prestar_libro(persona1, libro2)
biblioteca.devolver_libro(persona1, libro1)
biblioteca.mostrar_historial()
