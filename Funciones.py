
# Una función es un bloque de código que hace algo que el programa va a usar varias veces
# Se usa para, en lugar de escribir el mismo código varias veces, llamar a dicha función y listo
def sayhi():
    print("Hello User")
# Ahora el código tiene una función llamada "sayhi" que va a ejecutar un print
# Puedes llamar a esa función escribiendo su nombre solamente
print("Top")
sayhi()
print("Botton")
# Y se pueden usar los paréntesis de una función para incluirle un parámetro
def say_hi(name):
    print("Hello " + name)
# He creado otra función que esta vez pide un nombre, el cual va a usar en su print
say_hi("Samuel")
# Una función puede tener todos los parámetros que quieras
def saludar(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old" )
saludar("Samuel", 17)
# Estas funciones son muy básicas, sólo tienen 1 línea de código
# Fuera de las prácticas vas a usarlas para bloques más grandes