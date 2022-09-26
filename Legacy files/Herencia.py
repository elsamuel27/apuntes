# La herencia consiste en pasar funciones de una clase a otra
# Vamos a usar de ejemplo a un chef y un chef chino
class Chef:

    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes a salad")

    def make_special_dish(self):
        print("The chef makes a escalestris")
# Definimos 3 funciones para chef normales
# Ahora al momento de hacer al chef chino vamos a citar al chef normal para que pueda usar sus funciones
# Es tan fácil como poner el nombre de la clase que queremos heredar entre paréntesis
class ChineseChef(Chef):
    def make_fried_rice(self):
        print("The chef makes fried rice")

Chef1 = ChineseChef()
ChineseChef.make_chicken(Chef1)
