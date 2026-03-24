contacts={}  #Creates an empty dictionary (Dictionary stores data in key : value pairs)
while True:
    print("-----MENU------")
    print("1.Add contact")
    print("2.Search contact")
    print("3.Delete contact")
    print("4.Show contacts")
    print("5.Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        name=input("Enter name: ")
        number=(input("Enter contact number: "))
        contacts[name]=number  #Store number as value for the key name| Key does NOT exist->New entry is created, else Value gets updated
    elif choice==2:
        name=input("Enter name to search: ")
        if name in contacts:
            print(contacts[name])
        else:
            print("Contact not found")
    elif choice==3:
        name=input("Enter name to delete contact: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted")
        else:
            print("No such contact exists!!")
    elif choice==4:
        for name, number in contacts.items():
            print(name, ":", number)   
    elif choice==5:
        break
    else:
        print("Invalid choice")

# Add contact:
# contacts[name] = number

# 👉 Add or update contact

# Search contact:
# if name in contacts:
#     print(contacts[name])

# 👉 Check key exists → then access value

# Delete contact:
# del contacts[name]

# 👉 Removes key-value pair

# Show all:
# for name, number in contacts.items():

# 👉 .items() gives:

# ("Gagana", "9876")
# ("Rahul", "9123")