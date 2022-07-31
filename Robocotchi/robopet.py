import game_menu


class Robocotchi:

    def __init__(self, name):
        self.name = name
        self.battery = 100
        self.overheat = 0
        self.skills = 0
        self.boredom = 0
        self.rust = 0

    def change_boredom(self, points):
        self.boredom = self.boredom + points
        temporary_boredom = self.boredom
        if temporary_boredom < 0:
            temporary_boredom = 0
        elif temporary_boredom > 100:
            temporary_boredom = 100
        print(f"{self.name}'s level of boredom was {self.boredom - points}. Now it is {temporary_boredom}.")
        if self.boredom < 0:
            self.boredom = 0
        elif self.boredom > 100:
            self.boredom = 100

    def change_temp(self, points):
        self.overheat = self.overheat + points
        temporary_overheat = self.overheat
        if temporary_overheat <= 0:
            temporary_overheat = 0
            print(f"{self.name}'s level of overheat was {self.overheat - points}. Now it is {temporary_overheat}.")
            print(f"{self.name} is cool!")
        else:
            print(f"{self.name} cooled off!")
            print(f"{self.name}'s level of overheat was {self.overheat - points}. Now it is {self.overheat}.")
        if self.overheat < 0:
            self.overheat = 0

    def change_battery_level(self, points):
        self.battery = self.battery + points
        print(f"{self.name}'s level of the battery was {self.battery - points}. Now it is {self.battery}.")

    def change_skills(self, points):
        self.skills = self.skills + points
        temporary_skill = self.skills
        if temporary_skill > 100:
            temporary_skill = 100
        print(f"{self.name}'s level of skill was {self.skills - points}. Now it is {temporary_skill}.")
        if self.skills > 100:
            self.skills = 100

    def change_rust(self, points):
        self.rust = self.rust + points
        temporary_rust = self.rust
        if temporary_rust > 100:
            temporary_rust = 100
        elif temporary_rust < 0:
            temporary_rust = 0
        x = ""
        if points < 0:
            x = f"{self.name} is less rusty!"
        print(f"{self.name}'s level of rust was {self.rust - points}. Now it is {temporary_rust}.", x)
        if self.rust > 100:
            self.rust = 100
        elif self.rust < 0:
            self.rust = 0

    def sleep(self):
        if self.overheat == 0:
            print(f"{self.name} is cool!")
        else:
            self.change_temp(-20)

    def recharge(self):
        if self.battery < 100:
            self.change_temp(-5)
            self.change_battery_level(10)
            self.change_boredom(5)
            print(f"{self.name} is recharged!")
        else:
            print(f"{self.name} is charged!")

    def unpleasant_event(self):
        if self.battery < 10:
            print(f"Guess what! {self.name} fell into the pool!")
            return 50
        elif self.battery < 30:
            print(f"Oh no, {self.name} stepped into a puddle!")
            return 10

    def play(self):
        event = self.unpleasant_event()
        game_menu.choose_game()
        self.change_boredom(-20)
        self.change_temp(10)
        if event:
            self.change_rust(event)
        if self.boredom == 0:
            print(f"{self.name} is in a great mood!")

    def learn(self):
        if self.skills == 100:
            print(f"There's nothing for {self.name} to learn!")
        else:
            event = self.unpleasant_event()
            self.change_skills(10)
            self.change_temp(10)
            self.change_battery_level(-10)
            self.change_boredom(5)
            if event:
                self.change_rust(event)
            print(f"{self.name} has become smarter!")

    def work(self):
        if self.skills < 50:
            print(f"{self.name} has got to learn before working!")
        else:
            event = self.unpleasant_event()
            self.change_boredom(10)
            self.change_battery_level(-10)
            self.change_temp(10)
            if event:
                self.change_rust(event)
            print(f"{self.name} did well!")

    def oil(self):
        if self.rust == 0:
            print(f"{self.name} is fine, no need to oil!")
        else:
            self.change_rust(-20)

    def stats(self):
        print(f"{self.name}'s stats are: battery is {self.battery},")
        print(f"Overheat is {self.overheat},")
        print(f"Skill level is {self.skills},")
        print(f"Boredom is {self.boredom}.")



