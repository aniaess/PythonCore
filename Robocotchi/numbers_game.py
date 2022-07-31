from exceptions import LessThanZeroError, MoreThanMilionError
import random
from game_class import Game


class Numbers(Game):

    def __init__(self):
        self.number = 0
        super().__init__()

    def generate_num(self):
        self.number = random.randint(0, 1000000)
        print(f"The goal number is {self.number}")

    def robot_input(self):
        self.comp = random.randint(0, 1000000)
        print(f"\nThe robot entered the number {self.comp}.")

    def user_input(self):
        while True:
            user = input("What is your number? Type 'exit game' to cancel.\n")
            if user == "exit game":
                self.user = user
                break
            else:
                try:
                    if int(user) > 1000000:
                        raise MoreThanMilionError
                    elif int(user) < 0:
                        raise LessThanZeroError
                    else:
                        self.user = int(user)
                        break
                except ValueError:
                    print("A string is not a valid input!")
                except MoreThanMilionError as err:
                    print(err)
                except LessThanZeroError as err:
                    print(err)

    def compare(self):
        self.a = abs(self.number - int(self.user))
        self.b = abs(self.number - self.comp)
        super().compare()

    def game(self):
        self.robot_input()
        self.generate_num()
        self.compare()