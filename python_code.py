class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def __str__(self):
        return f"Customer: {self.name}\nAddress: {self.address}"


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} into Account {self.account_number}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from Account {self.account_number}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account {self.account_number}\nBalance: ${self.balance:.2f}"


# Creating instances
customer1 = Customer("Alice", "123 Main St")
account1 = BankAccount("A123")
account2 = BankAccount("A456", 500)

customer1.add_account(account1)
customer1.add_account(account2)

# Performing operations
account1.deposit(1000)
account2.withdraw(200)
print(customer1)
print(account1)
print(account2)

