import html

class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(current_question.text)
        user_answer = input(f"Q{self.question_number}: {q_text} (True or False) : ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        if self.question_number == len(self.question_list):
            print("You've completed the quiz.")
            print(f"Your final score was {self.score}/{self.question_number}")
            return False
        return True

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"You score {self.score}/{self.question_number}")
