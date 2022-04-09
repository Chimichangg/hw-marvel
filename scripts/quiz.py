from components.quizQuestions import questions
from components import vars, quizTally
import colorama
from colorama import Fore, Back, Style
from emoji import emojize

colorama.init(autoreset=True)

print(Back.GREEN + "================= Welcome to Guess your Avengers ==================","\n")
print("------------------" + emojize(":key:") + " Here is the hero list " + emojize(":key:") + "------------------")
print(Fore.BLUE + "Captain American", Fore.RED + "Iron Man", Fore.RED + Style.DIM + "Black Widow", Fore.MAGENTA + "Hawkeye", Fore.YELLOW + "Thor", Fore.GREEN + "Hulk")
print("----------------------------------------------------------------\n")
input("Enter Anything To Start The Questions:")
print("\n")

print(Back.YELLOW + Fore.BLACK + "Question 1/5")
answer1 = questions["q1"][input(questions["q1"]["question"])]
vars.quizTotal += answer1

print(Back.YELLOW + Fore.BLACK + "Question 2/5")
answer2 = questions["q2"][input(questions["q2"]["question"])]
vars.quizTotal += answer2

print(Back.YELLOW + Fore.BLACK + "Question 3/5")
answer3 = questions["q3"][input(questions["q3"]["question"])]
vars.quizTotal += answer3

print(Back.YELLOW + Fore.BLACK + "Question 4/5")
answer4 = questions["q4"][input(questions["q4"]["question"])]
vars.quizTotal += answer4

print(Back.YELLOW + Fore.BLACK + "Question 5/5")
answer5 = questions["q5"][input(questions["q5"]["question"])]
vars.quizTotal += answer5
print("----------------------------------------------------------------\n")

print("========================= Final Result =========================\n")
print("Score: " + str(vars.quizTotal) + "\n")
quizTally.total(vars.quizTotal)
print("----------------------------------------------------------------\n")

