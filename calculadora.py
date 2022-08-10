
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2

print(result)
print("Ups, wrong answer. Sorry, try again")
# esto no te da el resultado a la suma. Sólo junta los 2 valores que escriba el usuario
# Se debe a que Python no cuenta los valores que da el usuario como números, si no como strings
# arréglalo con la función int

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)
print(result)
# lo malo de esta versión es que es incompatible con decimales
# eso se arregla sustituyendo int por float
print("But maybe you want the sum of decimal numbers?\nLet's try one more time!")

num1 = input("Enter a DECIMAL number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)