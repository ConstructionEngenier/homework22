class GenericQuestion:
    """Класс является базовым.
    Инициализирует экземпляр и определяет сложность вопроса"""
    def __init__(self):
        self.is_asked = False
        self.is_right = True
        self.question = ""
        self.author = ""
        self.difficulty = ""
        self.answers = ""
        self.theme = ""
        self.user_answer = ""
        self.question_score = ""

    def __repr__(self):
        return self.question


class Question(GenericQuestion):
    def set_question(self, question):
        self.question = question

    def set_author(self, author):
        self.author = author

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def set_answers(self, answers):
        self.answers = answers

    def set_theme(self, theme):
        self.theme = theme

    def set_is_asked(self, is_asked: False):
        self.is_asked = is_asked

    def set_question_score(self, difficulty):
        self.question_score = difficulty * 10

    def set_user_answer(self, user_answer):
        self.user_answer = user_answer

    def calculate_points(self):
        return int(self.difficulty) * 10

    @property
    def points(self):
        return self.question_score

    @property
    def correct_answer(self):
        return self.answers[0]

    def is_correct(self):
        if self.user_answer:
            return self.user_answer in str(self.answers)
        return False

    def __repr__(self):
        return f"тема: {self.theme}, сложность: {self.difficulty}/10\n{self.question}"
