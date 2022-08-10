import random

opt1 = input("Elige la primera opción: ")
opt2 = input("Elige la segunda opción: ")
ruleta = [opt1, opt2]
result = random.choice(ruleta)
print(result)