import time
import os
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        return f"Personal Details:\n-----------------\nName: {self.name.title()}\nAge: {self.age}\n"

class Account(User): #inherits from user
    #attributes
    total_deposits = 1 #count the initial deposit on acc creation
    total_withdraws = 0
    def __init__(self, name, age, balance):
        super().__init__(name, age)
        self.balance = balance

    def show_balance(self):
        return f"{self.name} has a remaining balance of: £ {round(self.balance, 2)}\n"

    def deposit(self):
        dp = float(input("Please enter how much money you want to deposit: "))
        print("Thank you for depositing...")
        time.sleep(1)
        self.balance += dp # add recent deposit to current balance
        self.total_deposits += 1 #increment deposit count
        return f"Your balance is now: {round(self.balance, 2)}"
    
    def withdraw(self):
        wd = float(input("Please enter how much you would like to withdraw: "))
        if wd <= self.balance:
            print("Withdrawing from your balance...")
            time.sleep(1)
            self.balance -= wd
            self.total_withdraws += 1
            return f"Your balance is now: {round(self.balance, 2)}"
        else:
            print("You have insufficent funds to make this withdrawal.")
            return f"Please deposit more funds to make this withdrawal."

def options(client):
    os.system('cls')
    print("Thanks for creating your account")
    print("Here are a list of options, please choose the number you want. ")
    while True:
        option_choice = int(input("1. See Balance.\n2. Withdraw.\n3. Deposit.\n4. See Total Withdraws.\n5. See Total Deposits.\n6. Exit\n"))
        match option_choice:
            case 1:
                print(account.show_balance())
            case 2:
                print(account.withdraw())
            case 3:
                print(account.deposit())
            case 4:
                print(f"There have been {account.total_withdraws}")
            case 5:
                print(f"There have been {account.total_deposits}")
            case 6:
                print("Thank you for using PyBank!")
                exit()
            case default:
                print("Please give valid input")
                

def set_balance(name):
    balance = float(input(f"{name.title()}, how much money would you like to initially deposit? "))
    return balance

while True:
    print("Welcome to PyBank!")
    print("We appreciate you choosing us as your bank!")
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    client = User(name, age)
    client_balance = set_balance(name)
    account = Account(client.name, client.age, client_balance)
    print("Creating your account...")
    print("\nAccount details: ")
    print(client.show_details())
    time.sleep(2)
    pick = options(client)