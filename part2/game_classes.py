class GenericQuestion:
    """Класс является базовым.
    Инициализирует экземпляр и определяет сложность вопроса"""
    def __init__(self, question, author, difficulty, answers, theme, is_asked=False, user_answer="", is_right=True):
        self.question = question
        self.author = author
        self.difficulty = difficulty
        self.answers = answers
        self.theme = theme
        self.is_asked = is_asked
        self.user_answer = user_answer
        self.question_score = difficulty * 10
        self.is_right = is_right
        pass

    def __repr__(self):
        return self.question


class Question(GenericQuestion):
    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов."""
        return self.question_score

    def is_correct(self):
        """Возвращает bool. True, если ответ пользователя совпадает
        с одним из верных ответов"""
        return self.user_answer in str(self.answers)

    def build_question(self, number):
        """Возвращает вопрос в понятном пользователю виде"""
        return f"Вопрос {number}, тема: {self.theme}, сложность: {self.difficulty}/10\n{self.question}"
