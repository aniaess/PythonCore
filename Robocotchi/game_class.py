from abc import ABC, abstractmethod

class Game(ABC):

    def __init__(self):
        self.results = {"user": 0, "robot": 0, "Draws": 0}
        self.comp = 0
        self.user = 0
        self.a = 0
        self.b = 0

    @abstractmethod
    def user_input(self):
        ...

    @abstractmethod
    def robot_input(self):
        ...

    @abstractmethod
    def game(self):
        ...
    @abstractmethod
    def compare(self):
        if self.a == self.b:
            self.results["Draws"] += 1
            print("It's a draw!")
        elif self.a > self.b:
            self.results["robot"] += 1
            print("The robot won!")
        else:
            self.results["user"] += 1
            print("You won!")

    def show_results(self):
        print(f"You won: {self.results['user']},")
        print(f"The robot won: {self.results['robot']},")
        print(f"Draws: {self.results['Draws']}.")

    def game_menu(self):
        while True:
            self.user_input()
            if self.user == "exit game":
                self.show_results()
                break
            else:
                self.game()