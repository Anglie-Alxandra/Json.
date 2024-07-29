import json

class Modelo:
    def __init__(self):
        self.ruta_archivo = 'data.json'
        self.datos = self.cargar_datos()
        self.nombre = None
        self.apellido = None
        self.edad = None
        self.cedula = None

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre
    
    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_apellido(self):
        return self.apellido
    
    def set_edad(self, edad):
        self.edad = edad

    def get_edad(self):
        return self.edad
    
    def set_cedula(self, cedula):
        self.cedula = cedula

    def get_cedula(self):
        return self.cedula

    def cargar_datos(self):
        try:
            with open(self.ruta_archivo, 'r') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return []

    def guardar_datos(self):
        with open(self.ruta_archivo, 'w') as archivo:
            json.dump(self.datos, archivo, indent=4)

    def agregar_registro(self):
        registro = {
            "cedula": self.cedula,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad
        }
        self.datos.append(registro)
        self.guardar_datos()

    def obtener_datos(self):
        return json.dumps(self.datos, indent=4)
