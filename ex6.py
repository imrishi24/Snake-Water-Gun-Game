import random
print("Game started!")
list=["Snake","Water","Gun"]
print("Enter S for Snake")
print("Enter W for Water")
print("Enter G for Gun")
us=0
cs=0
d=0
for ch in range(0,10):
    up=input().capitalize()
    cp=random.choice(list)
    if up == "S":

        if cp == "Snake":
            print("Draw")
            d=d+1
            continue
        elif cp == "Water":
            print("You win")
            us=us+1
            continue
        else:
            print("Computer wins")
            cs=cs+1
            continue
    elif up == "W":

        if cp == "Snake":
            print("Computer wins")
            cs=cs+1
            continue
        elif cp == "Water":
            print("Draw")
            d=d+1
            continue
        else:
            print("You win")
            us=us+1
            continue
    elif up == "G":

        if cp == "Snake":
            print("You win")
            us=us+1
            continue
        elif cp == "Water":
            print("Computer wins")
            cs=cs+1
            continue
        else:
            print("Draw")
            d=d+1
            continue
    else:
        print("Enter the valid input")
        continue



print("\n\nGame Ended!")


print("Your Score is\n",us)
print("Computer's Score is\n",cs)
print("Total Draw=\n",d)
if us > cs:
    print("You won the Game!\n")
elif us < cs:
    print("Computer Won the Game")
else:
    print("Game is draw")



