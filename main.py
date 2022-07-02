import requests
import random
from question_model import Question
# from data import question_data
from quiz_brain import QuizBrain


response = requests.get("https://opentdb.com/api.php?amount=10&type=multiple")

question_data = response.json()["results"]
question_bank = []
for item in question_data:
    text = item["question"]
    options = [item["correct_answer"]] + item["incorrect_answers"]
    # print(options)
    random.shuffle(options)
    # print(options)
    answer = item["correct_answer"]
    # print(answer)
    question_bank.append(Question(text, answer, options))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
else:
    print("\n\nQuiz finished!")
    print(f"Your final score was {quiz.score}/{quiz.question_number}")
