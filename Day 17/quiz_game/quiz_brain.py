# TODO: asking the question
# TODO: checking if the answer was correct
# TODO: checking if we're at the end of the quiz

class QuizBrain:

    # attributes: 
    # question_number = 0
    # questions_list

    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0
        
    # method:
    # next_question()
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_input, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"Correct. Your current score is {self.score}/{self.question_number}")
        else:
            print(f"That's wrong. Your current score is {self.score}/{self.question_number}")
        print(f"The correct answer is: {correct_answer}\n")