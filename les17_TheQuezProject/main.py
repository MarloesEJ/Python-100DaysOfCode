from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for quest in question_data:
    quest_text = quest["text"]
    quest_answer = quest["answer"]
    new_question = Question(quest_text, quest_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
