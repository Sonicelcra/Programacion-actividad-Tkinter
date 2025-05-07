import tkinter as tk
from urllib.request import urlopen
from PIL import Image, ImageTk
from io import BytesIO

def descargarFondo():
    urlImagen = "https://github.com/Sonicelcra/Imagenes/blob/main/Bosque%20Bonito.png?raw=true"
    datosImagen = urlopen(urlImagen)
    imagenBinaria = datosImagen.read()
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen

def menuPrincipal():
    
    imagen=descargarFondo()
    
    imagenRedimensionada = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)
    
    imagenTK = ImageTk.PhotoImage(imagenRedimensionada)

    button1 = tk.Button(vt, text="Graficar.", font=("Arial", 20), command=graficar)
    button1.pack(side=tk.TOP)

    etiqueta = tk.Label(vt, image=imagenTK)
    etiqueta.pack()
    
    vt.mainloop()

def graficar():
    for widget in vt.winfo_children():
        widget.destroy()
    texto = tk.Label(vt, text="Has sido graficado.", font=("Comic Sans", 50))
    texto.place(x="450", y="350")
    vt.mainloop()

def main():
    global vt 
    vt = tk.Tk()
    vt.title("Graficacion")
    
    global ancho 
    ancho = vt.winfo_screenwidth()
    global alto
    alto = vt.winfo_screenheight()
    vt.geometry(f"{ancho}x{alto}")
    menuPrincipal()
    
if __name__ == "__main__":
    main()
