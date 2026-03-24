filename = "tasks.txt"

def add_task():
    note=input("\nWrite your note: ") 
    with open(filename, "a") as file: 
            file.write(note+"\n") 
            print("\nNote saved") 

def view_tasks():
    try:
        with open(filename,"r") as file: 
            print("\nYour notes....") 
            i=1 
            for line in file: 
                print(f"{i},{line.strip()}") 
                i+=1 
    except FileNotFoundError: 
            print("No notes found!")

def delete_tasks():
     with open(filename, "w")as file: 
            pass
     print("Deleted successfully..") 
     
while True:
    print("\n------ TO-DO MENU ------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete All Tasks")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_tasks()

    elif choice == "4":
        print("Exiting... 👋")
        break

    else:
        print("Invalid choice")