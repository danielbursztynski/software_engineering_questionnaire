import json
import random

# Questionnaire for the CS22120 - Software Engineering Exam
# @author Daniel Bursztynski
# @version 1

data = json.loads(open('CS22120 14.json').read())
completed_questions = []
correct_answers = 0


def new_question():
    i = 1
    print(question["question"], "Choose", len(question["answers"]), "correct answer(s).")

    options = []
    final_answer = ""

    for choice in question["choices"]:
        options.append(choice)

    for answer in question["answers"]:
        options.append(answer)
        final_answer = answer

    random.shuffle(options)

    for option in options:
        print(str(i) + ".", option)

        if final_answer == option:
            final_answer = i

        i = i + 1

    user_answer = input("Answer: ")

    if not user_answer == str(final_answer):
        for answer in question["answers"]:
            print("\nCorrect Answer:", answer)
        print("For more details please look at", question["directions"])
        return 0
    else:
        print("For more details please look at", question["directions"])
        print("\nCorrect!")
        return 1


while True:
    question = random.choice(data["questions"])
    if len(completed_questions) == len(data["questions"]):
        print(correct_answers, " out of ", len(completed_questions))
        print("would you like to try again? 1 = yes, everything else = no")
        user_ask = input()
        if user_ask == "1":
            correct_answers = 0
            completed_questions = []
        else:
            break
    if question not in completed_questions:
        print("")
        print("question " + (str(len(completed_questions) + 1) + "/" + str(len(data["questions"]) - len(completed_questions))))
        correct_answers += new_question()
        completed_questions.append(question)
