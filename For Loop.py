# Vamos a probar este comando con una lista anterior
friends = ["Francisco", "Gabriel", "Cristina", "Hamood", "Amongas"]
for friend in friends:
    print(friend)
# Esto lo que hace es definir los objetos de las listas
# En este caso un objeto de la lista "friends" se llamaría "friend"
# Escribe todas las letras del string, en caso de lista escribe todos los valores
for index in range(3, 10):
    print(index)
# Imprime todos los números del 3 al 10 sin contar el 10.
# El segundo número del range no se va a mostrar
for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("first Iteration")
    else:
        print("Not first")
# Escribe index 5 veces, si es 0 pone una cosa y si no otra