class Persona:
    contador = 0

def __init__(self, nombre, correo):
        self.nombre = nombre
        self._correo = correo  
        Persona.contador += 1

def __str__(self):
    return f"{self.nombre} ({self._correo})"

class Estudiante(Persona):
        def __init__(self, nombre, correo, carnet):
            super().__init__(nombre, correo)
            self.carnet = carnet


class Docente(Persona):
    def __init__(self, nombre, correo, lector_biometrico):
        super().__init__(nombre, correo)
        self.lector_biometico = lector_biometrico