from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    #question_bank = Question( item, question_data[item] )
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

answer_ratio = f"{quiz.score}/{quiz.question_number}"
print("You have completed the quiz.")
print(f"Your final score is: {answer_ratio}")