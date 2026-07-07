#Number Guessing Game
#Mauricio Garcia
# This is a game that helps u guess a random number
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
        print("Please choose between a number between 0 and 3")
        
   


secretNumber = establishingCaseScenarios(difficulty_select)
#print(f"Secret number is: {secretNumber}")

guessed = False
while guessed is False:
    attempts += 1
    print("Guess!")

    yourNumber = int(input())
    if yourNumber == secretNumber:
        
        print("Congratulations, u right!\n Attempts:", attempts)
        guessed = True
        
    elif yourNumber < secretNumber:
        print("Too low, try higher")
    else:
        print("too high, try lower")
        
        
