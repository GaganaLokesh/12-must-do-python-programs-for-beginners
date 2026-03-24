items= []  #creates an empty list in Python(A list is a collection of items)
while True:  #Keep running until manually stop you using break
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

# Common List Functions (Methods)
# 1. append()
# 👉 Adds item at the end

# items = [1,2]
# items.append(3)
# # [1,2,3]

# 2. insert()
# 👉 Insert at specific position

# items = [1,2]
# items.insert(1, 10)
# # [1,10,2]

# 3. remove()
# 👉 Removes specific value

# items = [1,2,3]
# items.remove(2)
# # [1,3]

# 4. pop()
# 👉 Removes using index (default last)

# items = [1,2,3]
# items.pop()
# # [1,2]

# items.pop(0)
# # removes 1

# 5. clear()
# 👉 Removes all elements

# items = [1,2,3]
# items.clear()
# []

# 6. index()
# 👉 Returns position of element

# items = [10,20,30]
# items.index(20)
# #1

# 7. count()
# 👉 Counts occurrences

# items = [1,2,2,3]
# items.count(2)
# 2

# 8. sort()
# 👉 Sorts list

# items = [3,1,2]
# items.sort()
# [1,2,3]

# 9. reverse()
# 👉 Reverses list

# items = [1,2,3]
# items.reverse()
# # [3,2,1]

# 10. copy()
# 👉 Creates a copy

# items = [1,2]
# new_list = items.copy()
# len(items)    # length
# max(items)    # maximum
# min(items)    # minimum
# sum(items)    # sum