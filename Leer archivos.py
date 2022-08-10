# Vamos a aprender cómo hacer para que un archivo de Python pueda leer archivos de fuera
# En el comando open hay que poner el nombre con su ruta completa, a menos que esté en la misma carpeta
open("warframes.txt", "r")
# Una r significa read, para leer el archivo sin modificarlo
# Con una w (write) podríamos escribir en él
# a (append) es como write pero sólo para añadir información, no podría modificar o borrar
# Por último, r+ es para leer y escribir
# La idea es guardar el contenido del archivo en una variable, haciéndola igual a abrirlo
information = open("warframes.txt", "r")
# Además de abrir un archivo, también hay que cerrarlo
information.close()
# Pero vamos a abrirlo otra vez porque no hemos hecho nada
information = open("warframes.txt", "r")
# Antes de intentar ver o escribir nada, es recomendable comprobar si se puede leer el archivo
print(information.readable())
# Al haber usado el modo r, sí se puede leer, así que mostrará "True"
print(information.read())
# También puedes leer sólo 1 línea
print(information.readline())
# Leer por líneas pero unas cuántas
print(information.readline())
print(information.readline())
# O hacer una lista con todas las líneas
information = open("warframes.txt", "r")
print(information.readlines())
# Que nos puede servir para escribir sólo 1 línea
# Importante abrir el archivo cada vez que se quiera manipular
information = open("warframes.txt", "r")
print(information.readlines()[2])