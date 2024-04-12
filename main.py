from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []


for i in question_data:
    question = i['text']
    answer = i['answer']
    new_question = Question(text=question, answer=answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Quiz completed")
print(f"You're final score is {quiz.score}/{quiz.question_number}\n")