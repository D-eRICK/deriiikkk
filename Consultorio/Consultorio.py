class Paciente:
    def __init__(self, nombre, motivo_consulta):
        self.nombre = nombre
        self.motivo_consulta = motivo_consulta
        self.tiene_cita = False

class Consultorio:
    def __init__(self):
        self.pacientes = []
        self.sala_espera = []
        self.doctores = ['Dr. Lopez', 'Dra. Portillo', 'Dr. Flores']
        self.doctor_index = 0  # Para asignar doctores de manera cíclica

    def registrar_paciente(self, paciente):
        if paciente.tiene_cita:
            self.sala_espera.append(paciente)
            print(f"{paciente.nombre} ya tiene una cita previa. Pasado a la sala de espera.")
        else:
            paciente.tiene_cita = True
            self.pacientes.append(paciente)
            doctor_asignado = self.doctores[self.doctor_index]
            self.doctor_index = (self.doctor_index + 1) % len(self.doctores)
            print(f"Cita asignada para {paciente.nombre} con {doctor_asignado}.")

    def mostrar_sala_espera(self):
        print("Pacientes en sala de espera:")
        for paciente in self.sala_espera:
            print(f"- {paciente.nombre}, Motivo: {paciente.motivo_consulta}")

# Ejemplo:
consultorio = Consultorio()

paciente1 = Paciente("Jose Reyes", "Dolor de estomago")
paciente2 = Paciente("Dulce Herrera", "Calentura")

consultorio.registrar_paciente(paciente1)
consultorio.registrar_paciente(paciente1)  # Segunda vez que llega, va a sala de espera
consultorio.registrar_paciente(paciente2)

consultorio.mostrar_sala_espera()
