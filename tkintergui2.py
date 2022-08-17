import tkinter
ventana = tkinter.Tk()
ventana.geometry("480x480")
# Cómo posicionar los widgets bien usando el método GRID
boton1 = tkinter.Button(ventana, text="boton1")
boton2 = tkinter.Button(ventana, text="boton2")
boton3 = tkinter.Button(ventana, text="boton3")
texto = tkinter.Entry(ventana)

boton1.grid(row=1, column=0)
boton2.grid(row=1, column=1)
boton3.grid(row=1, column=2)
texto.grid(row=3, column=1)

ventana.mainloop()
