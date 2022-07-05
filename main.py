import requests
import random
from time import sleep
from question_model import Question
from quiz_brain import QuizBrain


response = requests.get("https://opentdb.com/api.php?amount=10&type=multiple", timeout=5)

question_data = response.json()["results"]
question_bank = []
for item in question_data:
    text = item["question"]
    options_keys = ["A", "B", "C", "D"]
    options_values = [item["correct_answer"]] + item["incorrect_answers"]
    random.shuffle(options_values)
    options = dict(zip(options_keys, options_values))
    answer = item["correct_answer"]
    question_bank.append(Question(text, answer, options))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
else:
    print("\n\nQuiz finished!")
    print(f"Your final score was {quiz.score}/{quiz.question_number}")
    sleep(5)
