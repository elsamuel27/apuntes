# Los tipos de datos en Python se limitan a strings y números que podemos organizar en listas y diccionarios
# No son suficientes para cubrir todos los tipos de datos.
# Eso es exactamente lo que podemos hacer con las clases, crear tipos nuevos
# Vamos a definir una clase aquí, mejor que en otro archivo
class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


# "self" se está refiriendo al objeto
# El código dice que [nombre del objeto].name va a mostrar su nombre, y así con todo lo demás
# También tenemos dentro de la clase una función que indica si un estudiante está aprobado usando su GPA

student1 = Student("Jim", "Programación", 3.1, False)
student2 = Student("Jesús", "Religión", 17, True)
# Le damos a una variable los valores que tiene que tener un estudiante, determinados en el archivo anterior
print(student1.gpa)
# Ahora podemos usar print con el valor en concreto de uno de los estudiantes
print(student2.major)
# El hecho de haber hecho una clase para estudiantes significa que podemos crear tantos estudiantes como queramos
# bajo dicha clase, guardando sus valores en diferentes variables