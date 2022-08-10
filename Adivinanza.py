# La idea es que el programa contenga una palabra secreta. El usuario interactuará con el programa para adivinarla
secret_word = "Linux"
guess = ""
# Queremos que el usuario intente una y otra vez hasta acertar la palabra. Para eso va perfecto un while

while guess != secret_word:
    guess = input("Enter the secret word: ")

print("You win!")
# El programa le pregunta al usuario la palabra,
# y mientras esta no coincida con su respuesta,
# lo seguirá repitiendo hasta que acierte
