import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp =='s':
        if you == 'w':
            return False
        elif you =='g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you=='s':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you=='w':
            return True
    pass

randNo =  random.randint(1,2)
print(randNo)
if randNo == 1:
    comp = 's'
elif randNo== 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
    
you = input("Your turn: Snake(s) Water(w) gun(g):")
a= gameWin(comp,you)

print(f"computer choose : {comp}")
print(f"You choose : {you}")


if a ==None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")