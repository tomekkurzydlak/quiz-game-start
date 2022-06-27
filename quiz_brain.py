class QuizBrain:

   def __init__(self, q_list):
       self.question_number = 0
       self.score = 0
       self.question_list = q_list

   def still_has_questions(self):
      if self.question_number < len(self.question_list) and input(f"Would you like to answer the {self.question_number + 1}. question? (y/n): ") == "y":
         return True

   def next_question(self):
      current_question = self.question_list[self.question_number]
      self.question_number += 1
      user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
      self.check_answer(user_answer, current_question.answer)

   def check_answer(self, answer1, answer2):
      if answer1.lower() == answer2.lower():
         self.score += 1
         print("That's right")
      else:
         print("Wrong answer")
      print(f"The correct answer is: {answer2}")
      print(f"Your current score is: {self.score}/{self.question_number}\n")

   def final_board(self):
      percentage = round((self.score/self.question_number)*100, 1)
      print(f"Quiz is finished. Your total score is {self.score}/{self.question_number} -> {percentage}%")