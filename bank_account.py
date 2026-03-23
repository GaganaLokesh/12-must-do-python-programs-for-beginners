class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited successfully. Current balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdraw successful. Current balance: {self.balance}")
        else:
            print("Insufficient Balance ")

    def check_balance(self):
        print(f"Your account balance is: {self.balance}")


account = BankAccount(1000)

while True:
    print("\n--------- MENU ---------")
    print("1. Deposit Cash")
    print("2. Withdraw Cash")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = int(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == "2":
        amount = int(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Exiting... ")
        break

    else:
        print("Invalid choice ")