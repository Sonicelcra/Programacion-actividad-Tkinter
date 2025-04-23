import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejercicio 2.")
ventana.geometry("700x700")
ventana.configure(bg="skyblue")

ejercicio2 = tk.Label(ventana, text="Ejercicio 2.", bg="Skyblue", font=("Verdana", 40))
ejercicio2.pack()

nombre = tk.Label(ventana, text="Juan Ignacio Rodriguez", bg="Skyblue", font=("Verdana", 40))
nombre.pack()
