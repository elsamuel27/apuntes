import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x300")


def ayuda():
    print("Funciona jiji")


etiqueta = tkinter.Label(ventana, text="Hola Mundo")
# para colocar widgets
etiqueta.pack(side=tkinter.BOTTOM)
# Side para ponerlo a un lado, fill para que cubra una coordenada entera

# Toca hacer botones
button1 = tkinter.Button(ventana, text="Amongas", command=ayuda)
button1.pack(side=tkinter.TOP)
# Después de command puedes usar lambda para ejecutar una función con parámetros
# O puedes escribir directamente el comando que sea, si no es muy complicado


def usartexto():
    ye = cajaTexto.get()
    print(ye)
# Esta función sirve para guardar el texto de una caja en una variable
# Para una aplicación fullGUI no hace falta el print


button2 = tkinter.Button(ventana, text="Amongas2", command=usartexto)
button2.pack(side=tkinter.LEFT)
cajaTexto = tkinter.Entry(ventana)
cajaTexto.pack(side=tkinter.RIGHT)

ventana.mainloop()
