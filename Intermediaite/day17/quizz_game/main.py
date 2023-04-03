from question_model import Question
from data import question_data
from quizz_brain import QuizBrain

question_bank = []

for x in question_data:
    question = Question(x['question'], x['correct_answer'])
    question_bank.append(question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
