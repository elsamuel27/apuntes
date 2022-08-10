# Esta lección va sobre cómo afrontar los errores a los que te enfrentes programando
number = int(input("Enter a number: "))
print(number)
# Este programa le pide al usuario un número entero y lo muestra, pero si introduce otro valor salta error
# Se debe a que el input del usuario se convierte en un número entero, no lo deja como string
# Podemos hacer que el programa haga otra cosa y continúe con un "Try/Except"
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid number")
# El programa literalmente dice: Intenta (líneas de código anteriores), si no funciona, escribe "Invalid number"
# Esto sirve para proteger al programa de casos así, que el usuario introduzca algo que no va ahí
# Es capaz de manejar errores más grandes, como un valor que se divida entre 0
try:
    broken_value = 10 / 0
except:
    print("Hey, there is a broken value in the program")

# También puedes hacer un except que actúe ante un error en concreto
# Viene bien para tener una respuesta para cada error al que tu programa pueda enfrentarse
# A más complejo el programa, más errores posibles. Este código es VITAL
try:
    omagad = 69420 / 0
except ZeroDivisionError:
    print("plz help")
# Un "try" puede acabar en varios except si especificas el error
try:
    number = int(input("Enter a division: "))
    print(number)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("But the division cannot use 0!")
# Nota, un print(err) va a escribir el error