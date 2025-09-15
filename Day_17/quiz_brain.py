from question_model import Question

class QuizBrain:
    def __init__(self,question_list):
        self.question_list=question_list
        self.question_num=0
        self.score=0


    def still_has_question(self):
        return self.question_num < len(self.question_list)
        # while self.question_num <=len(self.question_list):
        #     return True
        


    def next_question(self):
        self.current_question=self.question_list[self.question_num]
        self.question_num +=1
        user_ans=input(f"Q.{self.question_num} : {self.current_question.text} (True/False)? :" )
        self.check_answer(user_ans,self.current_question.answer)


    def check_answer(self,user_ans,correct_ans):
        if user_ans.lower()==correct_ans.lower():
            print("you have got it right")
            self.score+=1
        else:
            print("you have got it wrong")
        print(f"The corrct answer {self.current_question.answer}")
        print(f"Your current score{self.score}/{self.question_num}")
        print("\n")




