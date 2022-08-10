# Esta vez el usuario va a tener límite de intentos
secret_word = "Linux"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
# Para esto va perfecto un while

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter the secret word: ")
        guess_count += 1

    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, you lose!")
else:
    print("You win!")
if guess != secret_word and not(out_of_guesses):
    print("You win!")
# El programa le pregunte al usuario la palabra,
# y si no coincide con su respuesta,
# le resta un intento. Al quedarse sin intentos, echa un mensaje de derrota
