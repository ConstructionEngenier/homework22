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


def read_json(file_name):
    with open(file_name, "r", encoding='utf-8') as f:
        questions_dict = json.load(f)
    return questions_dict


def create_random_question(questions_dict):
    questions_list = []
    for key in questions_dict.keys():
        question = Question()
        question.set_question(key)
        question.set_author(questions_dict[key]['author'])
        question.set_difficulty(questions_dict[key]['difficulty'])
        question.set_answers(questions_dict[key]['answers'])
        question.set_theme(questions_dict[key]['theme'])
        question.set_question_score(questions_dict[key]['difficulty'])
        questions_list.append(question)
    random.shuffle(questions_list)
    return questions_list


def answer_result(question):
    if question.is_correct():
        question.is_right = True
        return print(f"Ответ верный, получено {question.points} баллов\n")
    question.is_right = False
    return print(f"Ответ неверный. Верный ответ – {question.correct_answer}\n")
