from game_class import Game
import random

class RSP(Game):

    def __init__(self):
        self.choices = ["paper", "rock", "scissor"]
        super().__init__()

    def robot_input(self):
        self.comp = random.choice(self.choices)
        print(f"\nThe robot chose {self.comp}")

    def user_input(self):
        while True:
            user = input("\nWhat is your move? Type 'exit game' to cancel.\n")
            if user == "exit game":
                self.user = user
                break
            elif user in self.choices:
                self.user = user
                break
            else:
                print("No such option! Try again!")

    def compare(self):
        if self.user == "rock":
            if self.comp == "scissor":
                self.b = 1
            elif self.comp == "paper":
                self.a = 1
        elif self.user == "paper":
            if self.comp == "rock":
                self.b = 1
            elif self.comp == "scissor":
                self.a = 1
        else:
            if self.comp == "paper":
                self.b = 1
            elif self.comp == "rock":
                self.a = 1
        super().compare()
        self.a, self.b = 0, 0

    def game(self):
        self.robot_input()
        self.compare()