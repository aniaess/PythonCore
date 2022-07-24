from coffe_store import Magazine
from bank import Bank


class CoffeMachine():

    def __init__(self):
        self.espresso = {"water": 250, "milk": 0, "coffee beans": 16, "dispossable cups": 1}
        self.latte = {"water": 350, "milk": 75, "coffee beans": 20, "dispossable cups": 1}
        self.cappuccino = {"water": 200, "milk": 100, "coffee beans": 12, "dispossable cups": 1}
        self.prices = {"espresso": 4, "latte": 7, "cappuccino": 6}
        self.coffes = {1: "espresso", 2: "latte", 3 : "cappuccino"}
        self.magazine = Magazine()
        self.money = Bank()

    def main(self):
        while True:
            user = input("Write action (buy, fill, take, remaining, exit):\n")
            print()
            if user == "fill":
                self.magazine.fill_machine()
            elif user == "take":
                self.money.widraw_money()

            elif user == "buy":
                while True:
                    coffe = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
                    if coffe == "back":
                        break
                    elif int(coffe) == 1:
                        i =self.magazine.buying_a_coffe(self.espresso)
                    elif int(coffe) == 2:
                        i = self.magazine.buying_a_coffe(self.latte)
                    elif int(coffe) == 3:
                        i = self.magazine.buying_a_coffe(self.cappuccino)
                    if i:
                        print(i)
                    else:
                        print("I have enough resources, making you a coffee!")
                        self.money.update_money(self.prices[self.coffes[int(coffe)]])
                        print()
                    break
            elif user == "remaining":
                self.magazine.display_machine_state()
                self.money.display_money()
                print()
            elif user == "exit":
                break


coffe = CoffeMachine()
coffe.main()
