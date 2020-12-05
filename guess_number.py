# Import random module
import random



# Random number Variable
randomNumber = random.randrange(1, 50)

# Input From the User
userNumber = int(input("Enter Random number between 1 to 50: "))

# Condition for random NUmber Guess Execution
while userNumber != randomNumber:

    if randomNumber > userNumber:
        print("Enter higher value number: ")
        userNumber = int(input("Enter Random number between 1 to 50: "))
    else:
        print("Enter Lower value number: ")
        userNumber = int(input("Enter Random number between 1 to 50: "))

print(f"Your guess is Correct {userNumber}:", randomNumber)
