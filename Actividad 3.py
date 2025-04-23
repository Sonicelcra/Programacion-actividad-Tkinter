import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejercicio 3.")
ventana.geometry("700x700")
ventana.configure(bg="skyblue")

name_var = tk.StringVar()

pregunta = tk.Entry(ventana, textvariable = name_var, relief=("groove"), font=("Arial", 20))
pregunta.pack()

def nombre():
    nomvar = pregunta.get()
    nombre = tk.Label(ventana,text=("Hola, ", nomvar, ", te saluda Juani!"), font=("arial", 20), bg=("Skyblue"))
    nombre.pack()

saludar = tk.Button(ventana, text="Saludar", command=nombre, font=("arial",20))
saludar.pack()
