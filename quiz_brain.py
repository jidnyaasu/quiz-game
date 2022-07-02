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
        answer = input(f"Q.{self.question_number}: {current_question.text}\nOptions : A) {current_question.options[0]}"
                       f" B) {current_question.options[1]} C) {current_question.options[2]}"
                       f" D) {current_question.options[3]}\nAnswer: ")
        self.check_answer(answer, current_question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
        print(f"Your current score is: {self.score}/{self.question_number}")
