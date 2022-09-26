
#  Este traductor servirá para sustituir vocales por otro caracter
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "E"
            else:
                translation = translation + "e"

        else:
            translation = translation + letter
    return translation

# Comprueba si la frase tiene una vocal, ya sea mayúscula o minúscula,
# y la sustituye por e. Sí, sustituye una E por E también. No voy a cambiarlo
print(translate((input("Enter a phrase: "))))