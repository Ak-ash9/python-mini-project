import random
print("_________Lets play game___________")
a=input("Enter player name:")
print("hello",a)
print("Game start........")
att=6
print("Enter the range whom you want to select a number")
b=int(input("Enter the starting value:-"))
c=int(input("Enter the ending value:-"))
d=random.randint(b,c)
while att:
    n=int(input("Enter your chosen number:-"))
    if n<d:
        print("Number is too small.")
    elif n>d:
        print("Number is too large.")
    else:
        print("Number is same.")
        print("You are the winner.")
    att-=1
    print("You have left only",att,"attempt")
print("Correct answer is",d)
print("You lose.........")