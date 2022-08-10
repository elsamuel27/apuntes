from Clases import Student
# Usamos el archivo anterior otra vez
student1 = Student("Oscar", "Contabilidad", 4, True)
student2 = Student("Tim", "Religion", 1, False)

print(student1.on_honor_roll())
print(student2.on_honor_roll())