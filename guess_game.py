import random
number=random.randint(1,10)
# print(number)
guess=int(input("Guess the number:"))
while guess!=number:
    if(guess<number):
        print("Try higher number")
    elif(guess>number):
        print("Try lesser number")
    guess=int(input("Guess Again: "))
print("You won!")