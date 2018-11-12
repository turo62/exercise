from Question import Question

question_prompts = [
    "Milyen színű az alma? \n(a) piros/zöld \n(b) lila \n(c) narancs\n\n",
    "Milyen színű a banán? \n(a) kék \n(b) zöld \n(c) sárga\n\n",
    "Milyen színű az eper? \n(a) barna \n(b) piros \n(c) bordó\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Kaptál " + str(score) + " pontot a " + str(len(questions)) + "-ból! Szuper!")

run_test(questions)
    
