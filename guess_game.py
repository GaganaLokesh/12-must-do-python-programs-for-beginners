import random #The random module in Python is used to generate random values.
number=random.randint(1,10) #It takes 2 parameters, upper limit and lower limit to generate the number

# print(number)
guess=int(input("Guess the number:"))
while guess!=number:
    if(guess<number):
        print("Try higher number")
    elif(guess>number):
        print("Try lesser number")
    guess=int(input("Guess Again: "))
print("You won!")