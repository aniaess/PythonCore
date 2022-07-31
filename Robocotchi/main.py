from robopet import Robocotchi


class Menu:
    options = ["info", "exit", "recharge", "sleep", "play", "work", "learn", "oil"]

    def __init__(self):
        robot_name = input("How will you call your robot?\n")
        self.robot = Robocotchi(robot_name)

    def main_menu(self):
        while True:
            if self.robot.rust == 100:
                print(f"{self.robot.name} is too rusty! Game over.")
                break
            if self.robot.overheat == 100:
                print(f"The level of overheat reached 100, {self.robot.name} has blown up! Game over.")
                break
            print(
                f"\nAvailable interactions with {self.robot.name}:\nexit - Exit\ninfo - Check the vitals\nwork - Work",
                "\nplay - Play\noil - Oil\nrecharge - Recharge\nsleep - Sleep mode\nlearn - Learn skills")
            mode = input("Choose:\n")
            if mode not in Menu.options:
                print("Invalid input, try again!")
            elif self.robot.battery == 0 and mode not in ("recharge", "info"):
                print(f"The level of the battery is 0, {self.robot.name} needs recharging!")
            elif self.robot.boredom == 100 and mode not in ("play", "info"):
                print(f"{self.robot.name} is too bored! {self.robot.name} needs to have fun!")
            else:
                if mode == "play":
                    self.robot.play()
                elif mode == "recharge":
                    self.robot.recharge()
                elif mode == "sleep":
                    self.robot.sleep()
                elif mode == "info":
                    self.robot.stats()
                elif mode == "learn":
                    self.robot.learn()
                elif mode == "work":
                    self.robot.work()
                elif mode == "oil":
                    self.robot.oil()
                elif mode == "exit":
                    print("Bye!")
                    break


game = Menu()
game.main_menu()
