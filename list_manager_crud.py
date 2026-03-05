items= []
while True:
    print("1. Add item")
    print("2. Delete item")
    print("3. Show item")
    print("4. Exit")

    choice=int(input("Enter your choice: "))
    if choice==1:
        item=input("Enter item: ")
        if item in items:
            items.append(item)
        else:
            print("Item doesn't exist")
    elif choice==2:
        item=input("Enter item to delete: ")
        items.remove(item)
    elif choice==3:
        print(items)
    else:
        break