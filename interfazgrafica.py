import tkinter as tk
from tkinter import ttk
import math

def calcular_promedio_y_desviacion():
    numeros = []
    
    # Recoger los números ingresados por el usuario
    for entrada in entradas:
        try:
            numero = float(entrada.get())
            numeros.append(numero)
            etiqueta_error.config(text="")
        except ValueError:
            etiqueta_error.config(text="Introduce un número válido")
            return
    
    # Verificar si hay números para calcular
    if len(numeros) == 0:
        etiqueta_error.config(text="Introduce al menos un número")
        return

    # Calcular promedio
    promedio = sum(numeros) / len(numeros)
    
    # Calcular desviación estándar
    varianza = sum((x - promedio) ** 2 for x in numeros) / len(numeros)
    desviacion_estandar = math.sqrt(varianza)
    
    # Mostrar resultados
    etiqueta_promedio.config(text=f"Promedio: {promedio:.2f}")
    etiqueta_desviacion.config(text=f"Desviación estándar: {desviacion_estandar:.2f}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Promedio y Desviación Estándar")
ventana.config(width=500, height=300)

# Etiquetas para instrucciones
etiqueta_instrucciones = ttk.Label(text="Introduce hasta 5 números:")
etiqueta_instrucciones.place(x=10, y=10)

# Entradas para los números
entradas = []
for i in range(5):
    entrada = ttk.Entry()
    entrada.place(x=150, y=40 + i*30, width=80)
    entradas.append(entrada)

# Etiqueta de error
etiqueta_error = ttk.Label(text="", foreground="red")
etiqueta_error.place(x=300, y=10)

# Botón para calcular el promedio y la desviación estándar
boton_calcular = ttk.Button(text="Calcular", command=calcular_promedio_y_desviacion)
boton_calcular.place(x=150, y=200)

# Etiquetas para mostrar los resultados
etiqueta_promedio = ttk.Label(text="Promedio: ")
etiqueta_promedio.place(x=10, y=230)

etiqueta_desviacion = ttk.Label(text="Desviación estándar: ")
etiqueta_desviacion.place(x=10, y=250)

# Ejecutar la ventana principal
ventana.mainloop()