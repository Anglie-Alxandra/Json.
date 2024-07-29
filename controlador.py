from modelo import Modelo
from vista import Vista
import tkinter as tk

class Controlador:
    def __init__(self, root):
        self.modelo = Modelo()
        self.vista = Vista(root)
        self.vista.boton_agregar.config(command=self.agregar_registro)
        self.vista.boton_mostrar.config(command=self.mostrar_datos)

    def agregar_registro(self):
        cedula = self.vista.entry_cedula.get()
        nombre = self.vista.entry_nombre.get()
        apellido = self.vista.entry_apellido.get()
        edad = self.vista.entry_edad.get()

        if not cedula or not nombre or not apellido or not edad:
            self.vista.mostrar_mensaje("Error", "Todos los campos son obligatorios")
            return

        try:
            edad = int(edad)
        except ValueError:
            self.vista.mostrar_mensaje("Error", "La edad debe ser un número")
            return

        self.modelo.set_cedula(cedula)
        self.modelo.set_nombre(nombre)
        self.modelo.set_apellido(apellido)
        self.modelo.set_edad(edad)

        self.modelo.agregar_registro()
        self.vista.mostrar_mensaje("Éxito", "Registro agregado correctamente")
        self.limpiar_campos()

    def mostrar_datos(self):
        datos = self.modelo.obtener_datos()
        self.vista.mostrar_mensaje("Datos", datos)

    def limpiar_campos(self):
        self.vista.entry_cedula.delete(0, tk.END)
        self.vista.entry_nombre.delete(0, tk.END)
        self.vista.entry_apellido.delete(0, tk.END)
        self.vista.entry_edad.delete(0, tk.END)
