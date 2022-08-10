# Jan -> January
# Mar -> March
# La idea de este programa es que pueda hacer lo de arriba. Eso se hace con un diccionario
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}
print(monthConversions)
print(monthConversions["Feb"])
# Se puede mostrar en pantalla con un print, o se puede mostrar una conversión en concreto
# Muy parecido a las listas (Un poco más a los tuples)
print(monthConversions.get("Jan"))
# La diferencia entre los corchetes y el get es que si citas una conversión que no tiene resultado
# te va a poner un "None", pero con los corchetes va a darte error
# O te puede dar un valor que elijas tú
print(monthConversions.get("Om", "Incorrect"))
# Un diccionario también puede funcionar con números
monthNumbers = {
    0: "January",
    1: "February",
    2: "March",
}
print(monthNumbers)
print(monthNumbers.get(1))
print(monthNumbers.get(5))
# Aplica igual en ambos casos