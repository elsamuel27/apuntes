# Creo que va a tener bastante que ver con las listas 2D
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    print(row)
# Escribe todas las filas de la lista
for row in number_grid:
    for col in row:
        print(col)
# Escribe todos los valores de la lista individualmente