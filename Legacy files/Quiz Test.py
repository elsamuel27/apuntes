# Vamos a usar las clases otra vez
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "Sex?\n(a) No\n(b) Yes\n(c) Maybe\n\n",
    "Windows or Linux?\n(a) Windows\n(b) Linux\n(c) macOS\n\n"
]
# Preguntas escritas en una lista para almacenarlas

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]
# Usamos la clase y la lista creadas anteriormente para añadir las preguntas con su enunciado y respuesta correcta
# Después definimos una función
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")
# Hace una puntuación que vale cero, y por cada pregunta de la lista le pide input al usuario
# usando el enunciado de dicha pregunta. Si el input coincide con la respuesta, le suma 1 a la puntuación y pregunta la siguiente
# Cuando no quedan preguntas, escribe tus resultados
run_test(questions)
# Llamamos a la función escribiendo su nombre con la lista de preguntas y listo
