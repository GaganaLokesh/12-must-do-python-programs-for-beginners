filename="notes.txt" 
while True:
    print("\n-------Menu----") 
    print("1.Add note") 
    print("2.Read file") 
    print("3.Delete Notes") 
    print("4.Search note") 
    print("5.Exit") 
    choice= input("Enter your choice: ") 
    
    if choice=="1": 
        note=input("\nWrite your note: ") 
        with open(filename, "a") as file: 
            file.write(note+"\n") 
            print("\nNote saved") 
    elif choice=="2": 
        try: 
            with open(filename,"r") as file: 
                print("\nYour notes....") 
                i=1 
                for line in file: 
                    print(f"{i},{line.strip()}") 
                    i+=1 
        except FileNotFoundError: 
            print("No notes found!") 
    elif choice=="3": 
        with open(filename, "w")as file: 
            pass 
        print("Deleted successfully..") 
    elif choice=="4": 
        keyword=input("Enter keyword: ") 
        try: 
            with open(filename,"r") as file: 
                found = False 
                for line in file: 
                    if keyword in line: 
                        print(line.strip()) 
                        found = True 
                    if not found: 
                        print("No matching note found") 
        except FileNotFoundError: print("No notes found!") 
    elif choice=="5": 
        print("Exiting..") 
        break 
    else: 
        print("Invalid choice!!") 
    
# 1. open() -> Manually opens file and Must close using file.close() 
#  vs  with open()->Automatically opens and closes file and Prevents errors and memory leaks 
# 2. f-string (formatted string)->print(f"{i}. {line.strip()}")/Used to insert variables inside string 
# {} → placeholder 
# 3. strip()-> line.strip()/ Removes: newline (\n) and extra spaces