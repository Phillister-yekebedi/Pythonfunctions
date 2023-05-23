# 2) Create a files in the classes directory bank.py. Define the following class
# in each module respectively. 

# Each class should have one class attribute and three instance variables.

class Bank:
    account_name = "account_name"
    account_type = "account_type"
    balance = "balane"


class Bank:
    place_located = "Nairobi"

    def __init__(self, name, account_type, balance):
        self. account_name = name
        self.account_type = account_type
        self.balance = balance

    def detail(self):
        return f"{self.name} has a {self.balance} balance in her{self.account_type} Euros."