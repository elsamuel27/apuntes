
# La calculadora de antes sólo puede sumar y además se equivoca 2 veces o te tira errores
# Desarrollarla ha sido muy bueno para aprender, y mirar el código para repasar, pero toca sustituirla
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))
# Esta vez el usuario, además de 2 números enteros o decimales, va a elegir la operación

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")
# Si el operador es + suma, - resta, / divide y * multiplica. Si es otro, tira error