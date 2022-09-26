
# Aquí vamos a usar valores de True o False, y dependiendo de su valor el programa hará una cosa u otra
is_male = True
is_tall = False
if is_male:
     print("You are a male")
else:
    print("You aren't a male")
# El código dice literalmente, si es hombre, escribir "Eres hombre". Si no, escribir "No eres hombre"
# Vamos a complicarlo un poco con 2 valores y más condicionales
if is_male and is_tall:
    print("omg sexy baka")
if is_male or is_tall:
    print("maboy")
# Con "and" tienen que ser verdaderos los 2 valores, con "or" vale si es uno
if is_male and not(is_tall):
    print("energuia moment")
# También se puede añadir un not para comprobar si un valor es falso
# Y se puede usar elif para hacer la misma comprobación pero con valores invertidos