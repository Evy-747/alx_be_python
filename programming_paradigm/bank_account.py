class BankAccount:
    """
    A simple BankAccount class to manage deposits, withdrawals, and balance display.
    """
    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an optional initial balance (default is 0).
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        :param amount: Amount to be deposited.
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Invalid deposit amount. Must be greater than 0.")

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if sufficient funds exist.
        :param amount: Amount to be withdrawn.
        :return: True if the withdrawal was successful, False otherwise.
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        elif amount > self.__account_balance:
            print("Insufficient funds.")
            return False
        else:
            print("Invalid withdrawal amount. Must be greater than 0.")
            return False

    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")

