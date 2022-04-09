from components.quizQuestions import questions
from components import vars, quizTally

print("================ Welcome to Guess your Avengers ================","\n")
print("===================== Here are the hero list ===================")
print("- Captain American, Iron Man, Black Widow, Hawkeye, Thor, Hulk -")
print("----------------------------------------------------------------\n")
input("Enter Anything To Start The Questions:")
print("\n")

print("Question 1/5")
answer1 = questions["q1"][input(questions["q1"]["question"])]
vars.quizTotal += answer1

print("\n","Question 2/5")
answer2 = questions["q2"][input(questions["q2"]["question"])]
vars.quizTotal += answer2

print("\n","Question 3/5")
answer3 = questions["q3"][input(questions["q3"]["question"])]
vars.quizTotal += answer3

print("\n","Question 4/5")
answer4 = questions["q4"][input(questions["q4"]["question"])]
vars.quizTotal += answer4

print("\n","Question 5/5")
answer5 = questions["q5"][input(questions["q5"]["question"])]
vars.quizTotal += answer5
print("----------------------------------------------------------------\n")

print("========================= Final Result =========================\n")
print("Score: " + str(vars.quizTotal) + "\n")
quizTally.total(vars.quizTotal)
