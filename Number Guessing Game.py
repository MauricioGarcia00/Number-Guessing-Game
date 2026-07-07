# Number Guessing Game
# Mauricio Garcia
# A simple terminal-based game where the player selects a difficulty level and tries to guess a randomly generated number.
# The difficulty determines the range of possible numbers, while the game provides hints after each incorrect guess.
# This project was a good exercise for practicing functions, loops, user input validation, conditionals, and Python's random module.


import random

def establishingCaseScenarios(difficultySelected):
    match int(difficultySelected):
        case 0:
            secretNumber = random.randint(0,2)
            return secretNumber
        case 1:
            secretNumber = random.randint(1,5)
            return secretNumber
        case 2:
            secretNumber = random.randint(1,10)
            return secretNumber
        case 3:
            secretNumber = random.randint(1,100)
            return secretNumber 
        case 4:
            secretNumber = random.randint(1,1000)
            return secretNumber 
difficultiesList = ["0","1","2","3","4"]
attempts = 0 





print("Please select your difficulty")
print("-0 Baby Level \n-1 Easy \n-2 Normal\n-3 Hard\n-4 Very Hard")
difficultySelected = False

while difficultySelected is False:
    difficulty_select= input(": ")
    if difficulty_select in difficultiesList:
        difficultySelected = True
    else:
        print("Please choose between a number between 0 and 4")
        
        
   


secretNumber = establishingCaseScenarios(difficulty_select)
#print(f"Secret number is: {secretNumber}")

guessed = False



while guessed is False:
    attempts += 1
    print("Guess!")
    try:
        yourNumber = int(input())
        if yourNumber < 0:
            print("Positive numbers only")
            continue

    except ValueError:
        print("Please enter a number, not a letter or a decimal.")
        continue
    if yourNumber == secretNumber:
        print("Congratulations, u right!\n Attempts:", attempts)
        guessed = True
    elif yourNumber < secretNumber:
        print("Too low, try higher")
    else:
        print("too high, try lower")
