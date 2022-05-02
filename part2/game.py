import json
import random
from game_classes import Question


def statistics(question_list):
    stats = {
        "total_questions": 0,
        "right_questions": 0,
        "total_score": 0,
    }

    for stats_question in question_list:
        if stats_question.is_asked:
            stats['total_questions'] += 1
            if stats_question.is_right:
                stats['right_questions'] += 1
                stats['total_score'] += stats_question.question_score
    return stats


def read_questions(file_name):
    questions_list = []

    with open(file_name, "r", encoding='utf-8') as f:
        questions_dict = json.load(f)

    for key in questions_dict.keys():
        questions_list.append(Question(
            question=key,
            author=questions_dict[key]['author'],
            difficulty=questions_dict[key]['difficulty'],
            answers=questions_dict[key]['answers'],
            theme=questions_dict[key]['theme']
        )
        )

    return questions_list


questions = read_questions("questions.json")
random.shuffle(questions)

for question in questions:
    question_number = questions.index(question) + 1
    print(question.build_question(question_number))
    user_answer = input('')
    if str(user_answer):
        user_answer = user_answer.lower()
    if user_answer == 'stop':
        break

    question.user_answer = user_answer
    question.is_asked = True

    if question.is_correct():
        print(f"Ответ верный, получено {question.get_points()} баллов\n")
        question.is_right = True
    else:
        print(f"Ответ неверный. Верный ответ – {question.answers[0]}\n")
        question.is_right = False


statistic = statistics(questions)

print(f"\nВот и всё!\nОтвечено {statistic['right_questions']} вопроса из {statistic['total_questions']}\n"
      f"Итого заработано {statistic['total_score']} баллов")
