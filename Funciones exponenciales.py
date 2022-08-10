
print(2**3)
# Un asterisco es multiplicación y 2 es elevar al cuadrado. Qué susto
# Vamos a hacer eso con una función
def elevar(base, pow):
    result = 1
    for index in range(pow):
        result = result * base
    return result
print(elevar(40,190))
# Este código lo que hace es agarrar una base y un exponente.
# Elige el número base y usa el exponente para determinar cuántas veces tiene que multiplicarlo por sí mismo
# Esto lo hace indexando la potencia, con lo que le muestra cuántas veces ejecutar la línea 8