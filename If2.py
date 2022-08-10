
# Vamos a usar if para comparar valores
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
# Esta función recibe 3 números y comprueba cuál de todos es el mayor.
# Primero mira si el primero es igual o mayor que los 2 restantes, luego repite el proceso con el resto

print(max_num(420, 832, 160))