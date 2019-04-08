from questions import Question

question_prompt = [
        "What is the BGP TCP Number?\n(a) 72\n(b) 179\n(c) 22",
        "What large the VLAN Space is?\n(a) 4096\n(b) 512\n(c) 212",
        "How to display running config on cisco?\n(a) show run\n(b) show config\n(c) show configuration | display set",
]


questions = [
    Question(question_prompt[0], "b"),
    Question(question_prompt[1], "a"),
    Question(question_prompt[2], "a"),
]


def run_test(questions_function):
    score = 0
    for question in questions_function:
        answer = input(question_prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "Correct")

run_test(questions_function)



