# Primero vamos a usar la a (append)
# Esto hace que "write" escriba al final del archivo lo que queramos
information = open("warframes.txt", "a")
information.write("Pibote - Octavia")
information.close()
# Si queremos que lo que se añada esté en la última fila, lo mejor es añadir ese salto
# Con el ya mencionado \n
information = open("warframes.txt", "a")
information.write("\nTanque - Baruuk")
information.close()
# Si en vez de a usamos w, lo que escribamos va a sustituir a todo el contenido del archivo
information = open("warframes.txt", "w")
information.write("\nTanque - Baruuk")
information.close()
# Se puede usar w con un nombre de archivo inexistente para crearlo
information = open("amongas.txt", "w")
information.write("El sus")
information.close()
# Se puede sustituir información de un archivo, añadirla o hacer un archivo nuevo
information = open("amongas.exe", "w")
information.write("El hackeo sospechoso")
information.close()
# Es un exe y se detecta como tal pero no hace nada