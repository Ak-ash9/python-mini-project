import random
print("_________Lets play game___________")
a=input("Enter player name:")
print("hello",a)
print("Game start......")
print("Rules for playing this game-")
print("1.Rock beats Scissor.")
print("2.Scissor beats Paper.")
print("3.Paper beats Rock.")
ls=["Rock","Paper","Scissor"]
a=random.choice(ls)
b=input("Enter your choice:")
if a == b:
    print("No one lose or win...")
elif a=="Rock" and b=="Paper" or a=="Paper" and b=="Scissor" or a=="Scissor" and b=="Rock":
    print("You win.")
elif a=="Scissor" and b=="Paper" or a=="Paper" and b=="Rock" or a=="Rock" and b=="Scissor":
    print("You lose.")
else:
    print("Thank You.....")
    
    
    
    
    
    

