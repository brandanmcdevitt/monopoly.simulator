class Players:

    total_players = 0

    def __init__(self, name, token, balance=1500):
        self.name = name
        self.token = token
        self.balance = balance
        self.total_players += 1

    def get_balance(self):
        return self.balance

    def add_money(self, amount):
        self.balance += amount
        return self.balance

    def remove_money(self, amount):
        self.balance -= amount
        return self.balance


class Banker(Players):
    def __init__(self, name, token, balance=1500, bank=0):
        super().__init__(name, token)
        self.bank = bank

    def add_to_bank(self, amount):
        self.bank += amount
        return self.bank

    def remove_from_bank(self, amount):
        self.bank -= amount
        return self.bank

    def get_bank_balance(self):
        return self.bank
    