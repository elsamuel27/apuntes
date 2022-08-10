
lucky_numbers = [2, 4, 5, 9, 27]
friends = ["Francisco", "Gabriel", "Cristina", "Hamood", "Amongas"]
friends.extend(lucky_numbers)
# Esto junta el contenido de una lista a otra, y se ve reflejado en el print
friends.append("Sus")
# Añade un objeto a la lista, al final
friends.insert(1, "Baka")
# Añade un objeto pero eligiendo su ubicación
friends.remove("Sus")
# Elimina un objeto de la lista
# Si intentas eliminar algo que no está en la lista va a saltar un error
# Que se puede sortear con if else
friends.pop()
# Elimina el último objeto de la lista
print(friends)

print(friends.index("Hamood"))
# Escribe la ubicación en la lista del valor que elijas
# Hacer esto con un valor que no está en la lista te salta un error
print(friends.count("Francisco"))
# Cuenta cuántas veces sale un valor en la lista
lucky_numbers.sort()
# Ordena de menor a mayor los números de una lista. Si los valores son strings da error
friends.reverse()
print(friends)
# Invierte el orden de los valores. Da igual que tenga strings o números
friends2 = friends.copy()
print(friends2)
# Hace una copia de lista

# También podemos verificar si un elemento está en una lista de la siguiente forma
# Los casos serán True y False, respectivamente
"Francisco" in friends
"Motomami" in friends
vocales = ["a", "e", "i", "o", "u"]
"a" in vocales
# Por alguna razón estos últimos comandos los pilla el interpretador solamente

friends[9] = "Un gordo"
# Cambia un valor de la lista
print(friends)