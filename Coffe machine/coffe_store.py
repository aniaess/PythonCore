class Magazine():

    def __init__(self):
        self.supply = {"water": 400, "milk": 540, "coffee beans": 120, "dispossable cups": 9}

    def fill_machine(self):
        water = int(input("Write how many ml of water do you want to add:\n"))
        milk = int(input("Write how many ml of milk do you want to add:\n"))
        coffe_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
        cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))
        self.supply["water"] += water
        self.supply["milk"] += milk
        self.supply["coffee beans"] += coffe_beans
        self.supply["dispossable cups"] += cups

    def display_machine_state(self):
        print("The coffee machine has:")
        for k, v in self.supply.items():
            print(f"{v} of {k}")

    def buying_a_coffe(self, ingredients):
        magazine = self.supply
        for k,v in magazine.items():
            if magazine[k] - ingredients[k] < 0:
                return f"Sorry, not enough {k}!"
            else:
                magazine[k] -= ingredients[k]
        else:
            self.supply = magazine