# Demonstrates classes, objects, constructors, methods, and encapsulation.

class BankAccount:
    """A simple bank account with basic transaction operations."""

    def __init__(self, account_holder, opening_balance=0.0):
        self.account_holder = account_holder
        self.__balance = float(opening_balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited Rs. {amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrawn Rs. {amount:.2f}")

    def get_balance(self):
        return self.__balance

    def display_details(self):
        print("\\nAccount summary")
        print("----------------")
        print("Holder:", self.account_holder)
        print(f"Balance: Rs. {self.__balance:.2f}")


def main():
    account = BankAccount("Aarav", 2500)
    account.display_details()
    account.deposit(1000)
    account.withdraw(700)
    account.withdraw(5000)
    account.display_details()


if __name__ == "__main__":
    main()
