import random
def roll_dice():
    return random.randint(1,6)
while True:
    user_input=input("enter to roll dice")
    if user_input.lower()=="q":
        print("thank for playing!")
        break
    else:
     print("you rolled:",roll_dice())
