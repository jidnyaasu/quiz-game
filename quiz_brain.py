import html


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {html.unescape(current_question.text)}\nOptions :"
                       f" A) {current_question.options['A']}"
                       f" B) {current_question.options['B']} C) {current_question.options['C']}"
                       f" D) {current_question.options['D']}\nAnswer: ").upper()
        self.check_answer(current_question.options[answer], current_question.answer)

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
            print(f"Correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
