class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __getText__(self):
        return self.text

    def __getAnswer__(self):
        return self.answer

    def __str__(self):
        return f"{self.text} - {self.answer}"
