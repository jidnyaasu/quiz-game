from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    text = item["text"]
    answer = item["answer"]
    question_bank.append(Question(text, answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
else:
    print("\n\nQuiz finished!")
    print(f"Your final score was {quiz.score}/{quiz.question_number}")
