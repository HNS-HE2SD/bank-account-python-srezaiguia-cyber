# Class Client
class Client:
    def __init__(self, CIN, firstName, lastName, tel=""):
        self.__CIN = CIN
        self.__firstName = firstName
        self.__lastName = lastName
        self.__tel = tel
        self.__accounts = []   

    # Getters and setters
    def get_CIN(self): return self.__CIN
    def get_firstName(self): return self.__firstName
    def get_lastName(self): return self.__lastName
    def get_tel(self): return self.__tel
    def set_tel(self, tel): self.__tel = tel

    # multiple accounts
    def add_account(self, account):
        self.__accounts.append(account)

    # Display all client accounts
    def displayAccounts(self):
        print(f"Accounts of {self.__firstName} {self.__lastName}:")
        if not self.__accounts:
            print("No accounts found.")
        else:
            for account in self.__accounts:
                print(f" Account {account.get_code()} , Balance: {account.get_balance()}")

    def display(self):
        print(f"CIN: {self.__CIN}, Name: {self.__firstName} {self.__lastName}, Tel: {self.__tel}")


# Class Account
class Account:
    __nbAccounts = 0  # static variable for sequential codes

    def __init__(self, owner):
        Account.__nbAccounts += 1
        self.__code = Account.__nbAccounts
        self.__balance = 0.0
        self.__owner = owner
        self.__transactions = []  # store history
        owner.add_account(self)   # add account to client

    # Access methods
    def get_code(self): return self.__code
    def get_balance(self): return self.__balance
    def get_owner(self): return self.__owner

    # Credit method
    def credit(self, amount, account=None):
        if amount <= 0:
            print("Error, Amount must be positive!")
            return
        self.__balance += amount

        # Record transaction
        if account is None:
            self.__transactions.append(f"Credit,+ {amount}")
        else:
            self.__transactions.append(f"Credit from Transfer: +{amount}")

    # Debit method
    def debit(self, amount, account=None):
        if amount <= 0:
            print("Error, Amount must be positive!")
            return
        if self.__balance < amount:
            print("Insufficient balance.")
            return
        self.__balance -= amount

        # Record transaction
        if account is None:
            self.__transactions.append(f"Debit: -{amount}")

    # Transfer from this account to another
    def transfer(self, amount, target_account):
        if not isinstance(target_account, Account):
            print("Error, Invalid target account.")
            return
        if amount <= 0:
            print("Error, Amount must be positive!")
            return
        if self.__balance < amount:
            print("Transfer failed: insufficient balance.")
            return
        self.debit(amount, target_account)
        target_account.credit(amount, self)
        self.__transactions.append(f"Transfer to Account {target_account.get_code()}: -{amount}")
        target_account.__transactions.append(f"Transfer from Account {self.get_code()}: +{amount}")

    # Display account info
    def display(self):
        print(f"Account Code: {self.__code}")
        print(f"Owner: {self.__owner.get_firstName()} {self.__owner.get_lastName()}")
        print(f"Balance: {self.__balance} ")

    # Display transaction history
    def displayTransactions(self):
        print(f"Transaction History for Account {self.__code}:")
        if not self.__transactions:
            print("No transactions yet.")
        else:
            for transactions in self.__transactions:
                print(" -", transactions)

    @staticmethod
    def displayNbAccounts():
        print("Total accounts created:", Account.__nbAccounts) 



