num1=int(input("Enter 1st number:")) #input():Used to take input from user,By default it returns string

num2=int(input("Enter 2nd number:"))#Type Conversion — int():Converts string input to integer,Needed for mathematical operations

operation=input("Enter operation (+, -,*,/, %):")
#Conditional Statements — if-elif-else
if(operation=="+"):
    print("result: ",num1+num2)
elif(operation=="-"):
    print("result: ", num1-num2)
elif(operation=="*"):
    print("result ",num1*num2)
elif(operation=="/"):
    if num2==0:
        print("Can not be divided byb  zero")
    else:
        print("result: ",num1/num2)
elif(operation=="%"):
    print("result: ", num1%num2)
else:
    print("Invalid operation")
