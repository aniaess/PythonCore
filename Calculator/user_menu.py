from error_handler import ErrorHandler
from calculator import Calculator
import re


class User:

    def __init__(self):
        self.regex = []
        self.variables = {}

    def menu(self):
        while True:
            user = input()
            if user.startswith("/"):
                if user == "/exit":
                    print("Bye!")
                    break
                elif user == "/help":
                    print("""Calculate math expression.
It support addiction and substraction, multiplication, division""")
                else:
                    print("Unknown command")
            else:
                pattern = r"[\*\+^/-]+|[A-Za-z0-9]+|=|\)|\("
                self.regex = re.findall(pattern, user)
                if self.regex:
                    exceptions = ErrorHandler(self.regex)
                    if "=" in self.regex:
                        self.variables = exceptions.update_variables(self.variables)
                    else:
                        if exceptions.check_parethesis():
                            pass
                        elif exceptions.errors(self.variables):
                            pass
                        elif exceptions.error1(self.variables):
                            pass
                        else:
                            calculator = Calculator(self.variables)
                            if calculator:
                                print(calculator.calculate_result(self.regex))


calc = User()
calc.menu()
