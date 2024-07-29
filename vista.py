import tkinter as tk
from tkinter import messagebox

class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro")
        self.root.geometry("300x300")
        self.root.configure(bg="#aac2e6")
        
        self.crear_widgets()

    def crear_widgets(self):
        self.label_cedula = tk.Label(self.root, text="Cédula", bg="#aac2e6")
        self.label_cedula.grid(row=0, column=0, padx=10, pady=10)
        self.entry_cedula = tk.Entry(self.root)
        self.entry_cedula.grid(row=0, column=1, padx=10, pady=10)

        self.label_nombre = tk.Label(self.root, text="Nombre", bg="#aac2e6")
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10)
        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)

        self.label_apellido = tk.Label(self.root, text="Apellido", bg="#aac2e6")
        self.label_apellido.grid(row=2, column=0, padx=10, pady=10)
        self.entry_apellido = tk.Entry(self.root)
        self.entry_apellido.grid(row=2, column=1, padx=10, pady=10)

        self.label_edad = tk.Label(self.root, text="Edad", bg="#aac2e6")
        self.label_edad.grid(row=3, column=0, padx=10, pady=10)
        self.entry_edad = tk.Entry(self.root)
        self.entry_edad.grid(row=3, column=1, padx=10, pady=10)

        self.boton_agregar = tk.Button(self.root, text="Agregar", command=self.agregar_registro, bg="#1a3c70", fg="#FFFFFF")
        self.boton_agregar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.boton_mostrar = tk.Button(self.root, text="Mostrar Datos", command=self.mostrar_datos, bg="#1a3c70", fg="#FFFFFF")
        self.boton_mostrar.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def agregar_registro(self):
        pass

    def mostrar_datos(self):
        pass

    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)
