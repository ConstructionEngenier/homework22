from functions import *

questions_json = read_json("questions.json")
questions = create_random_question(questions_json)

for index, question in enumerate(questions):
    print(f"Вопрос {index+1}, {question}")
    user_answer = input('')
    if str(user_answer):
        user_answer = user_answer.lower()
    if user_answer == 'stop':
        break

    question.set_user_answer(user_answer)
    question.is_asked = True
    answer_result(question)

statistic = statistics(questions)

print(f"\nВот и всё!\nОтвечено {statistic['right_questions']} вопроса из {statistic['total_questions']}\n"
      f"Итого заработано {statistic['total_score']} баллов")
