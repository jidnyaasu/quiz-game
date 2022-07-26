from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizGui
from data import question_data

question_bank = []
for item in question_data:
    question_text = item["question"]
    answer = item["correct_answer"]
    question_bank.append(Question(question_text, answer))

quiz = QuizBrain(question_bank)
quiz_gui = QuizGui(quiz)
