class BankAccount:
    def __init__(self):
        self.name = ""
        self.account_no = 0
        self.initial_balance = 0

    def input_data(self):
        self.name = input("Enter your name: ")
        self.account_no = int(input("Enter your account number: "))
        self.initial_balance = int(input("Enter the initial balance: "))
        print("----------------------------------------------")

    def show_data(self):
        print("Name:", self.name)
        print("Account No.:", self.account_no)
        print("Initial Balance:", self.initial_balance)
        print("----------------------------------------------")

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        self.initial_balance += amount
        print("Name:", self.name)
        print("Account No.:", self.account_no)
        print("Total Balance:", self.initial_balance)
        print("----------------------------------------------")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount <= self.initial_balance:
            self.initial_balance -= amount
            print("Name:", self.name)
            print("Account No.:", self.account_no)
            print("Remaining Balance:", self.initial_balance)
            print("----------------------------------------------")
        else:
            print("Error: Insufficient funds.")
            print("----------------------------------------------")

obj = BankAccount()
obj.input_data()
obj.show_data()
obj.deposit()
obj.withdraw()