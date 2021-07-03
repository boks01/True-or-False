class Checking:
    def __init__(self, question, answer):
        self.answer = answer
        self.question = question
        self.question_number = 0
        self.score = 0

    def give_question(self):
        for _ in range(len(self.question)):
            current_question = self.question[self.question_number]
            answer = self.answer[self.question_number]
            self.question_number += 1
            asking = input(f"{self.question_number}.{current_question} : True or False?\n")
            self.check_answer(answer, asking)
        print(f"\nYou reach the end of this quiz\nscore: {self.score}/{self.question_number}")
    def check_answer(self, answer, user_answer):
        if answer.lower() == user_answer.lower():
            print("You right!!!")
            self.score += 1
            print(f"{self.score}/{self.question_number}")
        else:
            print("You wrong")
            print(f"{self.score}/{self.question_number}")
