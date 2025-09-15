from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank=[]
for i in range (0, len(question_data)):
    question=Question(question_data[i]["question"],question_data[i]["correct_answer"])
    question_bank.append(question)

# print(question_bank[0].text)

# print(question_bank[0].answer)


#another approach

# question_bank=[]
# for question in question_data:
#     question_text=question["text"]
#     question_ans= question_data["answer"]
#     new_question= Question(question_text,question_ans)
#     question_bank.append(new_question)

quiz=QuizBrain(question_bank)


while quiz.still_has_question():
    quiz.next_question()
print("you have completed the quize")
print(f"final score {quiz.score}/{quiz.current_question}")