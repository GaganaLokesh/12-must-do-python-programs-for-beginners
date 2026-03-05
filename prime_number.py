num=int(input("Enter a number: "))
for i in range(2,num):
    if num%i==0:
        print("Not a prime number")
        break
    # Here the else belongs to for, not if(The else block runs only if the loop finishes normally.)
    #break occurs->else does NOT run
else:                        
    print("prime number")