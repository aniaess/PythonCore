import random
from db_manager import DataBase

class BankingSystem():

    def __init__(self):
        self.database = []
        self.card_num = ""
        self.storing_data = DataBase()

    def luhn_algorithm(self, my_card):
        number = list(my_card)
        multiplied = [int(number[x]) * 2 if x % 2 == 0 else int(number[x]) for x in range(len(number))]
        substracted = [x - 9 if x > 9 else x for x in multiplied]
        suma = str(sum(substracted))
        return suma

    def checking_card(self, number_to_transfer):
        suma = self.luhn_algorithm(number_to_transfer[:-1])
        if (int(suma) + int(number_to_transfer[-1])) % 10 == 0:
            return number_to_transfer

    def create_account(self):
        my_card = "400000"
        pin = ""
        checksum = 0
        for i in range(9):
            my_card += str(random.randint(0,9))
        suma = self.luhn_algorithm(my_card)
        if suma[1] != "0":
            checksum = 10 - int(suma[1])
        valid_card = my_card + str(checksum)
        for i in range(4):
            pin += str(random.randint(0,9))
        self.database = [valid_card, pin, 0]
        self.storing_data.insert_customer(self.database)
        print("Your card has been created")
        print("Your card number:",valid_card, sep = "\n")
        print("Your card PIN:",pin, sep = "\n")

    def log_into_account(self):
        self.card_num = input("Enter your card number:\n")
        my_pin = input("Enter your PIN:\n")
        if self.storing_data.log_into(self.card_num, my_pin):
            print("\nYou have successfully logged in!")
            return 1
        else:
            print("\nWrong card number or PIN!")

    def add_income(self):
        income = int(input("Enter income:\n"))
        self.storing_data.add_money(self.card_num, income)
        print("Income was added")

    def transfer(self):
        print("\nTransfer")
        while True:
            number_to_transfer = input("Enter card number:\n")
            if self.checking_card(number_to_transfer):
                if number_to_transfer != self.card_num:
                    if self.storing_data.checking_if_exist(number_to_transfer):
                        money = int(input("Enter how much money you want to transfer:\n"))
                        if money < self.storing_data.balance(self.card_num):
                            self.storing_data.transfer_money(self.card_num, number_to_transfer, money)
                            print("Success!")
                        else:
                            print("Not enough money!")
                        break
                    else:
                        print("Such a card does not exist")
                        break
                else:
                    print("You can't transfer money to the same account!")
                    break
            else:
                print("Probably you made a mistake in the card number. Please try again!")
                break

    def menu_bank(self):
        while True:
            user = input("1. Create an account\n2. Log into account\n0. Exit\n")
            print()
            if user == "1":
                self.create_account()
            elif user == "2":
                if self.log_into_account():
                    while True:
                        logged_in_user = input("""\n1. Balance\n2. Add income\n3. Do transfer
4. Close account\n5. Log out\n0. Exit\n""")
                        if logged_in_user == "1":
                            print(f"\nBalance: {self.storing_data.balance(self.card_num)}")
                        elif logged_in_user == "2":
                            self.add_income()
                        elif logged_in_user == "3":
                            self.transfer()
                        elif logged_in_user == "4":
                            self.storing_data.close_account(self.card_num)
                            break
                        elif logged_in_user == "5":
                            break
                        else:
                            print("Bye!")
                            exit()
            elif user == "0":
                print("Bye!")
                exit()
            print()

customer = BankingSystem()
customer.menu_bank()