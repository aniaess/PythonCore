class Bank():

    def __init__(self):
        self.money = 550

    def display_money(self):
        print(f"${self.money} of money\n")

    def widraw_money(self):
        money = self.money
        self.money = 0
        print("I gave you", money,"\n")
        return money

    def update_money(self, price):
        self.money += price