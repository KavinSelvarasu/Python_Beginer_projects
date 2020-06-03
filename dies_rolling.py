# importing random number generator
import random

play = input('would you like to roll dies: ').strip().lower()
if play == 'yes':
    rolls = int(input("Enter number of dies to roll: "))


    def diesRoll(rolls):

        for i in range(0, rolls):
            dies = random.randint(1, 6)
            print(dies)


    diesRoll(rolls)
else:
    exit()



