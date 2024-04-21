class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit successful. New balance is {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrawal successful. New balance is {self.balance}"

    def display_balance(self):
        return f"Current balance is {self.balance}"

# if __name__ == "__main__":
    # Creating an object with an initial balance of 1000
# account = BankAccount(1000)

# # Making transactions and displaying balance
# print(account.deposit(500))        # Output: Deposit successful. New balance is 1500
# print(account.withdraw(2000))      # Output: Insufficient funds
# print(account.withdraw(500))       # Output: Withdrawal successful. New balance is 1000
# print(account.display_balance())   # Output: Current balance is 1000
