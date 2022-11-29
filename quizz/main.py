from quiz_brain import QuizBrain
from question_bank import question_bank

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_jas_questions():
    quiz_brain.next_question()

print("You have completed the quiz")
print(f"Your final score was {quiz_brain.score}")
 