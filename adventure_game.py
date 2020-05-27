# User input game
answer = input("Would you like to play game? : (yes/no) ").lower().strip()

if answer == "yes":
    answer = input("You have four way road which side would you like to go left right or stright: ").lower().strip()
    if answer == "left":
        answer = input('there is moster in left side would like to face or run: ').lower().strip()
        if answer == "face":
            print("you loose not good idea to face moster")
        else:
            print('your safe to go home')
    elif answer == "right":
        answer = input('you have Money and Love in this side which one would you like to move: ').lower().strip()
        if answer == "money":
            print("you have to go way more way to great life: ")
        else:
            print("your happy what you have")
    else:
        print('your going to have diffrent path in life')
else:
    print('this is too bad :-(')
