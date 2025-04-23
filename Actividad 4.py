import tkinter as tk

def LimpiarVentana():
    for widget in ventana.winfo_children():
          widget.destroy()

def opcion1():
    LimpiarVentana()
    accion = tk.Label(ventana, text="Eligio la opcion 1.", font=("arial", 20))
    accion.pack()
    boton = tk.Button(ventana, text="Volver al menu principal.", font=("arial", 10), command=menuprincipal)
    boton.pack()

def opcion2():
    LimpiarVentana()
    accion2 = tk.Label(ventana, text="Eligio la opcion 2.", font=("arial", 20))
    accion2.pack()
    boton = tk.Button(ventana, text="Volver al menu principal.", font=("arial", 10), command=menuprincipal)
    boton.pack()

def opcion3():
    LimpiarVentana()
    accion3 = tk.Label(ventana, text="Eligio la opcion 3.", font=("arial", 20))
    accion3.pack()
    boton = tk.Button(ventana, text="Volver al menu principal.", font=("arial", 10), command=menuprincipal)
    boton.pack()

def opcion4():
    LimpiarVentana()
    accion4 = tk.Label(ventana, text="Eligio la opcion 4.", font=("arial", 20))
    accion4.pack()
    boton = tk.Button(ventana, text="Volver al menu principal.", font=("arial", 10), command=menuprincipal)
    boton.pack()

def menuprincipal():
    LimpiarVentana()
    titulo = tk.Label(ventana, text="Menu Principal", font=("arial", 20))
    titulo.pack()
    boton1 = tk.Button(ventana, text="Opcion 1", command=opcion1)
    boton1.pack()
    boton2 = tk.Button(ventana, text="Opcion 2", command=opcion2)
    boton2.pack()
    boton3 = tk.Button(ventana, text="Opcion 3", command=opcion3)
    boton3.pack()
    boton4 = tk.Button(ventana, text="Opcion 4", command=opcion4)
    boton4.pack()

def main():
    global ventana
    ventana = tk.Tk()
    ventana.geometry("450x250")
    ventana.title("Actividad 4.")
    menuprincipal()
    

if __name__ == "__main__":
    main()
