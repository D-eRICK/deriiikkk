class Animal:
    def __init__(self, nombre, especie, area):
        self.nombre = nombre
        self.especie = especie
        self.area = area
        self.tratamientos = []  

    def agregar_tratamiento(self, medicamento, dosis, frecuencia):
        tratamiento = {
            'medicamento': medicamento,
            'dosis': dosis,
            'frecuencia': frecuencia
        }
        self.tratamientos.append(tratamiento)
        print(f"Tratamiento agregado a {self.nombre}: {medicamento}, Dosis: {dosis}, Frecuencia: {frecuencia}")

    def mostrar_tratamientos(self):
        if not self.tratamientos:
            print(f"{self.nombre} no tiene tratamientos registrados.")
            return
        
        print(f"\nTratamientos para {self.nombre}:")
        for tratamiento in self.tratamientos:
            print(f"Medicamento: {tratamiento['medicamento']}, Dosis: {tratamiento['dosis']}, Frecuencia: {tratamiento['frecuencia']}")
        print()


class Zoologico:
    def __init__(self):
        self.animales = []  

    def agregar_animal(self, nombre, especie, area):
        animal = Animal(nombre, especie, area)
        self.animales.append(animal)
        print(f"Animal agregado: {nombre}, Especie: {especie}, Área: {area}")

    def listar_animales(self):
        if not self.animales:
            print("No hay animales en el zoológico.")
            return
        
        print("\nLista de animales en el zoológico:")
        for animal in self.animales:
            print(f"Nombre: {animal.nombre}, Especie: {animal.especie}, Área: {animal.area}")
        print()

    def listar_tratamientos(self):
        print("\nAnimales en tratamiento:")
        for animal in self.animales:
            if animal.tratamientos:
                animal.mostrar_tratamientos()
        print()


zoologico = Zoologico()


zoologico.agregar_animal("Simba", "León", "Sabana")
zoologico.agregar_animal("Manyula", "Elefante", "Selva Tropical")


zoologico.listar_animales()


simba = zoologico.animales[0]  
simba.agregar_tratamiento("Antibiótico", "500mg", "Cada 8 horas")

manyula = zoologico.animales[1]  
manyula.agregar_tratamiento("Vitamina B12", "2ml", "Cada 24 horas")


zoologico.listar_tratamientos()
