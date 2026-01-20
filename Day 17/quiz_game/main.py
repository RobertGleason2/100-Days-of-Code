from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# create a question bank. loop through the question data and create a new question object for each of the questions

question_bank = []
for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

# can access the question objects through the list
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f"you've completed the quiz. your final score is {quiz.score}/ {quiz.question_number}")