import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.deposit(amount)
        else:
            print("Insufficient funds")

class BankingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.accounts = {}  
        self.create_account("abi", 1000) 
        self.initUI()

    def create_account(self, name, balance):
        account = Account(name, balance)
        self.accounts[name] = account

    def initUI(self):
        self.setWindowTitle('Online Banking System')
        self.setGeometry(100, 100, 400, 200)

        self.name_label = QLabel('Account Name:')
        self.name_input = QLineEdit()
        self.balance_label = QLabel('Balance:')
        self.balance_input = QLineEdit()

        self.deposit_button = QPushButton('Deposit Funds')
        self.withdraw_button = QPushButton('Withdraw Funds')
        self.transfer_button = QPushButton('Transfer Funds')

        self.deposit_button.clicked.connect(self.deposit)
        self.withdraw_button.clicked.connect(self.withdraw)
        self.transfer_button.clicked.connect(self.transfer)

        vbox = QVBoxLayout()
        vbox.addWidget(self.name_label)
        vbox.addWidget(self.name_input)
        vbox.addWidget(self.balance_label)
        vbox.addWidget(self.balance_input)
        vbox.addWidget(self.deposit_button)
        vbox.addWidget(self.withdraw_button)
        vbox.addWidget(self.transfer_button)

        self.setLayout(vbox)

    def deposit(self):
        amount = float(self.balance_input.text())
        if amount > 0:
            account_name = self.name_input.text()
            if account_name:
                if account_name in self.accounts:
                    self.accounts[account_name].deposit(amount)
                    self.balance_input.setText(str(self.accounts[account_name].balance))
                else:
                    print("Account not found")
            else:
                print("Please enter an account name")
        else:
            print("Invalid deposit amount")

    def withdraw(self):
        amount = float(self.balance_input.text())
        if amount > 0:
            account_name = self.name_input.text()
            if account_name:
                if account_name in self.accounts:
                    self.accounts[account_name].withdraw(amount)
                    self.balance_input.setText(str(self.accounts[account_name].balance))
                else:
                    print("Account not found")
            else:
                print("Please enter an account name")
        else:
            print("Invalid withdrawal amount")

    def transfer(self):
        recipient_name = self.name_input.text()
        amount = float(self.balance_input.text())
        if amount > 0:
            account_name = self.name_input.text()
            if account_name and recipient_name:
                if account_name in self.accounts and recipient_name in self.accounts:
                    self.accounts[account_name].transfer(self.accounts[recipient_name], amount)
                    self.balance_input.setText(str(self.accounts[account_name].balance))
                    print("successfully transferred")
                else:
                    print("One or both accounts not found")
            else:
                print("Please enter account names")
        else:
            print("Invalid transfer amount")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    banking_app = BankingApp()
    banking_app.show()
    sys.exit(app.exec_())